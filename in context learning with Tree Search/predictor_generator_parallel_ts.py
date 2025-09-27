import pandas as pd
import json
import random
import os
import time
import ast
import matplotlib.pyplot as plt
from termcolor import colored
from API_client import make_API_call
from predictor_evaluator import evaluate_predictor
import asyncio
import math
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict, Any

# IMPORTANT VARIABLES
PROVIDER = "OPENROUTER"  # CAN BE ONE OF: OPENROUTER OR OPENAI
CSV_FILE = "complex_dataset.csv"
SAMPLE_SIZE = 10
MODEL_NAME = "openrouter/sonoma-sky-alpha"
OUTPUT_FILE = "generated_predictor.py"
TOTAL_NODES = 1000  # Total nodes for tree search
MISTAKES_TO_SHOW = 10  # Number of mistakes to show per iteration
PREDICTORS_FOLDER = "predictors-SKY-PARALLEL-TS-1"  # Folder to save enumerated predictor files
TOP_PERFORMERS_TO_KEEP = 3  # Number of top performers to preserve between cycles
EXAMPLES_PER_PERFORMER = 10  # Number of failure examples to show per top performer
REFLECTIONS_TO_KEEP = 3  # Number of latest reflections to keep for future cycles
PLOT_FILENAME = "accuracy_progress-SKY-PARALLEL-TS-1.png"
C_PUCT = 1.0  # Exploration constant for PUCT
TREE_CHILDREN_PER_EXPANSION = 4  # Number of children per expansion for better breadth
HYBRIDIZATION_FREQUENCY = 50  # Every N nodes, try hybridization
STAGNATION_CHECK_FREQUENCY = 10  # Check for stagnation every N nodes
TREE_VISUALIZATION_FREQUENCY = 1  # Show tree visualization every N nodes (0 to disable)
HTML_VISUALIZATION_FREQUENCY = 1  # Generate HTML visualization every N nodes (0 to disable)
REFLECTION_FREQUENCY = 3  # Generate periodic reflection every N nodes (0 to disable)
PARALLEL_BRANCHES = 5  # Number of branches to explore in parallel (NEW PARAMETER)

# API Configuration
MAX_API_RETRIES = 10  # Maximum retries for API calls
API_RETRY_DELAY = 2  # Base delay between retries (seconds)
RATE_LIMIT_DELAY = 0.1  # Delay between API calls to avoid rate limiting

class TreeNode:
    """Node in the tree search structure with thread-safe operations."""
    def __init__(self, code="", parent=None, prompt="", lock=None):
        self.code = code
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0.0
        self.accuracy = 0.0
        self.mistakes = []
        self.prompt = prompt
        self.eval_results = None
        self.lock = lock or threading.RLock()  # Thread-safe operations

def plot_accuracy_progress(accuracy_history, node_count, cycle_boundaries=None):
    """Create and save a line plot of accuracy progression with cycle boundaries."""
    plt.figure(figsize=(14, 8))

    # Create x-axis values (nodes)
    nodes = list(range(1, len(accuracy_history) + 1))

    # Plot the accuracy line
    plt.plot(nodes, accuracy_history, 'b-o', linewidth=2, markersize=6, label='Accuracy')

    # Add current node marker with different color
    if node_count <= len(accuracy_history):
        plt.plot(node_count, accuracy_history[node_count-1], 'r*', markersize=12, label=f'Node {node_count}')

    # Add vertical lines for cycle boundaries
    if cycle_boundaries:
        for i, boundary in enumerate(cycle_boundaries):
            if boundary <= len(nodes):
                plt.axvline(x=boundary, color='red', linestyle='--', alpha=0.7, linewidth=2)
                plt.text(boundary + 0.5, max(accuracy_history) * 0.95,
                        f'Cycle {i + 2}',  # Cycle number (i+2 because cycle 1 has no boundaries)
                        rotation=90, verticalalignment='top', fontsize=10, color='red')

    # Customize the plot
    title_suffix = f" - Parallel Tree Search (Branches: {PARALLEL_BRANCHES})"
    plt.title(f'Predictor Accuracy Progression{title_suffix}', fontsize=14, fontweight='bold')
    plt.xlabel('Node Number', fontsize=12)
    plt.ylabel('Accuracy (%)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='lower right')

    # Set y-axis limits with some padding
    if accuracy_history:
        min_acc = min(accuracy_history)
        max_acc = max(accuracy_history)
        padding = (max_acc - min_acc) * 0.1 if max_acc > min_acc else 5
        plt.ylim(max(0, min_acc - padding), min(100, max_acc + padding))

    # Save the plot (overwrite the same file each time)
    plot_filename = PLOT_FILENAME
    plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
    plt.close()

    print(colored(f"📊 Accuracy plot saved as {plot_filename}", "cyan"))

def validate_python_syntax(code_string):
    """Validate Python syntax and return list of errors."""
    errors = []

    try:
        # Try to parse the code as an AST (Abstract Syntax Tree)
        ast.parse(code_string)
    except SyntaxError as e:
        errors.append(f"SyntaxError at line {e.lineno}: {e.msg}")
        if e.text:
            errors.append(f"  Code: {e.text.strip()}")
    except Exception as e:
        errors.append(f"Parse Error: {str(e)}")

    # Additional checks for common issues
    lines = code_string.split('\n')

    # Check for markdown code blocks
    if '```' in code_string:
        errors.append("Markdown code blocks (```) detected - remove all markdown formatting")

    # Check for incomplete function definitions
    if 'def ' in code_string and not code_string.strip().endswith(':'):
        if not any(line.strip().endswith(':') for line in lines if 'def ' in line):
            errors.append("Incomplete function definition - missing colon")

    # Check for unmatched parentheses/brackets
    open_parens = code_string.count('(')
    close_parens = code_string.count(')')
    if open_parens != close_parens:
        errors.append(f"Unmatched parentheses: {open_parens} opening, {close_parens} closing")

    open_brackets = code_string.count('[')
    close_brackets = code_string.count(']')
    if open_brackets != close_brackets:
        errors.append(f"Unmatched brackets: {open_brackets} opening, {close_brackets} closing")

    open_braces = code_string.count('{')
    close_braces = code_string.count('}')
    if open_braces != close_braces:
        errors.append(f"Unmatched braces: {open_braces} opening, {close_braces} closing")

    return errors

async def make_api_call_with_retry(model_name, messages, max_retries=MAX_API_RETRIES):
    """Make API call with retry logic and exponential backoff."""
    for attempt in range(max_retries):
        try:
            print(colored(f"🤖 API Call Attempt {attempt + 1}/{max_retries}", "blue"))

            # Rate limiting delay
            if attempt > 0:
                await asyncio.sleep(RATE_LIMIT_DELAY)

            response = await make_API_call(model_name, messages, PROVIDER)

            if response:
                return response
            else:
                print(colored(f"❌ API call failed (attempt {attempt + 1})", "red"))

        except Exception as e:
            print(colored(f"⚠️  API exception (attempt {attempt + 1}): {e}", "yellow"))

        # Exponential backoff delay
        if attempt < max_retries - 1:
            delay = API_RETRY_DELAY * (2 ** attempt)  # Exponential backoff
            print(colored(f"⏳ Waiting {delay}s before retry...", "cyan"))
            await asyncio.sleep(delay)

    print(colored(f"💀 All {max_retries} API attempts failed", "red"))
    return None

def write_file_with_encoding(filepath, content, description=None):
    """Helper function to write files with consistent encoding."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    if description:
        log_message(f"{description} saved to {filepath}", "cyan")

def save_predictor_with_accuracy(predictor_code, accuracy, node_id, total_predictions=None, correct_predictions=None):
    """Save predictor function to enumerated file with accuracy information."""
    # Create predictors folder if it doesn't exist
    if not os.path.exists(PREDICTORS_FOLDER):
        os.makedirs(PREDICTORS_FOLDER)

    # Create filename with enumeration
    filename = f"{PREDICTORS_FOLDER}/predictor_{node_id}.py"

    # Create header comment with accuracy information
    header_comment = f'''"""
Predictor {node_id}
Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
Accuracy: {accuracy:.2f}%
"""

'''

    # Add accuracy information as inline comment at the top of the function
    accuracy_comment = f'''
# PREDICTOR {node_id} - Accuracy: {accuracy:.2f}%
# Correct predictions: {correct_predictions}/{total_predictions} ({accuracy:.2f}%)
'''

    # Combine header, accuracy comment, and predictor code
    full_content = header_comment + accuracy_comment + "\n" + predictor_code

    # Save to file using helper function
    write_file_with_encoding(filename, full_content, f"💾 Predictor {node_id}")
    return filename

def get_error_type(mistake):
    """Helper function to determine error type for cleaner logic."""
    if not mistake.get('error'):
        return 'prediction'
    if 'Syntax' in str(mistake.get('error', '')):
        return 'syntax'
    return 'execution'

def log_message(message, color="white"):
    """Helper function for consistent colored logging."""
    print(colored(message, color))

def select_random_mistakes(mistakes, num_mistakes=MISTAKES_TO_SHOW):
    """Select random mistakes for improvement feedback."""
    if len(mistakes) <= num_mistakes:
        return mistakes
    return random.sample(mistakes, num_mistakes)

def check_stagnation_pattern(accuracy_history):
    """Check if the same accuracy percentage has been achieved 3 times in a row."""
    if len(accuracy_history) < 3:
        return False, None

    # Check last 3 accuracies
    last_three = accuracy_history[-3:]

    # Check if all three are exactly the same
    if len(set(last_three)) == 1:
        return True, last_three[0]

    return False, None

def create_stagnation_feedback_prompt(stuck_accuracy, node_id, base_prompt):
    """Create a prompt that encourages creative variation when stuck at same accuracy."""
    return f"""{base_prompt}

🚨 STAGNATION DETECTED: You have achieved exactly {stuck_accuracy:.2f}% accuracy for 3 consecutive nodes.

Break this pattern with creative mathematical innovation. Try different approaches, combine features in new ways, and explore alternative logical structures. Be constructively creative while maintaining mathematical validity.

REMINDER: Your function MUST be able to predict ALL 4 categories (1, 2, 3, and 4) - not just some of them. Study the training data to understand when each category should be predicted."""

def extract_top_performers(cycle_results):
    """Extract the top performing functions from a cycle."""
    if not cycle_results:
        return []

    # Sort by accuracy descending
    sorted_results = sorted(cycle_results, key=lambda x: x['accuracy'], reverse=True)

    # Return top performers
    top_performers = sorted_results[:TOP_PERFORMERS_TO_KEEP]

    print(colored(f"🏆 Top {len(top_performers)} performers extracted:", "green"))
    for i, performer in enumerate(top_performers, 1):
        print(colored(f"  {i}. Accuracy: {performer['accuracy']:.2f}% (Node {performer['node_id']})", "green"))

    return top_performers

def collect_failure_examples(top_performers, all_cycle_results):
    """Collect failure examples from the top performers."""
    failure_examples = {}

    for performer in top_performers:
        node_id = performer['node_id']
        performer_key = f"node_{node_id}"

        # Find the results for this performer
        performer_result = next((r for r in all_cycle_results if r['node_id'] == node_id), None)

        if performer_result and 'mistakes' in performer_result:
            mistakes = performer_result['mistakes']
            # Select random examples of failures (limit to EXAMPLES_PER_PERFORMER)
            selected_mistakes = select_random_mistakes(mistakes, EXAMPLES_PER_PERFORMER)
            failure_examples[performer_key] = {
                'accuracy': performer['accuracy'],
                'function': performer['function'],
                'mistakes': selected_mistakes
            }
            print(colored(f"📝 Collected {len(selected_mistakes)} failure examples for Node {node_id}", "cyan"))

    return failure_examples

def create_improved_prompt(base_prompt, mistakes, node_id, eval_results=None, failure_examples=None, cycle_number=1):
    """Create an improved prompt that includes mistake history and top performers from previous cycles."""
    if not mistakes and not failure_examples:
        return base_prompt

    mistakes_text = "\n".join([
        f"❌ {get_error_type(m).upper()} ERROR #{mistakes.index(m) + 1}:\n" +
        (f"   Input: A={m['input'].get('A', 'N/A')}, B={m['input'].get('B', 'N/A')}, C={m['input'].get('C', 'N/A')}, D={m['input'].get('D', 'N/A')}, E={m['input'].get('E', 'N/A')}\n"
         f"   Execution Error: {m['error']}\n"
         f"   The function crashed with this input!\n"
         f"   Expected: Input({m['input'].get('A', 'N/A')}, {m['input'].get('B', 'N/A')}, {m['input'].get('C', 'N/A')}, {m['input'].get('D', 'N/A')}, {m['input'].get('E', 'N/A')}) should give Output = {m['actual']}\n"
         f"   Fix: Ensure your function handles this input combination without errors"
         if m.get('error') and 'Syntax' not in str(m.get('error', '')) else
         f"   Syntax/Code Error: {m['error']}\n"
         f"   The generated code has syntax errors and cannot be executed!\n"
         f"   Fix: Correct the syntax errors in your generated code before testing"
         if m.get('error') and 'Syntax' in str(m.get('error', '')) else
         f"   Input: A={m['input']['A']}, B={m['input']['B']}, C={m['input']['C']}, D={m['input']['D']}, E={m['input']['E']}\n"
         f"   Your prediction: {m['predicted']}\n"
         f"   Correct output: {m['actual']}\n"
         f"   Expected: Input({m['input']['A']}, {m['input']['B']}, {m['input']['C']}, {m['input']['D']}, {m['input']['E']}) should give Output = {m['actual']}")
        for m in mistakes
    ])

    # Check for different types of errors using helper function
    execution_errors = [m for m in mistakes if get_error_type(m) == 'execution']
    syntax_errors = [m for m in mistakes if get_error_type(m) == 'syntax']
    prediction_errors = [m for m in mistakes if get_error_type(m) == 'prediction']

    has_execution_errors = len(execution_errors) > 0
    has_syntax_errors = len(syntax_errors) > 0
    has_prediction_errors = len(prediction_errors) > 0

    # Get accuracy information if available
    accuracy_info = ""
    improvement_target = ""
    if eval_results:
        accuracy_info = f"\n📊 CURRENT PERFORMANCE: The previous function achieved {eval_results['overall_accuracy']:.2f}% accuracy ({eval_results['correct_predictions']}/{eval_results['total_rows']} correct predictions)"
        improvement_target = f"\n📈 IMPROVEMENT TARGET: Aim to exceed {eval_results['overall_accuracy']:.2f}% accuracy by fixing these issues"

    improvement_message = f"""
🔧 CYCLE {cycle_number} IMPROVEMENT REQUEST{accuracy_info}

Your previous predictor function made these specific mistakes on test data:
{mistakes_text}{improvement_target}

📚 LEARNING OBJECTIVES:
1. Analyze the mathematical relationships between inputs (A, B, C, D, E) and correct outputs using basic arithmetic
2. Identify simple patterns that should map specific input combinations to correct outputs
3. Improve your mathematical formulas using sums, differences, ratios, and comparisons
4. Ensure generalization to similar patterns in the full dataset
5. Draw inspiration from successful patterns while exploring new approaches
6. Balance proven techniques with creative mathematical innovation
7. Focus on clear, understandable mathematical relationships - avoid complex or domain-specific concepts
8. CRITICAL: Your function MUST predict ALL 4 categories (1, 2, 3, and 4) - not just some of them
{f'9. CRITICAL: Fix all syntax errors - your generated code must be valid Python syntax' if has_syntax_errors else ''}
{f'10. CRITICAL: Fix all execution errors - your function must handle all input combinations without crashing' if has_execution_errors else ''}

🎨 CREATIVITY GUIDELINES:
- Study previous high-accuracy patterns for inspiration, not imitation
- Explore novel mathematical combinations using basic arithmetic
- Try creative combinations of sums, differences, ratios, and products
- Combine features in simple but effective ways (A+B, A-B, A*B, A/B, A+B-C, etc.)
- Avoid complex mathematical concepts or domain-specific terminology
- Be intelligently creative using basic mathematical operations

{f'🚨 SYNTAX ERRORS DETECTED: Your generated code has syntax errors and cannot be executed! This is critical - fix syntax first.' if has_syntax_errors else ''}
{f'🚨 EXECUTION ERRORS DETECTED: Your function crashed on {len(execution_errors)} input combinations! Fix these immediately.' if has_execution_errors else ''}

🎯 SPECIFIC CORRECTIONS NEEDED:
{f'- Fix syntax errors: {", ".join([m["error"].replace("Syntax Error: ", "") for m in syntax_errors[:3]])}' if has_syntax_errors else ''}
{f'- When input values are like: {", ".join([f"(A={m["input"]["A"]}, B={m["input"]["B"]}, C={m["input"]["C"]})" for m in prediction_errors[:2]])}' if has_prediction_errors else ''}
{f'- The function should return: {", ".join([str(m["actual"]) for m in prediction_errors[:2]])}' if has_prediction_errors else ''}
{f'- Instead of returning: {", ".join([str(m["predicted"]) for m in prediction_errors[:2]])}' if has_prediction_errors else ''}
- REMEMBER: Your function MUST be able to predict ALL 4 categories (1, 2, 3, and 4) - not just some of them
- Analyze the training data to understand when each category should be predicted

🔬 INNOVATION STRATEGIES:
- Study the conversation history for simple, effective patterns
- Try basic mathematical combinations: sums, differences, ratios, products
- Experiment with simple feature interactions: A+B, A-B, A*B, A/B, min(A,B), max(A,B)
- Consider conditional logic based on simple comparisons (A > B, A + B > C, etc.)
- Focus on clear, understandable mathematical relationships
- Be creative with basic operations - avoid complex formulas or domain-specific approaches

💡 CREATIVITY GUIDANCE:
- Reuse successful code patterns and structures from high accuracy samples that exist so far
- Combine the best elements from high-performing functions with new basic mathematical innovations
- Build incrementally upon proven successful approaches
- Think creatively with arithmetic operations while maintaining mathematical validity
- Consider simple multi-stage calculations using basic operations
- Never repeat code in its entirety - always modify and improve upon successful patterns

{f'⚠️  PRIORITY ORDER: 1) Fix syntax errors 2) Fix execution errors 3) Improve accuracy' if has_syntax_errors or has_execution_errors else ''}

{f'''🎯 CROSS-CYCLE LEARNING - CYCLE {cycle_number}
From previous cycles, here are the top performing functions and their failure patterns.
Study these successful approaches and learn from their mistakes:

''' + "\n".join([
    f"""TOP PERFORMER #{i+1} (Accuracy: {performer_data['accuracy']:.2f}%):
Function Code:
```python
{performer_data['function']}
```

Failure Examples ({len(performer_data['mistakes'])} cases):
""" + "\n".join([
    f"❌ Case {j+1}: Input(A={m['input'].get('A', 'N/A')}, B={m['input'].get('B', 'N/A')}, C={m['input'].get('C', 'N/A')}, D={m['input'].get('D', 'N/A')}, E={m['input'].get('E', 'N/A')}) → Expected: {m.get('actual', 'N/A')}, Got: {m.get('predicted', 'N/A')}"
    for j, m in enumerate(performer_data['mistakes'][:5])  # Show first 5 mistakes per performer
]) + "\n\nKey Learning: " +
    ("This function excelled at " + (", ".join([f"cases with A={m['input'].get('A', 'N/A')}" for m in performer_data['mistakes'][:2]])) if performer_data['mistakes'] else "This function showed strong overall performance")
    for i, (performer_key, performer_data) in enumerate((failure_examples or {}).items())
]) + '''

🔬 CROSS-CYCLE INSIGHTS:
- Analyze the mathematical patterns that made these top performers successful
- Identify common failure modes across different approaches
- Combine the strengths of multiple successful functions
- Avoid the specific mistake patterns shown above
- Build upon proven mathematical relationships while innovating new combinations

''' if failure_examples else ''}

Generate an improved predictor function that correctly handles these specific cases and maintains accuracy on the broader dataset.

📝 FINAL NOTE: If high accuracy samples exist so far, you can use parts of them for inspiration. Build incrementally upon proven approaches while adding creative innovations using basic mathematical operations. Never repeat code in its entirety - always modify and improve upon successful patterns. Combine the best elements from high-performing functions with new mathematical discoveries.
"""

    return base_prompt + improvement_message

def get_rank_score(node, all_nodes):
    """Get rank-normalized score for a node across all evaluated nodes."""
    if not all_nodes:
        return 0.0

    # Get all nodes with accuracy > 0
    evaluated_nodes = [n for n in all_nodes if n.accuracy > 0]

    if not evaluated_nodes:
        return 0.0

    # Sort by accuracy (descending)
    sorted_nodes = sorted(evaluated_nodes, key=lambda x: x.accuracy, reverse=True)

    # Find rank of this node
    try:
        rank = sorted_nodes.index(node) + 1  # 1-based rank
        total_nodes = len(sorted_nodes)
        # Normalize rank to [0, 1] where 1 is best
        return 1.0 - (rank - 1) / max(1, total_nodes - 1)
    except ValueError:
        # Node not found in evaluated nodes
        return 0.0

def collect_all_nodes(root):
    """Collect all nodes in the tree."""
    all_nodes = []
    def collect(node):
        all_nodes.append(node)
        for child in node.children:
            collect(child)
    collect(root)
    return all_nodes

def print_tree_visualization(root, max_depth=4, show_current_path=None):
    """Print tree visualization to terminal."""
    print("\n" + "="*80)
    tree_viz = visualize_tree(root, max_depth, show_current_path)
    print(tree_viz)
    print("="*80 + "\n")

def generate_html_tree_visualization(root, node_count, cycle_number, parallel_branches=PARALLEL_BRANCHES, filename=None, show_current_path=None):
    """Generate a compact HTML visualization of the tree structure (single file that gets updated)."""
    if not filename:
        filename = "tree_visualization.html"

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tree Search Visualization</title>
    <style>
        body {{
            font-family: 'Courier New', monospace;
            margin: 0;
            padding: 10px;
            background: #000;
            color: #fff;
            font-size: 11px;
            line-height: 1.2;
        }}

        .header {{
            background: #333;
            padding: 5px 10px;
            margin-bottom: 10px;
            border-radius: 3px;
        }}

        .header h1 {{
            margin: 0;
            font-size: 14px;
            font-weight: normal;
        }}

        .stats {{
            display: flex;
            justify-content: space-between;
            background: #222;
            padding: 5px 10px;
            margin-bottom: 10px;
            border-radius: 3px;
            font-size: 10px;
        }}

        .tree-container {{
            font-family: 'Courier New', monospace;
            font-size: 10px;
            line-height: 1.1;
            white-space: pre;
            background: #111;
            padding: 10px;
            border-radius: 3px;
            overflow-x: auto;
            max-height: 80vh;
            overflow-y: auto;
        }}

        .node-high {{ color: #0f0; }}
        .node-medium {{ color: #ff0; }}
        .node-low {{ color: #f80; }}
        .node-zero {{ color: #888; }}
        .current-path {{ color: #f0f; font-weight: bold; }}

        .legend {{
            position: fixed;
            top: 10px;
            right: 10px;
            background: #333;
            padding: 5px;
            border-radius: 3px;
            font-size: 9px;
        }}

        .legend-item {{
            display: block;
            margin: 2px 0;
        }}

        .refresh-info {{
            position: fixed;
            bottom: 10px;
            right: 10px;
            background: #333;
            padding: 5px;
            border-radius: 3px;
            font-size: 9px;
            color: #aaa;
        }}
    </style>
    <script>
        // Auto-refresh every 5 seconds
        setTimeout(function() {{
            location.reload();
        }}, 5000);
    </script>
</head>
<body>
    <div class="legend">
        <div class="legend-item"><span style="color: #0f0">🟢</span> ≥90% Accuracy</div>
        <div class="legend-item"><span style="color: #ff0">🟡</span> ≥70% Accuracy</div>
        <div class="legend-item"><span style="color: #f80">🟠</span> >0% Accuracy</div>
        <div class="legend-item"><span style="color: #888">⚪</span> 0% Accuracy</div>
        <div class="legend-item"><span style="color: #f0f">🟣</span> Current Path</div>
    </div>

    <div class="refresh-info">
        Auto-refresh: 5s<br>
        Last update: {pd.Timestamp.now().strftime('%H:%M:%S')}
    </div>

    <div class="header">
        <h1>🌳 Parallel Tree Search - Node {node_count} • Cycle {cycle_number} • {parallel_branches} Branches</h1>
    </div>

    <div class="stats">
        <span>Total Nodes: {len(collect_all_nodes(root))}</span>
        <span>Evaluated: {len([n for n in collect_all_nodes(root) if n.accuracy > 0])}</span>
        <span>Best: {max((n.accuracy for n in collect_all_nodes(root)), default=0):.1f}%</span>
        <span>Avg: {sum(n.accuracy for n in collect_all_nodes(root) if n.accuracy > 0) / max(1, len([n for n in collect_all_nodes(root) if n.accuracy > 0])):.1f}%</span>
    </div>

    <div class="tree-container">
'''

    def get_node_symbol(accuracy):
        """Get the symbol for a node based on its accuracy (matching terminal output)."""
        if accuracy >= 90:
            return "🟢"
        elif accuracy >= 70:
            return "🟡"
        elif accuracy > 0:
            return "🟠"
        else:
            return "⚪"

    def get_node_class(accuracy):
        """Get CSS class based on accuracy."""
        if accuracy >= 90:
            return "node-high"
        elif accuracy >= 70:
            return "node-medium"
        elif accuracy > 0:
            return "node-low"
        else:
            return "node-zero"

    def build_ascii_tree(node, prefix="", is_last=True, depth=0, max_depth=8):
        """Build ASCII tree structure like terminal output."""
        if depth > max_depth:
            return f"{prefix}{'└── ' if is_last else '├── '}... (depth limit)\n"

        # Node information
        symbol = get_node_symbol(node.accuracy)
        accuracy_str = f"{node.accuracy:.1f}%" if node.accuracy > 0 else "0.0%"
        visits_str = f"v{node.visits}"
        value_str = f"val{node.value:.1f}" if node.visits > 0 else "val0.0"

        # Check if this node is in the current path
        is_in_path = show_current_path and node in show_current_path
        path_class = " current-path" if is_in_path else ""

        # Create the node line
        node_line = f'<span class="{get_node_class(node.accuracy)}{path_class}">{symbol} {accuracy_str} {visits_str} {value_str}</span>'

        # Add connector
        if depth == 0:
            result = f"{node_line}\n"
        else:
            connector = "└── " if is_last else "├── "
            result = f"{prefix}{connector}{node_line}\n"

        # Add children
        if node.children and depth < max_depth:
            for i, child in enumerate(node.children):
                is_last_child = (i == len(node.children) - 1)
                extension = "    " if is_last_child else "│   "
                result += build_ascii_tree(child, prefix + extension, is_last_child, depth + 1, max_depth)

        return result

    # Build the ASCII-style tree HTML
    tree_ascii = build_ascii_tree(root)

    # Add tree statistics
    all_nodes = collect_all_nodes(root)
    total_nodes = len(all_nodes)
    evaluated_nodes = len([n for n in all_nodes if n.accuracy > 0])

    html_content += f'''{tree_ascii}
===============================================================================
🌳 Tree Summary: {total_nodes} nodes | {evaluated_nodes} evaluated
===============================================================================
    </div>
</body>
</html>'''

    # Save the HTML file
    write_file_with_encoding(filename, html_content, f"HTML tree visualization saved")
    print(colored(f"🌳 HTML tree visualization saved as {filename}", "green"))

    return filename

def visualize_tree(root, max_depth=4, show_current_path=None):
    """Create an ASCII visualization of the tree structure."""
    def get_node_symbol(node, is_current=False):
        """Get the symbol for a node based on its state."""
        if is_current:
            return "🔍"  # Current node being explored
        elif node.accuracy >= 90:
            return "🟢"  # High accuracy
        elif node.accuracy >= 70:
            return "🟡"  # Medium accuracy
        elif node.accuracy > 0:
            return "🟠"  # Low accuracy
        else:
            return "⚪"  # No accuracy yet

    def build_tree_string(node, prefix="", is_last=True, depth=0, current_path=None):
        """Recursively build the tree string."""
        if depth > max_depth:
            return f"{prefix}{'└── ' if is_last else '├── '}... (depth limit)\n"

        # Check if this node is in the current exploration path
        in_current_path = current_path and node in current_path

        # Node symbol and info
        symbol = get_node_symbol(node, in_current_path)
        accuracy_str = f"{node.accuracy:.1f}%" if node.accuracy > 0 else "0.0%"
        visits_str = f"v{node.visits}"
        value_str = f"val{node.value:.1f}" if node.visits > 0 else "val0.0"

        # Create the node line
        node_line = f"{symbol} {accuracy_str} {visits_str} {value_str}"

        # Add connector
        if depth == 0:
            result = f"{node_line}\n"
        else:
            connector = "└── " if is_last else "├── "
            result = f"{prefix}{connector}{node_line}\n"

        # Add children
        if node.children and depth < max_depth:
            for i, child in enumerate(node.children):
                is_last_child = (i == len(node.children) - 1)
                extension = "    " if is_last else "│   "
                result += build_tree_string(
                    child,
                    prefix + extension,
                    is_last_child,
                    depth + 1,
                    current_path
                )

        return result

    # Build the visualization
    tree_str = build_tree_string(root, current_path=show_current_path)

    # Add summary statistics
    all_nodes = collect_all_nodes(root)
    total_nodes = len(all_nodes)
    evaluated_nodes = len([n for n in all_nodes if n.accuracy > 0])
    avg_accuracy = sum(n.accuracy for n in all_nodes if n.accuracy > 0) / max(1, evaluated_nodes)
    max_accuracy = max((n.accuracy for n in all_nodes), default=0)

    summary = f"""
🌳 Tree Visualization (depth limit: {max_depth})
📊 Summary: {total_nodes} nodes | {evaluated_nodes} evaluated | Avg: {avg_accuracy:.1f}% | Max: {max_accuracy:.1f}%
🔍 Legend: 🟢≥90% 🟡≥70% 🟠>0% ⚪=0% 🔍=current path
"""

    return summary + tree_str

def puct_score(node, total_visits, c_puct=C_PUCT, parent=None, all_nodes=None):
    """Calculate PUCT score for a node using Q-values and exploration."""
    if node.visits == 0:
        return float('inf')  # Encourage exploration of unvisited nodes

    # Q-value: learned value estimate (average of outcomes), normalized to 0-1 scale
    q_value = (node.value / max(1, node.visits)) / 100.0  # Normalize from 0-100 to 0-1

    # Alternative: Use rank-based scoring instead of raw Q-value
    if all_nodes:
        rank_score = get_rank_score(node, all_nodes)
        # Blend Q-value and rank score
        q_value = 0.7 * q_value + 0.3 * rank_score

    # Exploration term (corrected PUCT formula)
    exploration = c_puct * math.sqrt(math.log(total_visits + 1) / (node.visits + 1))

    # Principled prior: 1 / max(1, len(parent.children)) integrated into exploration
    if parent and parent.children:
        prior_factor = 1.0 / max(1, len(parent.children))
        exploration *= prior_factor

    return q_value + exploration

def select_multiple_nodes(root, num_branches=PARALLEL_BRANCHES):
    """Select multiple nodes to expand in parallel using PUCT with rank-based scoring."""
    selected_nodes_and_paths = []
    selected_leaves = set()  # Track selected leaf nodes to avoid duplicates

    for _ in range(num_branches):
        current = root
        path = [current]

        while current.children:
            # Calculate total visits for the current node's children
            total_visits = sum(child.visits for child in current.children)

            # Collect all nodes for rank-based scoring
            all_nodes = collect_all_nodes(root)

            # Filter out already selected leaves and get available children
            available_children = [child for child in current.children if child not in selected_leaves]

            # If no available children, break (shouldn't happen in a properly balanced tree)
            if not available_children:
                break

            # Select child with highest PUCT score from available children
            best_child = max(available_children, key=lambda child: puct_score(child, total_visits, parent=current, all_nodes=all_nodes))
            current = best_child
            path.append(current)

        # Mark this leaf as selected to avoid duplicates
        selected_leaves.add(current)
        selected_nodes_and_paths.append((current, path))

    return selected_nodes_and_paths

def backpropagate(path, value):
    """Backpropagate the value up the tree (thread-safe)."""
    for node in reversed(path):
        with node.lock:
            node.visits += 1
            node.value += value

async def process_single_branch(branch_id, selected_node, path, conversation_histories, accuracy_history, cycle_number,
                              failure_examples, global_node_id_counter, base_prompt, best_accuracy, best_node, node_count):
    """Process a single branch with parallel children generation and evaluation."""
    print(colored(f"🌿 BRANCH {branch_id}: Selected node with accuracy: {selected_node.accuracy:.2f}%", "cyan"))

    # Check for stagnation every STAGNATION_CHECK_FREQUENCY nodes
    is_stagnant = False
    stuck_accuracy = None
    if node_count % STAGNATION_CHECK_FREQUENCY == 0 and len(accuracy_history) >= 3:
        last_three = accuracy_history[-3:]
        if len(set(last_three)) == 1 and last_three[0] > 0:
            is_stagnant = True
            stuck_accuracy = last_three[0]
            print(colored(f"🔄 BRANCH {branch_id}: STAGNATION DETECTED: {stuck_accuracy:.2f}% accuracy repeated 3 times", "yellow"))

    # Hybridization: Every HYBRIDIZATION_FREQUENCY nodes, try hybridization two top performers
    is_hybridization = False
    hybridization_prompt = None
    if node_count % HYBRIDIZATION_FREQUENCY == 0 and len(accuracy_history) > 1:
        # Find top two performers in the tree
        all_nodes = collect_all_nodes(path[0])  # Root is path[0]
        top_nodes = sorted([n for n in all_nodes if n.accuracy > 0], key=lambda x: x.accuracy, reverse=True)
        if len(top_nodes) >= 2:
            top1, top2 = top_nodes[0], top_nodes[1]
            hybridization_prompt = f"""
🎯 HYBRIDIZATION REQUEST: Create a new predictor function that combines the best aspects of these two successful approaches:

TOP PERFORMER 1 (Accuracy: {top1.accuracy:.2f}%):
```python
{top1.code}
```

TOP PERFORMER 2 (Accuracy: {top2.accuracy:.2f}%):
```python
{top2.code}
```

Requirements:
- Analyze the mathematical patterns that made each successful
- Create a hybrid that combines their strengths while avoiding their weaknesses
- Use simple arithmetic operations and conditional logic
- CRITICAL: The hybrid function MUST be able to predict ALL 4 categories (1, 2, 3, and 4) - not just some of them
- Study both functions to understand how they handle different categories
- Ensure the hybrid can handle cases that should return category 1, 2, 3, AND 4
- Return only the Python function code

HYBRID FUNCTION:
"""
            is_hybridization = True
            print(colored(f"🔗 BRANCH {branch_id}: Attempting hybridization of top two performers", "magenta"))

    # Generate new prompt for expansion
    current_prompt = selected_node.prompt

    # Apply stagnation feedback if detected
    if is_stagnant and stuck_accuracy:
        current_prompt = create_stagnation_feedback_prompt(stuck_accuracy, global_node_id_counter['value'], current_prompt)
        print(colored(f"💡 BRANCH {branch_id}: Applied stagnation feedback to prompt", "yellow"))

    # Apply hybridization prompt if applicable
    if hybridization_prompt:
        current_prompt = hybridization_prompt
        print(colored(f"🔗 BRANCH {branch_id}: Using hybridization prompt", "magenta"))

    # Get conversation history for this branch (thread-safe)
    with global_node_id_counter['lock']:
        if selected_node in conversation_histories:
            conversation_history = conversation_histories[selected_node].copy()
        else:
            conversation_history = [{"role": "user", "content": current_prompt}]

    # Inject best function context for exploitation
    best_function_context = ""
    if best_node and best_node.code and best_accuracy > 0:
        best_function_context = f"""

💡 CURRENT BEST FUNCTION (Accuracy: {best_accuracy:.2f}%):
```python
{best_node.code}
```

LEARN FROM THIS SUCCESS: Study the mathematical patterns and approaches that made this function effective.
"""

    # If node has mistakes, create improved prompt
    if selected_node.mistakes:
        improved_base_prompt = base_prompt + best_function_context
        current_prompt = create_improved_prompt(
            improved_base_prompt,
            select_random_mistakes(selected_node.mistakes),
            global_node_id_counter['value'],
            selected_node.eval_results,
            failure_examples if cycle_number > 1 else None,
            cycle_number
        )

    # Always append the current prompt to conversation history before API call
    conversation_history.append({"role": "user", "content": current_prompt})

    # Save the current prompt (branch-specific)
    branch_prompt_file = f"prompt_branch_{branch_id}.txt"
    write_file_with_encoding(branch_prompt_file, current_prompt)

    print(colored(f"🤖 BRANCH {branch_id}: Sending request to {MODEL_NAME}...", "yellow"))

    response = await make_api_call_with_retry(MODEL_NAME, conversation_history)

    branch_results = {
        'branch_id': branch_id,
        'selected_node': selected_node,
        'path': path,
        'conversation_history': conversation_history,
        'current_prompt': current_prompt,
        'response': response,
        'children_data': [],
        'eval_results': None,
        'accuracy': 0.0
    }

    if response:
        generated_function = response.choices[0].message.content.strip()

        # Clean up the response
        if generated_function.startswith("```python"):
            generated_function = generated_function[9:]
        if generated_function.startswith("```"):
            generated_function = generated_function[3:]
        if generated_function.endswith("```"):
            generated_function = generated_function[:-3]
        elif "```" in generated_function:
            generated_function = generated_function.split("```")[0]
        generated_function = generated_function.strip()

        # Validate function
        if not generated_function or 'def predict_output' not in generated_function:
            print(colored(f"❌ BRANCH {branch_id}: Invalid response: Missing predict_output function", "red"))
            backpropagate(path, 0.0)
            return branch_results

        print(colored(f"✅ BRANCH {branch_id}: Received valid function from model", "green"))

        # Validate syntax
        syntax_errors = validate_python_syntax(generated_function)
        if syntax_errors:
            print(colored(f"🚨 BRANCH {branch_id}: SYNTAX ERRORS DETECTED: {len(syntax_errors)} issues found", "red"))
            for error in syntax_errors:
                print(colored(f"  • {error}", "red"))

            # Store syntax error
            syntax_mistake = {
                'error': f"Syntax Error: {'; '.join(syntax_errors)}",
                'input': {},
                'predicted': None,
                'actual': None
            }

            # Create child node with syntax error
            child_node = TreeNode(
                code=generated_function,
                parent=selected_node,
                prompt=current_prompt
            )
            child_node.mistakes = [syntax_mistake]

            # Thread-safe tree operations
            with selected_node.lock:
                selected_node.children.append(child_node)

            backpropagate(path + [child_node], 0.0)

            # Update conversation histories (thread-safe)
            with global_node_id_counter['lock']:
                conversation_histories[child_node] = conversation_history + [{"role": "assistant", "content": f"```python\n{generated_function}\n```"}]
            return branch_results

        # Save and evaluate the function (branch-specific file)
        branch_output_file = f"generated_predictor_branch_{branch_id}.py"
        write_file_with_encoding(branch_output_file, generated_function, f"Function saved to {branch_output_file}")
        conversation_history.append({"role": "assistant", "content": f"```python\n{generated_function}\n```"})

        # Update conversation histories (thread-safe)
        with global_node_id_counter['lock']:
            conversation_histories[selected_node] = conversation_history

        print(colored(f"\n📊 BRANCH {branch_id}: Evaluating predictor accuracy...", "yellow"))
        eval_results = await evaluate_predictor(CSV_FILE, branch_output_file)

        branch_results['eval_results'] = eval_results

        if eval_results:
            current_accuracy = eval_results['overall_accuracy']
            branch_results['accuracy'] = current_accuracy

            # PARALLEL CHILD GENERATION AND EVALUATION
            print(colored(f"🌿 BRANCH {branch_id}: Generating and evaluating {TREE_CHILDREN_PER_EXPANSION} children in parallel", "cyan"))

            # Prepare all children for parallel processing
            children_data = []

            # Main child data
            with global_node_id_counter['lock']:
                main_child_node_id = global_node_id_counter['value']
                global_node_id_counter['value'] += 1

            children_data.append({
                'type': 'main',
                'node_id': main_child_node_id,
                'branch_id': branch_id,
                'code': generated_function,
                'prompt': current_prompt,
                'conversation_history': conversation_history,
                'output_file': branch_output_file,
                'eval_results': eval_results,
                'accuracy': current_accuracy
            })

            # Generate variation prompts and data
            for child_idx in range(TREE_CHILDREN_PER_EXPANSION - 1):
                with global_node_id_counter['lock']:
                    variation_node_id = global_node_id_counter['value']
                    global_node_id_counter['value'] += 1

                varied_prompt = current_prompt + f"\n\nVARIATION {child_idx + 1}: Try a different mathematical approach while maintaining the core successful patterns."
                variation_output_file = f"generated_predictor_branch_{branch_id}_variation_{child_idx + 1}.py"

                children_data.append({
                    'type': 'variation',
                    'node_id': variation_node_id,
                    'branch_id': branch_id,
                    'prompt': varied_prompt,
                    'conversation_history': conversation_history,
                    'output_file': variation_output_file,
                    'code': None,  # Will be generated
                    'eval_results': None,
                    'accuracy': None
                })

            # Create tasks for parallel API calls (only for variations that need code generation)
            generation_tasks = []
            for child_data in children_data:
                if child_data['type'] == 'variation':
                    task = make_api_call_with_retry(
                        MODEL_NAME,
                        child_data['conversation_history'] + [{"role": "user", "content": child_data['prompt']}]
                    )
                    generation_tasks.append((child_data, task))

            # Execute all generation tasks in parallel
            if generation_tasks:
                print(colored(f"🤖 BRANCH {branch_id}: Generating {len(generation_tasks)} variation codes in parallel", "yellow"))
                generation_results = await asyncio.gather(*[task for _, task in generation_tasks])

                # Process generation results
                for (child_data, _), response in zip(generation_tasks, generation_results):
                    if response:
                        variation_function = response.choices[0].message.content.strip()

                        # Clean up variation response
                        if variation_function.startswith("```python"):
                            variation_function = variation_function[9:]
                        if variation_function.startswith("```"):
                            variation_function = variation_function[3:]
                        if variation_function.endswith("```"):
                            variation_function = variation_function[:-3]
                        elif "```" in variation_function:
                            variation_function = variation_function.split("```")[0]
                        variation_function = variation_function.strip()

                        # Validate variation function
                        if variation_function and 'def predict_output' in variation_function:
                            variation_errors = validate_python_syntax(variation_function)
                            if not variation_errors:
                                child_data['code'] = variation_function
                                # Save variation code temporarily
                                write_file_with_encoding(child_data['output_file'], variation_function, f"Variation saved")

            # Create evaluation tasks for all children that have valid code
            evaluation_tasks = []
            valid_children_data = []

            for child_data in children_data:
                if child_data['code'] or child_data['type'] == 'main':
                    valid_children_data.append(child_data)

            # Create evaluation tasks for variations (main already evaluated)
            for child_data in valid_children_data:
                if child_data['type'] == 'variation':
                    task = evaluate_predictor(CSV_FILE, child_data['output_file'])
                    evaluation_tasks.append((child_data, task))

            # Execute all evaluation tasks in parallel
            if evaluation_tasks:
                print(colored(f"📊 BRANCH {branch_id}: Evaluating {len(evaluation_tasks)} variations in parallel", "yellow"))
                evaluation_results = await asyncio.gather(*[task for _, task in evaluation_tasks])

                # Process evaluation results
                for (child_data, _), eval_result in zip(evaluation_tasks, evaluation_results):
                    if eval_result:
                        child_data['eval_results'] = eval_result
                        child_data['accuracy'] = eval_result['overall_accuracy']

            branch_results['children_data'] = valid_children_data

        else:
            print(colored(f"❌ BRANCH {branch_id}: Evaluation failed", "red"))
    else:
        print(colored(f"❌ BRANCH {branch_id}: Failed to get response from model", "red"))

    return branch_results

async def generate_predictor():
    print(colored("🔍 Reading dataset...", "cyan"))

    # Read CSV and get sample
    df = pd.read_csv(CSV_FILE)
    sample_df = df.sample(SAMPLE_SIZE)  # Random sample instead of first N rows

    print(colored(f"✅ Loaded {len(sample_df)} rows from dataset", "green"))

    # Format data for the model (include Output column for training)
    data_preview = sample_df.to_string(index=False)

    base_prompt = f"""
Based on the following dataset sample with {SAMPLE_SIZE} rows, create a Python function that perfectly predicts the 'Output' column (which has 4 categories: 1, 2, 3, 4).

Dataset structure:
- Input columns: A, B, C, D, E (all numeric)
- Output column: Output (categorical: 1-4)
- All columns including Output are provided for training

Sample data:
{data_preview}

Requirements:
- Create a function called 'predict_output' that takes A, B, C, D, E as parameters
- The function MUST be able to predict ALL 4 categories (1, 2, 3, and 4) - not just some of them
- For different input combinations, the function should return 1, 2, 3, or 4 as appropriate
- Analyze the provided training data (including Output values) to learn patterns for ALL categories
- Use SIMPLE mathematical operations: arithmetic (+, -, *, /), comparisons (<, >, <=, >=), and basic logic
- Keep the function simple and readable - avoid complex formulas or domain-specific concepts
- Only return the Python function code, no explanations
- Do NOT use machine learning concepts, statistical methods, or domain-specific terminology
- Focus on basic mathematical relationships and conditional logic

CRITICAL REQUIREMENT:
- Your function MUST handle cases that should return category 1, category 2, category 3, AND category 4
- Do not create a function that only predicts 2-3 categories - it must predict ALL 4 categories
- Study the training data to understand when each category (1, 2, 3, 4) should be predicted

Important Instructions:
- Get inspired by previous high-accuracy code examples but remain intelligently creative
- Explore new mathematical approaches using basic arithmetic and comparisons
- Reuse successful patterns and code structures that have shown potential from high accuracy samples
- Combine proven techniques from high-performing functions with new innovations
- Use simple mathematical operations: sums, differences, ratios, products, min/max, averages
- Avoid complex mathematical concepts, logarithms, exponentials, or trigonometric functions unless absolutely necessary
- Focus on clear, understandable mathematical relationships

Return only the Python function code in between ```python and ```:
"""

    # Tree Search variables
    root = TreeNode(prompt=base_prompt)
    best_accuracy = 0.0
    best_node = root
    accuracy_history = []
    cycle_number = 1
    cycle_boundaries = []
    failure_examples = {}
    reflection_history = []

    # Thread-safe global node ID counter
    global_node_id_counter = {'value': 0, 'lock': threading.Lock()}

    # Conversation history for the tree
    conversation_histories = {root: [{"role": "user", "content": base_prompt}]}

    for node_count in range(1, TOTAL_NODES + 1):
        print(colored(f"\n🌳 PARALLEL TREE SEARCH - NODE {node_count}/{TOTAL_NODES} (Cycle {cycle_number})", "blue"))
        print(colored(f"🌿 Processing {PARALLEL_BRANCHES} branches in parallel", "cyan"))

        # Select multiple nodes to expand in parallel
        selected_branches = select_multiple_nodes(root, PARALLEL_BRANCHES)

        # Create tasks for parallel branch processing
        branch_tasks = []
        for branch_id, (selected_node, path) in enumerate(selected_branches, 1):
            task = process_single_branch(
                branch_id, selected_node, path, conversation_histories, accuracy_history,
                cycle_number, failure_examples, global_node_id_counter, base_prompt, best_accuracy, best_node, node_count
            )
            branch_tasks.append(task)

        # Execute all branches in parallel
        print(colored(f"🚀 Executing {len(branch_tasks)} branches concurrently", "green"))
        branch_results = await asyncio.gather(*branch_tasks)

        # Process results from all branches
        all_children_data = []
        for branch_result in branch_results:
            branch_id = branch_result['branch_id']

            # Collect all children data from this branch (accuracies will be added when processing children)
            all_children_data.extend(branch_result['children_data'])

        # Process all children from parallel branches
        for child_data in all_children_data:
            # Find the correct parent node for this child based on branch_id
            selected_node = None
            child_path = None
            for branch_result in branch_results:
                if branch_result['branch_id'] == child_data['branch_id']:
                    selected_node = branch_result['selected_node']
                    child_path = branch_result['path']
                    break

            if not selected_node:
                continue

            # Create tree node
            child_node = TreeNode(
                code=child_data['code'],
                parent=selected_node,
                prompt=child_data['prompt']
            )

            if child_data['eval_results']:
                child_node.accuracy = child_data['accuracy']
                child_node.mistakes = child_data['eval_results']['mistakes']
                child_node.eval_results = child_data['eval_results']

                # Update best accuracy
                if child_node.accuracy > best_accuracy:
                    best_accuracy = child_node.accuracy
                    best_node = child_node
                    print(colored(f"🏆 New best: {best_accuracy:.2f}%", "green"))

                # Add accuracy to history (like original TS)
                accuracy_history.append(child_node.accuracy)

                # Save predictor
                save_predictor_with_accuracy(
                    predictor_code=child_node.code,
                    accuracy=child_node.accuracy,
                    node_id=child_data['node_id'],
                    total_predictions=child_node.eval_results['total_rows'],
                    correct_predictions=child_node.eval_results['correct_predictions']
                )

                # Add to conversation histories (thread-safe)
                child_conversation_history = child_data['conversation_history'] + [
                    {"role": "assistant", "content": f"```python\n{child_node.code}\n```"}
                ]
                with global_node_id_counter['lock']:
                    conversation_histories[child_node] = child_conversation_history

            # Add to tree (thread-safe)
            with selected_node.lock:
                selected_node.children.append(child_node)

            # Backpropagate using the correct path for this child
            if child_path:
                backpropagate(child_path + [child_node], child_node.accuracy if child_node.accuracy else 0)

            # Clean up variation files
            if child_data['type'] == 'variation':
                try:
                    os.remove(child_data['output_file'])
                except:
                    pass

        # Show error summary for the best child from any branch
        best_child_data = None
        max_accuracy = 0
        for child_data in all_children_data:
            if child_data.get('accuracy', 0) > max_accuracy:
                max_accuracy = child_data['accuracy']
                best_child_data = child_data

        if best_child_data and best_child_data['eval_results']:
            num_execution_errors = best_child_data['eval_results'].get('num_execution_errors', 0)
            num_prediction_errors = best_child_data['eval_results'].get('num_prediction_errors', 0)

            if num_execution_errors > 0:
                print(colored(f"🚨 EXECUTION ERRORS: {num_execution_errors} crashes detected", "red"))
            if num_prediction_errors > 0:
                print(colored(f"📊 PREDICTION ERRORS: {num_prediction_errors} incorrect predictions", "yellow"))

        # Update plot
        plot_accuracy_progress(accuracy_history, node_count, cycle_boundaries)

        # Visualize tree periodically for debugging
        if TREE_VISUALIZATION_FREQUENCY > 0 and (node_count % TREE_VISUALIZATION_FREQUENCY == 0 or node_count <= 5):
            print("\n" + "="*80)
            tree_viz = visualize_tree(root, max_depth=4)
            print(tree_viz)
            print("="*80 + "\n")

            # Generate HTML visualization (single file that gets updated)
            if HTML_VISUALIZATION_FREQUENCY > 0 and node_count % HTML_VISUALIZATION_FREQUENCY == 0:
                generate_html_tree_visualization(root, node_count, cycle_number, PARALLEL_BRANCHES, "tree_visualization.html")

        # Check if target accuracy reached (any child)
        max_child_accuracy = max((c.get('accuracy', 0) for c in all_children_data), default=0)
        if max_child_accuracy >= 95.0:
            print(colored(f"🎯 Target accuracy reached: {max_child_accuracy:.2f}% in Node {node_count}", "green"))
            return

        # Periodic reflection
        if REFLECTION_FREQUENCY > 0 and node_count % REFLECTION_FREQUENCY == 0 and node_count > 0:
            print(colored(f"\n🧠 PERIODIC REFLECTION - NODE {node_count}", "magenta"))
            print(colored("=" * 60, "magenta"))

            # Create reflection prompt
            reflection_prompt = f"""
CYCLE {cycle_number} PROGRESS REFLECTION (Node {node_count})

Current Progress:
- Best accuracy: {best_accuracy:.2f}%
- Total nodes explored: {node_count}
- Parallel branches: {PARALLEL_BRANCHES}

Strategic Analysis:
1. What patterns are emerging in successful predictors?
2. Are there specific mathematical approaches that consistently perform better?
3. What types of failures are most common?
4. What new strategies should be prioritized?

Provide strategic insights for the remaining parallel tree search.
"""

            # Get best function context
            best_context = ""
            if best_node and best_node.code:
                best_context = f"""
Current Best Function (Accuracy: {best_accuracy:.2f}%):
```python
{best_node.code}
```"""

            full_reflection_prompt = reflection_prompt + best_context

            # Make reflection API call
            print(colored("🤔 Requesting periodic reflection from model...", "magenta"))
            reflection_response = await make_api_call_with_retry(MODEL_NAME, [{"role": "user", "content": full_reflection_prompt}])

            if reflection_response:
                reflection_text = reflection_response.choices[0].message.content.strip()

                # Save reflection
                reflection_filename = f"{PREDICTORS_FOLDER}/reflection_node_{node_count}.txt"
                if not os.path.exists(PREDICTORS_FOLDER):
                    os.makedirs(PREDICTORS_FOLDER)

                with open(reflection_filename, "w", encoding="utf-8") as f:
                    f.write(f"NODE {node_count} REFLECTION\n")
                    f.write(f"Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f"Best Accuracy: {best_accuracy:.2f}%\n")
                    f.write(f"Total Nodes: {node_count}\n")
                    f.write(f"Parallel Branches: {PARALLEL_BRANCHES}\n\n")
                    f.write("=" * 80 + "\n\n")
                    f.write(reflection_text)

                print(colored(f"📝 Periodic reflection saved to {reflection_filename}", "magenta"))

                # Add to reflection history
                reflection_history.append({
                    'node': node_count,
                    'content': reflection_text,
                    'filename': reflection_filename,
                    'timestamp': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
                })

                # Keep only recent reflections
                if len(reflection_history) > REFLECTIONS_TO_KEEP:
                    reflection_history = reflection_history[-REFLECTIONS_TO_KEEP:]

    print(colored("✨ Parallel tree search complete!", "blue"))
    print(colored(f"🏆 Best accuracy achieved: {best_accuracy:.2f}%", "green"))
    print(colored(f"🌿 Used {PARALLEL_BRANCHES} parallel branches per iteration", "cyan"))

    # Final tree visualization
    if TREE_VISUALIZATION_FREQUENCY > 0:
        print("\n" + "="*100)
        print("🎯 FINAL TREE VISUALIZATION")
        final_tree_viz = visualize_tree(root, max_depth=6)  # Show more depth for final view
        print(final_tree_viz)
        print("="*100 + "\n")

        # Generate final HTML visualization (single file that gets updated)
        if HTML_VISUALIZATION_FREQUENCY > 0:
            # Show the path to the best node if available
            show_current_path = None
            if best_node != root:
                # Build path from root to best node
                current = best_node
                path_to_best = []
                while current:
                    path_to_best.insert(0, current)
                    current = current.parent
                show_current_path = path_to_best
            generate_html_tree_visualization(root, node_count, cycle_number, PARALLEL_BRANCHES, "tree_visualization.html", show_current_path)

if __name__ == "__main__":
    print(colored("🚀 Starting predictor generation with Parallel Tree Search...", "blue"))
    print(colored(f"🌿 Using {PARALLEL_BRANCHES} parallel branches per iteration", "cyan"))
    asyncio.run(generate_predictor())
    print(colored("✨ Process complete!", "blue"))

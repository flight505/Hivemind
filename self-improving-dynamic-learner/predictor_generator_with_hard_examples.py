import pandas as pd
import json
import random
import os
import time
import ast
import importlib.util
import matplotlib.pyplot as plt
from termcolor import colored
from API_client import make_API_call
from predictor_evaluator import evaluate_predictor
import asyncio

# IMPORTANT VARIABLES
PROVIDER = "OPENROUTER" # CAN BE ONE OF: OPENROUTER OR OPENAI
CSV_FILE = "complex_dataset.csv"
SAMPLE_SIZE = 10
MODEL_NAME = "openrouter/sonoma-sky-alpha"
OUTPUT_FILE = "generated_predictor.py"
ITERATIONS_PER_CYCLE = 10  # Number of iterations per cycle
MISTAKES_TO_SHOW = 10  # Number of mistakes to show per iteration
PREDICTORS_FOLDER = "predictors-SKY-hard-examples"  # Folder to save enumerated predictor files
TOP_PERFORMERS_TO_KEEP = 3  # Number of top performers to preserve between cycles
EXAMPLES_PER_PERFORMER = 10  # Number of failure examples to show per top performer
REFLECTIONS_TO_KEEP = 3  # Number of latest reflections to keep for future cycles
PLOT_FILENAME = "accuracy_progress-SKY-hard-examples.png"

# Hard Examples Configuration
HARD_EXAMPLES_JSON = "unsolved_rows.json"  # File containing unsolved row indices
MAX_HARD_EXAMPLES_TO_SHOW = 5  # Maximum hard examples to include in prompts

# API Configuration
MAX_API_RETRIES = 10  # Maximum retries for API calls
API_RETRY_DELAY = 2  # Base delay between retries (seconds)
RATE_LIMIT_DELAY = 0.1  # Delay between API calls to avoid rate limiting

def load_hard_examples():
    """Load hard examples from JSON file."""
    if not os.path.exists(HARD_EXAMPLES_JSON):
        print(colored(f"⚠️  Hard examples file {HARD_EXAMPLES_JSON} not found. Starting with empty hard examples.", "yellow"))
        return []

    try:
        with open(HARD_EXAMPLES_JSON, 'r') as f:
            data = json.load(f)
        hard_indices = data.get('unsolved_row_indices', [])
        print(colored(f"✅ Loaded {len(hard_indices)} hard examples from {HARD_EXAMPLES_JSON}", "green"))
        return hard_indices
    except Exception as e:
        print(colored(f"❌ Error loading hard examples: {e}", "red"))
        return []

def save_hard_examples(hard_indices):
    """Save current hard examples to JSON file."""
    data = {
        "total_unsolved_rows": len(hard_indices),
        "unsolved_row_indices": hard_indices,
        "last_updated": pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    with open(HARD_EXAMPLES_JSON, 'w') as f:
        json.dump(data, f, indent=4)

    print(colored(f"💾 Saved {len(hard_indices)} hard examples to {HARD_EXAMPLES_JSON}", "cyan"))

def get_hard_examples_text(hard_indices, df):
    """Generate text description of hard examples for inclusion in prompts."""
    if not hard_indices:
        return ""

    # Select random subset of hard examples to avoid token limits
    selected_indices = random.sample(hard_indices, min(MAX_HARD_EXAMPLES_TO_SHOW, len(hard_indices)))

    examples_text = "\n\n🎯 HARD EXAMPLES TO SOLVE:\n"
    examples_text += "These specific cases have been consistently unsolved by all previous predictors.\n"
    examples_text += "Your function MUST correctly handle these examples:\n\n"

    for i, idx in enumerate(selected_indices, 1):
        if idx < len(df):
            row = df.iloc[idx]
            examples_text += f"❌ Hard Case #{i}: Input(A={row['A']}, B={row['B']}, C={row['C']}, D={row['D']}, E={row['E']}) must return Output={row['Output']}\n"

    examples_text += "\n🔥 CRITICAL: Solve these hard cases while maintaining overall accuracy!"
    return examples_text

def check_solved_hard_examples(hard_indices, eval_results, df):
    """Check which hard examples were solved by the current predictor and remove them."""
    if not hard_indices or not eval_results:
        return hard_indices

    solved_indices = []

    # Get the correct predictions from eval_results
    correct_predictions = eval_results.get('correct_predictions_detail', [])

    for idx in hard_indices:
        if idx < len(df):
            # Check if this hard example was predicted correctly
            actual_output = df.iloc[idx]['Output']
            # We need to find if this row was in the correct predictions
            # Since we don't have detailed prediction results, we'll need to re-evaluate the specific hard examples
            try:
                # Import the current predictor function
                spec = importlib.util.spec_from_file_location("temp_predictor", OUTPUT_FILE)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                row = df.iloc[idx]
                predicted = module.predict_output(row['A'], row['B'], row['C'], row['D'], row['E'])

                if predicted == actual_output:
                    solved_indices.append(idx)
                    print(colored(f"🎉 Hard example Row {idx} SOLVED! (Predicted: {predicted}, Actual: {actual_output})", "green"))
            except Exception as e:
                # If there's an error, consider it unsolved
                pass

    # Remove solved examples from hard set
    remaining_hard_indices = [idx for idx in hard_indices if idx not in solved_indices]

    if solved_indices:
        print(colored(f"✅ Removed {len(solved_indices)} solved hard examples. {len(remaining_hard_indices)} remain.", "green"))
        # Save updated hard examples
        save_hard_examples(remaining_hard_indices)

    return remaining_hard_indices

def plot_accuracy_progress(accuracy_history, iteration, cycle_boundaries=None):
    """Create and save a line plot of accuracy progression with cycle boundaries."""
    plt.figure(figsize=(14, 8))

    # Create x-axis values (iterations)
    iterations = list(range(1, len(accuracy_history) + 1))

    # Plot the accuracy line
    plt.plot(iterations, accuracy_history, 'b-o', linewidth=2, markersize=6, label='Accuracy')

    # Add current iteration marker with different color
    if iteration <= len(accuracy_history):
        plt.plot(iteration, accuracy_history[iteration-1], 'r*', markersize=12, label=f'Iteration {iteration}')

    # Add vertical lines for cycle boundaries
    if cycle_boundaries:
        for i, boundary in enumerate(cycle_boundaries):
            if boundary <= len(iterations):
                plt.axvline(x=boundary, color='red', linestyle='--', alpha=0.7, linewidth=2)
                plt.text(boundary + 0.5, max(accuracy_history) * 0.95,
                        f'Cycle {i + 2}',  # Cycle number (i+2 because cycle 1 has no boundaries)
                        rotation=90, verticalalignment='top', fontsize=10, color='red')

    # Customize the plot
    title_suffix = f" - Cycle {len(cycle_boundaries) + 1 if cycle_boundaries else 1}"
    plt.title(f'Predictor Accuracy Progression with Hard Examples{title_suffix}', fontsize=14, fontweight='bold')
    plt.xlabel('Iteration Number', fontsize=12)
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
                time.sleep(RATE_LIMIT_DELAY)

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
            time.sleep(delay)

    print(colored(f"💀 All {max_retries} API attempts failed", "red"))
    return None

def write_file_with_encoding(filepath, content, description=None):
    """Helper function to write files with consistent encoding."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    if description:
        log_message(f"{description} saved to {filepath}", "cyan")

def save_predictor_with_accuracy(predictor_code, accuracy, iteration, total_predictions=None, correct_predictions=None):
    """Save predictor function to enumerated file with accuracy information."""
    # Create predictors folder if it doesn't exist
    if not os.path.exists(PREDICTORS_FOLDER):
        os.makedirs(PREDICTORS_FOLDER)

    # Create filename with enumeration
    filename = f"{PREDICTORS_FOLDER}/predictor_{iteration}.py"

    # Create header comment with accuracy information
    header_comment = f'''"""
Predictor {iteration}
Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}
Accuracy: {accuracy:.2f}%
"""

'''

    # Add accuracy information as inline comment at the top of the function
    accuracy_comment = f'''
# PREDICTOR {iteration} - Accuracy: {accuracy:.2f}%
# Correct predictions: {correct_predictions}/{total_predictions} ({accuracy:.2f}%)
'''

    # Combine header, accuracy comment, and predictor code
    full_content = header_comment + accuracy_comment + "\n" + predictor_code

    # Save to file using helper function
    write_file_with_encoding(filename, full_content, f"💾 Predictor {iteration}")
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

def create_stagnation_feedback_prompt(stuck_accuracy, iteration, base_prompt):
    """Create a prompt that encourages creative variation when stuck at same accuracy."""
    return f"""{base_prompt}

🚨 STAGNATION DETECTED: You have achieved exactly {stuck_accuracy:.2f}% accuracy for 3 consecutive iterations.

Break this pattern with creative mathematical innovation. Try different approaches, combine features in new ways, and explore alternative logical structures. Be constructively creative while maintaining mathematical validity."""

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
        print(colored(f"  {i}. Accuracy: {performer['accuracy']:.2f}% (Iteration {performer['iteration']})", "green"))

    return top_performers

def collect_failure_examples(top_performers, all_cycle_results):
    """Collect failure examples from the top performers."""
    failure_examples = {}

    for performer in top_performers:
        iteration = performer['iteration']
        performer_key = f"iteration_{iteration}"

        # Find the results for this performer
        performer_result = next((r for r in all_cycle_results if r['iteration'] == iteration), None)

        if performer_result and 'mistakes' in performer_result:
            mistakes = performer_result['mistakes']
            # Select random examples of failures (limit to EXAMPLES_PER_PERFORMER)
            selected_mistakes = select_random_mistakes(mistakes, EXAMPLES_PER_PERFORMER)
            failure_examples[performer_key] = {
                'accuracy': performer['accuracy'],
                'function': performer['function'],
                'mistakes': selected_mistakes
            }
            print(colored(f"📝 Collected {len(selected_mistakes)} failure examples for Iteration {iteration}", "cyan"))

    return failure_examples

def create_improved_prompt(base_prompt, mistakes, iteration, eval_results=None, failure_examples=None, cycle_number=1, hard_examples_text=""):
    """Create an improved prompt that includes mistake history and top performers from previous cycles."""
    if not mistakes and not failure_examples and not hard_examples_text:
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
{f'8. CRITICAL: Fix all syntax errors - your generated code must be valid Python syntax' if has_syntax_errors else ''}
{f'9. CRITICAL: Fix all execution errors - your function must handle all input combinations without crashing' if has_execution_errors else ''}

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

📝 FINAL NOTE: If high accuracy samples exist so far, you can use parts of them for inspiration. Build incrementally upon proven approaches while adding creative innovations using basic mathematical operations. Never repeat code in its entirety - always modify and improve upon successful patterns. Combine the best elements from high-performing functions with new mathematical discoveries.{hard_examples_text}
"""

    return base_prompt + improvement_message

async def generate_predictor():
    print(colored("🔍 Reading dataset...", "cyan"))

    # Read CSV and get sample
    df = pd.read_csv(CSV_FILE)
    sample_df = df.head(SAMPLE_SIZE)

    print(colored(f"✅ Loaded {len(sample_df)} rows from dataset", "green"))

    # Load hard examples
    hard_indices = load_hard_examples()
    print(colored(f"🎯 Starting with {len(hard_indices)} hard examples to solve", "yellow"))

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
- The function should return the predicted category (1, 2, 3, or 4)
- Analyze the provided training data (including Output values) to learn patterns
- Use SIMPLE mathematical operations: arithmetic (+, -, *, /), comparisons (<, >, <=, >=), and basic logic
- Keep the function simple and readable - avoid complex formulas or domain-specific concepts
- Only return the Python function code, no explanations
- Do NOT use machine learning concepts, statistical methods, or domain-specific terminology
- Focus on basic mathematical relationships and conditional logic

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

    # Cycle-based variables
    cycle_number = 1
    global_iteration = 0
    accuracy_history = []  # Global accuracy history across all cycles
    cycle_boundaries = []  # Track where each cycle begins
    failure_examples = {}  # Cross-cycle learning data
    reflection_history = []  # Store all strategic reflections across cycles

    # Run indefinitely in cycles
    while True:
        print(colored(f"\n🚀 STARTING CYCLE {cycle_number}", "blue"))
        print(colored("=" * 60, "blue"))

        # Cycle-specific variables
        cycle_results = []  # Store results from this cycle
        conversation_history = []  # Fresh conversation history per cycle

        # Add previous reflections to conversation history for continuity
        if reflection_history:
            for reflection in reflection_history[-REFLECTIONS_TO_KEEP:]:  # Include latest reflections to avoid token limits
                conversation_history.append({"role": "user", "content": f"Previous Strategic Reflection (Cycle {reflection['cycle']}):\n{reflection['content']}"})

        best_accuracy_this_cycle = 0
        best_function_this_cycle = None
        best_eval_results_this_cycle = None

        # Mark cycle boundary
        if cycle_number > 1:
            cycle_boundaries.append(global_iteration + 1)

        # Run iterations within this cycle
        for cycle_iteration in range(1, ITERATIONS_PER_CYCLE + 1):
            global_iteration += 1

            print(colored(f"\n🔄 CYCLE {cycle_number} - ITERATION {cycle_iteration}/{ITERATIONS_PER_CYCLE} (Global: {global_iteration})", "blue"))
            print(colored(f"🎯 Hard examples remaining: {len(hard_indices)}", "yellow"))

            # Create prompt for this iteration
            if cycle_iteration == 1 and cycle_number == 1:
                # First iteration of first cycle - use base prompt
                current_prompt = base_prompt
                conversation_history.append({"role": "user", "content": current_prompt})
                messages = conversation_history.copy()
            else:
                # Use mistakes and cross-cycle learning
                current_mistakes = []

                # Get mistakes from previous iteration in this cycle
                if cycle_results and cycle_iteration > 1:
                    prev_result = cycle_results[-1]
                    if 'mistakes' in prev_result:
                        current_mistakes = prev_result['mistakes']

                # Create improved prompt with cross-cycle learning and hard examples
                if current_mistakes or failure_examples or hard_indices:
                    selected_mistakes = select_random_mistakes(current_mistakes) if current_mistakes else []
                    hard_examples_text = get_hard_examples_text(hard_indices, df)
                    current_prompt = create_improved_prompt(
                        base_prompt,
                        selected_mistakes,
                        global_iteration,
                        best_eval_results_this_cycle,
                        failure_examples if cycle_number > 1 else None,
                        cycle_number,
                        hard_examples_text
                    )
                else:
                    current_prompt = base_prompt + f"\n\nCycle {cycle_number}, Iteration {cycle_iteration}: Please improve the predictor function."

                # Check for stagnation pattern within this cycle
                cycle_accuracy_history = [r['accuracy'] for r in cycle_results]
                is_stagnant, stuck_accuracy = check_stagnation_pattern(cycle_accuracy_history)
                if is_stagnant and cycle_iteration > 3:
                    print(colored(f"🔄 STAGNATION DETECTED: {stuck_accuracy:.2f}% accuracy repeated 3 times", "yellow"))
                    current_prompt = create_stagnation_feedback_prompt(stuck_accuracy, global_iteration, current_prompt)

                # Add best function from this cycle if available
                if best_function_this_cycle is not None and best_eval_results_this_cycle is not None:
                    accuracy_info = f"""
PERFORMANCE SUMMARY (This Cycle):
- Overall Accuracy: {best_eval_results_this_cycle['overall_accuracy']:.2f}%
- Correct Predictions: {best_eval_results_this_cycle['correct_predictions']}/{best_eval_results_this_cycle['total_rows']}
- Execution Errors: {best_eval_results_this_cycle.get('num_execution_errors', 0)}
- Prediction Errors: {best_eval_results_this_cycle.get('num_prediction_errors', 0)}

Function code:
```python
{best_function_this_cycle}
```"""
                    conversation_history.append({"role": "assistant", "content": accuracy_info})

                # Add new improvement request
                improvement_message = f"Cycle {cycle_number}, Iteration {cycle_iteration}: Improve this predictor function using the provided feedback and cross-cycle learning.\n\n{current_prompt}"
                conversation_history.append({"role": "user", "content": improvement_message})

                messages = conversation_history.copy()

            # Save the current prompt
            write_file_with_encoding("prompt.txt", current_prompt)

            print(colored(f"🤖 Sending request to {MODEL_NAME} (Cycle {cycle_number}, Iteration {cycle_iteration})...", "yellow"))

            response = await make_api_call_with_retry(MODEL_NAME, messages)

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
                    print(colored("❌ Invalid response: Missing predict_output function", "red"))
                    continue

                print(colored("✅ Received valid function from model", "green"))

                # Validate syntax
                syntax_errors = validate_python_syntax(generated_function)
                if syntax_errors:
                    print(colored(f"🚨 SYNTAX ERRORS DETECTED: {len(syntax_errors)} issues found", "red"))
                    for error in syntax_errors:
                        print(colored(f"  • {error}", "red"))

                    # Store syntax error for next iteration
                    syntax_mistake = {
                        'error': f"Syntax Error: {'; '.join(syntax_errors)}",
                        'input': {},
                        'predicted': None,
                        'actual': None
                    }

                    # Store this as a failed result
                    cycle_results.append({
                        'iteration': global_iteration,
                        'accuracy': 0,
                        'function': generated_function,
                        'mistakes': [syntax_mistake],
                        'eval_results': None
                    })

                    conversation_history.append({"role": "assistant", "content": f"```python\n{generated_function}\n```"})
                    continue

                # Save and evaluate the function
                write_file_with_encoding(OUTPUT_FILE, generated_function, f"Function saved to {OUTPUT_FILE}")
                conversation_history.append({"role": "assistant", "content": f"```python\n{generated_function}\n```"})

                print(colored(f"\n📊 Evaluating predictor accuracy (Cycle {cycle_number}, Iteration {cycle_iteration})...", "yellow"))
                eval_results = await evaluate_predictor(CSV_FILE, OUTPUT_FILE)

                if eval_results:
                    current_accuracy = eval_results['overall_accuracy']

                    # Check and update hard examples
                    hard_indices = check_solved_hard_examples(hard_indices, eval_results, df)

                    # Store results for this cycle
                    cycle_results.append({
                        'iteration': global_iteration,
                        'accuracy': current_accuracy,
                        'function': generated_function,
                        'mistakes': eval_results['mistakes'],
                        'eval_results': eval_results
                    })

                    # Update global accuracy history
                    accuracy_history.append(current_accuracy)

                    # Update cycle best
                    if current_accuracy > best_accuracy_this_cycle:
                        best_accuracy_this_cycle = current_accuracy
                        best_function_this_cycle = generated_function
                        best_eval_results_this_cycle = eval_results
                        print(colored(f"🏆 New best in cycle {cycle_number}: {best_accuracy_this_cycle:.2f}%", "green"))

                    # Show error summary
                    num_execution_errors = eval_results.get('num_execution_errors', 0)
                    num_prediction_errors = eval_results.get('num_prediction_errors', 0)

                    if num_execution_errors > 0:
                        print(colored(f"🚨 EXECUTION ERRORS: {num_execution_errors} crashes detected", "red"))
                    if num_prediction_errors > 0:
                        print(colored(f"📊 PREDICTION ERRORS: {num_prediction_errors} incorrect predictions", "yellow"))

                    # Update plot with cycle boundaries
                    plot_accuracy_progress(accuracy_history, global_iteration, cycle_boundaries)

                    # Save predictor with accuracy
                    saved_filename = save_predictor_with_accuracy(
                        predictor_code=generated_function,
                        accuracy=current_accuracy,
                        iteration=global_iteration,
                        total_predictions=eval_results['total_rows'],
                        correct_predictions=eval_results['correct_predictions']
                    )

                    # Check if target accuracy reached
                    if current_accuracy >= 95.0:
                        print(colored(f"🎯 Target accuracy reached: {current_accuracy:.2f}% in Cycle {cycle_number}", "green"))
                        return  # Exit the infinite loop

                else:
                    print(colored("❌ Evaluation failed", "red"))
                    cycle_results.append({
                        'iteration': global_iteration,
                        'accuracy': 0,
                        'function': "Failed to generate",
                        'mistakes': [],
                        'eval_results': None
                    })
            else:
                print(colored(f"❌ Failed to get response from model (Cycle {cycle_number}, Iteration {cycle_iteration})", "red"))
                cycle_results.append({
                    'iteration': global_iteration,
                    'accuracy': 0,
                    'function': "Failed to generate",
                    'mistakes': [],
                    'eval_results': None
                })

        # Cycle completed - extract top performers and prepare for next cycle
        print(colored(f"\n🏁 CYCLE {cycle_number} COMPLETED", "green"))
        print(colored("=" * 60, "green"))

        # Extract top performers from this cycle
        top_performers = extract_top_performers(cycle_results)

        # Collect failure examples from top performers
        if top_performers:
            cycle_failure_examples = collect_failure_examples(top_performers, cycle_results)

            # Merge with existing cross-cycle failure examples and keep only top 3 overall
            # First, add all existing performers to a combined list
            all_performers = []

            # Add existing performers
            for performer_key, data in failure_examples.items():
                all_performers.append({
                    'key': performer_key,
                    'accuracy': data['accuracy'],
                    'data': data
                })

            # Add new performers from this cycle
            for performer_key, data in cycle_failure_examples.items():
                all_performers.append({
                    'key': performer_key,
                    'accuracy': data['accuracy'],
                    'data': data
                })

            # Sort by accuracy (descending) and keep only top performers
            all_performers.sort(key=lambda x: x['accuracy'], reverse=True)
            top_performers_overall = all_performers[:TOP_PERFORMERS_TO_KEEP]

            # Update failure_examples with only the top performers
            failure_examples.clear()
            for performer in top_performers_overall:
                failure_examples[performer['key']] = performer['data']

            print(colored(f"🏆 Retained top {TOP_PERFORMERS_TO_KEEP} performers across all cycles: {[f'{p['accuracy']:.1f}%' for p in top_performers_overall]}", "green"))

        # Cycle summary
        cycle_accuracies = [r['accuracy'] for r in cycle_results if r['accuracy'] > 0]
        if cycle_accuracies:
            avg_accuracy = sum(cycle_accuracies) / len(cycle_accuracies)
            max_accuracy = max(cycle_accuracies)
            print(colored(f"📊 Cycle {cycle_number} Summary:", "cyan"))
            print(colored(f"  • Average Accuracy: {avg_accuracy:.2f}%", "cyan"))
            print(colored(f"  • Best Accuracy: {max_accuracy:.2f}%", "cyan"))
            print(colored(f"  • Total Iterations: {len(cycle_results)}", "cyan"))
            print(colored(f"  • Cross-cycle examples preserved: {len(failure_examples)}", "cyan"))
            print(colored(f"  • Hard examples remaining: {len(hard_indices)}", "yellow"))

        # REFLECTION ITERATION: Strategic thinking for next cycle
        global_iteration += 1
        print(colored(f"\n🧠 CYCLE {cycle_number} REFLECTION - ITERATION {global_iteration}", "magenta"))
        print(colored("=" * 60, "magenta"))

        # Create reflection prompt
        reflection_prompt = f"""
CYCLE {cycle_number} REFLECTION AND STRATEGIC PLANNING

You have completed Cycle {cycle_number} of predictor function optimization. Here's what you accomplished:

📊 CYCLE PERFORMANCE SUMMARY:
- Best accuracy achieved: {max_accuracy:.2f}%
- Average accuracy: {avg_accuracy:.2f}%
- Total iterations: {len(cycle_results)}
- Cross-cycle learning examples preserved: {len(failure_examples)}
- Hard examples remaining: {len(hard_indices)}

🎯 REFLECTION REQUEST:
Please provide a strategic reflection on what you have learned and outline creative new approaches to explore in the next cycle.

Consider these aspects:
1. **Patterns Observed**: What mathematical relationships or prediction strategies showed the most promise?
2. **Failure Analysis**: What types of inputs or patterns continue to be challenging?
3. **Innovation Opportunities**: What creative mathematical approaches haven't been fully explored yet?
4. **Strategic Direction**: What specific new avenues should be prioritized in the next cycle?

🎨 CREATIVE PLANNING:
Outline 3-5 specific creative strategies or mathematical innovations you want to explore in the next cycle. Be specific about:
- New mathematical operations or combinations to try
- Different logical structures or conditional approaches
- Alternative ways to handle challenging input patterns
- Novel feature interactions or transformations

Provide your reflection and strategic plan as regular text (not code). This will help guide the optimization process going forward.

STRATEGIC REFLECTION:
"""

        # Get best function from this cycle for context
        best_function_context = ""
        if cycle_results:
            best_result = max(cycle_results, key=lambda x: x['accuracy'])
            if best_result['accuracy'] > 0:
                best_function_context = f"""

BEST FUNCTION FROM THIS CYCLE (Accuracy: {best_result['accuracy']:.2f}%):
```python
{best_result['function']}
```"""

        full_reflection_prompt = reflection_prompt + best_function_context

        # Make API call for reflection
        print(colored("🤔 Requesting strategic reflection from model...", "magenta"))
        reflection_response = await make_api_call_with_retry(MODEL_NAME, [{"role": "user", "content": full_reflection_prompt}])

        if reflection_response:
            reflection_text = reflection_response.choices[0].message.content.strip()

            # Save reflection to file
            reflection_filename = f"{PREDICTORS_FOLDER}/reflection_cycle_{cycle_number}.txt"
            if not os.path.exists(PREDICTORS_FOLDER):
                os.makedirs(PREDICTORS_FOLDER)

            with open(reflection_filename, "w", encoding="utf-8") as f:
                f.write(f"CYCLE {cycle_number} STRATEGIC REFLECTION\n")
                f.write(f"Generated on: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Cycle Performance: Best {max_accuracy:.2f}%, Average {avg_accuracy:.2f}%\n")
                f.write(f"Hard Examples Remaining: {len(hard_indices)}\n\n")
                f.write("=" * 80 + "\n\n")
                f.write(reflection_text)

            print(colored(f"📝 Strategic reflection saved to {reflection_filename}", "magenta"))

            # Store reflection as part of cycle results
            cycle_results.append({
                'iteration': global_iteration,
                'accuracy': 0,  # Reflections don't have accuracy
                'function': "STRATEGIC_REFLECTION",
                'mistakes': [],
                'eval_results': None,
                'reflection_file': reflection_filename,
                'reflection_content': reflection_text
            })

            # Add reflection to reflection_history for cross-cycle continuity
            reflection_history.append({
                'cycle': cycle_number,
                'content': reflection_text,
                'filename': reflection_filename,
                'timestamp': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
            })
        else:
            print(colored("❌ Failed to get strategic reflection from model", "red"))

        # Prepare for next cycle
        cycle_number += 1
        print(colored(f"🔄 Preparing for Cycle {cycle_number} with {len(failure_examples)} cross-cycle learning examples and {len(hard_indices)} hard examples...", "yellow"))

if __name__ == "__main__":
    print(colored("🚀 Starting predictor generation process with hard examples...", "blue"))
    asyncio.run(generate_predictor())
    print(colored("✨ Process complete!", "blue"))

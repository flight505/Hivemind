"""
Parallel Tree Search Solution Generator

Uses Monte Carlo Tree Search with PUCT scoring to generate and iteratively improve
AI-powered solutions to complex goals through parallel exploration and 2-STAGE HARSH evaluation.

Features:
- Parallel branch processing with concurrent solution generation
- 2-STAGE EVALUATION: Only 2 API calls total for all rubrics (Stage 1 + Stage 2)
- Stage 1: 7 rubrics in 1 call (70pts total), Stage 2: multiple rubrics in 1 call (30pts total)
- Only solutions passing Stage 1 proceed to Stage 2 and get saved
- EXTREMELY STRICT LLM-based quality evaluation using demanding rubrics (0-100 scale)
- Stagnation detection and creative variation prompts
- Hybridization of top-performing solutions
- Cross-cycle learning and periodic strategic reflection

Configuration: Set GOAL and parameters as ALL_CAPS constants at module level.
Usage: python goal_solver_parallel_ts.py
Output: Solutions saved to solutions/ folder as solution_N_SCORE.txt with HARSH quality scores; reflections in solutions/reflections/; rubrics in solutions/rubrics/.

Dependencies: termcolor, API_client, asyncio, threading, matplotlib, numpy
"""

import asyncio
import random
import time
import os
import re
import threading
from termcolor import colored
from API_client import make_API_call
import math
import matplotlib.pyplot as plt
import numpy as np

# IMPORTANT USER INPUT
GOAL = "most effective exercise regimen that can be done at home and in 5 minutes"

# API Configuration
PROVIDER = "OPENROUTER"
MODEL_NAME = "openrouter/sonoma-sky-alpha"
MAX_API_RETRIES = 10
API_RETRY_DELAY = 2
RATE_LIMIT_DELAY = 0.1

# two stage evaluation
STAGE_1_SETTINGS = {
    "TOTAL_POINTS": 70,
    "CHUNKS": 7,
    "MINIMUM_SCORE_TO_PASS_STAGE_1": 55
}
STAGE_2_INCREMENTS = 1 # IN HOW MANY INCREMENTS THE REMAINING POINTS ARE ALLOCATED

# Tree Search Configuration
TOTAL_NODES = 100
PARALLEL_BRANCHES = 5
TREE_CHILDREN_PER_EXPANSION = 4
C_PUCT = 1.0
HYBRIDIZATION_FREQUENCY = 20
STAGNATION_CHECK_FREQUENCY = 10
REFLECTION_FREQUENCY = 2

# Solution Configuration
TOP_PERFORMERS_TO_KEEP = 3
EXAMPLES_PER_PERFORMER = 5
REFLECTIONS_TO_KEEP = 3
SOLUTIONS_FOLDER = "solutions_exercise_2" # change this folder name for different goals
REFLECTIONS_FOLDER = f"{SOLUTIONS_FOLDER}/reflections"
RUBRICS_FOLDER = f"{SOLUTIONS_FOLDER}/rubrics"

# Score Thresholds Configuration
TARGET_QUALITY_THRESHOLD = 90.0  # Stop when solution reaches this quality score
MINIMUM_QUALITY_THRESHOLD = 0.0  # Minimum quality score to consider a solution evaluated
MAXIMUM_QUALITY_SCORE = 100.0    # Maximum possible quality score

# Plotting Configuration
PLOT_FILE = f"{SOLUTIONS_FOLDER}/progress_plot.png"  # Real-time progress plot file
ENABLE_PLOTTING = True  # Set to False to disable plotting

# Global locks
state_lock = threading.RLock()  # Dedicated lock for conversation histories state

def plot_progress(quality_scores, evaluation_numbers, best_qualities, current_evaluation):
    """Create and save real-time progress plot showing quality scores over time."""
    if not ENABLE_PLOTTING or not quality_scores:
        return

    plt.figure(figsize=(12, 8))

    # Create subplots
    plt.subplot(2, 2, 1)
    # Quality scores over time - regular line chart
    plt.plot(evaluation_numbers, quality_scores, color='blue', linewidth=2, marker='o', markersize=4, alpha=0.8)
    plt.title('Quality Scores Over Time')
    plt.xlabel('Evaluation Number')
    plt.ylabel('Quality Score (0-100)')
    plt.ylim(0, 105)
    plt.grid(True, alpha=0.3)

    # Moving average
    if len(quality_scores) >= 5:
        window_size = min(10, len(quality_scores))
        moving_avg = np.convolve(quality_scores, np.ones(window_size)/window_size, mode='valid')
        plt.plot(evaluation_numbers[window_size-1:], moving_avg, color='red', linewidth=3, label=f'Moving Avg ({window_size})')
        plt.legend()

    plt.subplot(2, 2, 2)
    # Best quality progression
    plt.plot(evaluation_numbers, best_qualities, color='green', linewidth=3, marker='s', markersize=5)
    plt.title('Best Quality Found So Far')
    plt.xlabel('Evaluation Number')
    plt.ylabel('Best Quality Score')
    plt.ylim(0, 105)
    plt.grid(True, alpha=0.3)

    plt.subplot(2, 2, 3)
    # Quality distribution histogram
    if len(quality_scores) > 1:
        plt.hist(quality_scores, bins=min(20, len(set(quality_scores))), alpha=0.7, color='purple', edgecolor='black')
        plt.title('Quality Score Distribution')
        plt.xlabel('Quality Score')
        plt.ylabel('Frequency')
        plt.grid(True, alpha=0.3)

    plt.subplot(2, 2, 4)
    # Progress metrics
    plt.text(0.1, 0.8, f'Current Evaluation: {current_evaluation}', fontsize=12, fontweight='bold')
    plt.text(0.1, 0.7, f'Total Solutions: {len(quality_scores)}', fontsize=11)
    plt.text(0.1, 0.6, f'Best Score: {max(best_qualities):.1f}', fontsize=11)
    plt.text(0.1, 0.5, f'Average Score: {np.mean(quality_scores):.1f}', fontsize=11)
    plt.text(0.1, 0.4, f'Latest Score: {quality_scores[-1]:.1f}', fontsize=11)
    plt.title('Progress Summary')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.axis('off')

    plt.suptitle(f'Goal Solver Progress - Evaluation {current_evaluation}\n{GOAL[:80]}...', fontsize=14, fontweight='bold')
    plt.tight_layout()

    # Ensure solutions directory exists
    if not os.path.exists(SOLUTIONS_FOLDER):
        os.makedirs(SOLUTIONS_FOLDER)

    # Save plot
    plt.savefig(PLOT_FILE, dpi=150, bbox_inches='tight')
    plt.close()

    log_message(f"📊 Progress plot updated: {PLOT_FILE}", "cyan")

class TreeNode:
    """Node in the tree search structure with thread-safe operations for general goal solving."""
    def __init__(self, solution="", parent=None, prompt="", lock=None):
        self.solution = solution
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0.0
        self.quality_score = 0.0  # 0-100 scale from LLM evaluation
        self.feedback = ""
        self.prompt = prompt
        self.eval_results = None
        self.lock = lock or threading.RLock()

def log_message(message, color="white"):
    """Helper function for consistent colored logging."""
    print(colored(message, color))

def check_stagnation_pattern(quality_history):
    """Check if the same quality score has been achieved 3 times in a row."""
    if len(quality_history) < 3:
        return False, None

    last_three = quality_history[-3:]
    if len(set(last_three)) == 1 and last_three[0] > MINIMUM_QUALITY_THRESHOLD:
        return True, last_three[0]

    return False, None

def create_stagnation_feedback_prompt(stuck_score, node_id, base_prompt):
    """Create a prompt that encourages creative variation when stuck at same quality."""
    return f"""{base_prompt}

🚨 STAGNATION DETECTED: You have achieved exactly {stuck_score:.1f} quality score for 3 consecutive nodes.

Break this pattern with creative innovation. Try different approaches, combine strategies in new ways, and explore alternative solution structures. Be constructively creative while maintaining goal relevance.

REMINDER: Your solution MUST effectively address: {GOAL}"""

async def make_api_call_with_retry(model_name, messages, max_retries=MAX_API_RETRIES):
    """Make API call with retry logic and exponential backoff."""
    for attempt in range(max_retries):
        try:
            log_message(f"🤖 API Call Attempt {attempt + 1}/{max_retries}", "blue")

            if attempt > 0:
                await asyncio.sleep(RATE_LIMIT_DELAY)

            response = await make_API_call(model_name, messages, PROVIDER)
            if response:
                return response
            else:
                log_message(f"❌ API call failed (attempt {attempt + 1})", "red")

        except Exception as e:
            log_message(f"⚠️  API exception (attempt {attempt + 1}): {e}", "yellow")

        if attempt < max_retries - 1:
            delay = API_RETRY_DELAY * (2 ** attempt)
            log_message(f"⏳ Waiting {delay}s before retry...", "cyan")
            await asyncio.sleep(delay)

    log_message(f"💀 All {max_retries} API attempts failed", "red")
    return None

async def generate_stage1_rubrics(goal):
    """Generate all 7 stage 1 rubrics in a single API call."""
    rubric_prompt = f"""
Generate {STAGE_1_SETTINGS["CHUNKS"]} STRICT evaluation rubrics for assessing solutions to this goal. Create ALL {STAGE_1_SETTINGS["CHUNKS"]} rubrics in your response.

GOAL: {goal}

Create {STAGE_1_SETTINGS["CHUNKS"]} DEMANDING evaluation rubrics that each focus on DIFFERENT SPECIFIC ASPECTS of evaluation. Each rubric allocates exactly {STAGE_1_SETTINGS["TOTAL_POINTS"] // STAGE_1_SETTINGS["CHUNKS"]} points.

REQUIREMENTS FOR EACH RUBRIC:
- Focus on ONE specific evaluation dimension/aspect
- HIGH STANDARDS with specific criteria
- CRITICAL scoring (0-{STAGE_1_SETTINGS["TOTAL_POINTS"] // STAGE_1_SETTINGS["CHUNKS"]} points)
- EXAMPLES showing what constitutes poor solutions
- CHALLENGING requirements that only excellent solutions fully meet
- SEVERE penalties for any significant issues

IMPORTANT: Each rubric should be STRICT - most solutions should score below {STAGE_1_SETTINGS["TOTAL_POINTS"] // STAGE_1_SETTINGS["CHUNKS"] // 2} points. Be critical but fair.

FORMAT: Provide {STAGE_1_SETTINGS["CHUNKS"]} complete, structured rubrics clearly separated.

RUBRIC 1:
[Complete rubric here]

RUBRIC 2:
[Complete rubric here]

[... continue for all {STAGE_1_SETTINGS["CHUNKS"]} rubrics]
"""

    messages = [{"role": "user", "content": rubric_prompt}]
    response = await make_api_call_with_retry(MODEL_NAME, messages)

    if response:
        full_response = response.choices[0].message.content.strip()
        log_message(f"📋 Stage 1 rubrics generated in single API call", "blue")

        # Parse the response to extract individual rubrics
        rubrics = []

        for i in range(1, STAGE_1_SETTINGS["CHUNKS"] + 1):
            # Look for RUBRIC i: pattern
            rubric_marker = f"RUBRIC {i}:"
            if rubric_marker in full_response:
                # Extract from "RUBRIC i:" to next "RUBRIC" or end
                start_idx = full_response.find(rubric_marker) + len(rubric_marker)
                end_idx = full_response.find(f"RUBRIC {i+1}:", start_idx) if i < STAGE_1_SETTINGS["CHUNKS"] else len(full_response)
                rubric_content = full_response[start_idx:end_idx].strip()

                if rubric_content:
                    rubrics.append(f"RUBRIC {i}:\n{rubric_content}")
                else:
                    # Fallback for this rubric
                    rubrics.append(f"""
STRICT EVALUATION RUBRIC #{i} FOR: {goal}

DIMENSION: Critical Aspect #{i} Evaluation
- HIGH standards for this evaluation dimension
- DEMANDING requirements rarely fully met
- SEVERE penalties for any shortcomings

SCORING (0-{STAGE_1_SETTINGS["TOTAL_POINTS"] // STAGE_1_SETTINGS["CHUNKS"]} points):
{STAGE_1_SETTINGS["TOTAL_POINTS"] // STAGE_1_SETTINGS["CHUNKS"]}: EXCEPTIONAL - Outstanding in this aspect
{STAGE_1_SETTINGS["TOTAL_POINTS"] // STAGE_1_SETTINGS["CHUNKS"] // 2}: MINIMAL - Barely meets basic requirements
0: COMPLETE FAILURE - Does not meet any standards
""")
            else:
                # Fallback rubric when pattern not found
                rubrics.append(f"""
STRICT EVALUATION RUBRIC #{i} FOR: {goal}

DIMENSION: Critical Aspect #{i} Evaluation
- HIGH standards for this evaluation dimension
- DEMANDING requirements rarely fully met
- SEVERE penalties for any shortcomings

SCORING (0-{STAGE_1_SETTINGS["TOTAL_POINTS"] // STAGE_1_SETTINGS["CHUNKS"]} points):
{STAGE_1_SETTINGS["TOTAL_POINTS"] // STAGE_1_SETTINGS["CHUNKS"]}: EXCEPTIONAL - Outstanding in this aspect
{STAGE_1_SETTINGS["TOTAL_POINTS"] // STAGE_1_SETTINGS["CHUNKS"] // 2}: MINIMAL - Barely meets basic requirements
0: COMPLETE FAILURE - Does not meet any standards
""")

        return rubrics
    else:
        # Complete fallback - generate all 7 fallback rubrics
        rubrics = []
        for i in range(STAGE_1_SETTINGS["CHUNKS"]):
            rubric = f"""
STRICT EVALUATION RUBRIC #{i+1} FOR: {goal}

DIMENSION: Critical Aspect #{i+1} Evaluation
- HIGH standards for this evaluation dimension
- DEMANDING requirements rarely fully met
- SEVERE penalties for any shortcomings

SCORING (0-{STAGE_1_SETTINGS["TOTAL_POINTS"] // STAGE_1_SETTINGS["CHUNKS"]} points):
{STAGE_1_SETTINGS["TOTAL_POINTS"] // STAGE_1_SETTINGS["CHUNKS"]}: EXCEPTIONAL - Outstanding in this aspect
{STAGE_1_SETTINGS["TOTAL_POINTS"] // STAGE_1_SETTINGS["CHUNKS"] // 2}: MINIMAL - Barely meets basic requirements
0: COMPLETE FAILURE - Does not meet any standards
"""
            rubrics.append(rubric)
        return rubrics

async def generate_stage2_rubrics(goal, stage1_rubrics):
    """Generate all stage 2 rubrics in a single API call."""
    remaining_points = 100 - STAGE_1_SETTINGS["TOTAL_POINTS"]
    num_stage2_rubrics = remaining_points // STAGE_2_INCREMENTS

    if num_stage2_rubrics == 0:
        log_message(f"⚠️ Not enough remaining points ({remaining_points}) for STAGE_2_INCREMENTS ({STAGE_2_INCREMENTS})", "yellow")
        return []

    stage1_summary = "\n\n".join([f"RUBRIC {i+1}:\n{rubric[:300]}..." for i, rubric in enumerate(stage1_rubrics)])

    rubric_prompt = f"""
Generate {num_stage2_rubrics} STAGE 2 evaluation rubrics that COMPLEMENT and vary from the Stage 1 rubrics. Create ALL {num_stage2_rubrics} rubrics in your response.

GOAL: {goal}

STAGE 1 RUBRICS SUMMARY:
{stage1_summary}

Create {num_stage2_rubrics} DIFFERENT evaluation rubrics that focus on GENERAL DIMENSIONS not covered in Stage 1. Each rubric allocates exactly {STAGE_2_INCREMENTS} points.

REQUIREMENTS FOR EACH STAGE 2 RUBRIC:
- ONE key evaluation dimension DIFFERENT from Stage 1
- Focus on BROADER PERSPECTIVES (integration, scalability, impact, etc.)
- CLEAR scoring criteria (0-{STAGE_2_INCREMENTS} points)
- REASONABLE requirements that good solutions can meet
- Examples of both good and adequate solutions

IMPORTANT: Each rubric should be moderately challenging but allow good solutions to score reasonably well.

FORMAT: Provide {num_stage2_rubrics} complete, structured rubrics clearly separated.

STAGE 2 RUBRIC 1:
[Complete rubric here]

STAGE 2 RUBRIC 2:
[Complete rubric here]

[... continue for all {num_stage2_rubrics} rubrics]
"""

    messages = [{"role": "user", "content": rubric_prompt}]
    response = await make_api_call_with_retry(MODEL_NAME, messages)

    if response:
        full_response = response.choices[0].message.content.strip()
        log_message(f"📋 Stage 2 rubrics generated in single API call", "blue")

        # Parse the response to extract individual rubrics
        rubrics = []

        for i in range(1, num_stage2_rubrics + 1):
            # Look for STAGE 2 RUBRIC i: pattern
            rubric_start = f"STAGE 2 RUBRIC {i}:"
            if rubric_start in full_response:
                # Extract from "STAGE 2 RUBRIC i:" to next "STAGE 2 RUBRIC" or end
                start_idx = full_response.find(rubric_start) + len(rubric_start)
                end_idx = full_response.find(f"STAGE 2 RUBRIC {i+1}:", start_idx) if i < num_stage2_rubrics else len(full_response)
                rubric_content = full_response[start_idx:end_idx].strip()

                if rubric_content:
                    rubrics.append(f"STAGE 2 RUBRIC {i}:\n{rubric_content}")
                else:
                    # Fallback for this rubric
                    rubrics.append(f"""
REASONABLE STAGE 2 EVALUATION RUBRIC #{i} FOR: {goal}

DIMENSION: Additional Aspect #{i} Evaluation
- DIFFERENT from Stage 1 rubrics
- CLEAR requirements that good solutions can meet
- FAIR penalties for shortcomings

SCORING (0-{STAGE_2_INCREMENTS} points):
{STAGE_2_INCREMENTS}: EXCEPTIONAL - Excellent in this additional dimension
{STAGE_2_INCREMENTS // 2 if STAGE_2_INCREMENTS > 1 else 1}: ADEQUATE - Meets reasonable standards
0: NEEDS IMPROVEMENT - Does not meet basic standards in this dimension
""")
            else:
                # Fallback rubric
                rubrics.append(f"""
REASONABLE STAGE 2 EVALUATION RUBRIC #{i} FOR: {goal}

DIMENSION: Additional Aspect #{i} Evaluation
- DIFFERENT from Stage 1 rubrics
- CLEAR requirements that good solutions can meet
- FAIR penalties for shortcomings

SCORING (0-{STAGE_2_INCREMENTS} points):
{STAGE_2_INCREMENTS}: EXCEPTIONAL - Excellent in this additional dimension
{STAGE_2_INCREMENTS // 2 if STAGE_2_INCREMENTS > 1 else 1}: ADEQUATE - Meets reasonable standards
0: NEEDS IMPROVEMENT - Does not meet basic standards in this dimension
""")

        return rubrics
    else:
        # Complete fallback - generate all Stage 2 fallback rubrics
        rubrics = []
        for i in range(num_stage2_rubrics):
            rubric = f"""
REASONABLE STAGE 2 EVALUATION RUBRIC #{i+1} FOR: {goal}

DIMENSION: Additional Aspect #{i+1} Evaluation
- DIFFERENT from Stage 1 rubrics
- CLEAR requirements that good solutions can meet
- FAIR penalties for shortcomings

SCORING (0-{STAGE_2_INCREMENTS} points):
{STAGE_2_INCREMENTS}: EXCEPTIONAL - Excellent in this additional dimension
{STAGE_2_INCREMENTS // 2 if STAGE_2_INCREMENTS > 1 else 1}: ADEQUATE - Meets reasonable standards
0: NEEDS IMPROVEMENT - Does not meet basic standards in this dimension
"""
            rubrics.append(rubric)
        return rubrics

async def evaluate_solution_2stage(solution, goal=GOAL, stage1_rubrics=None, stage2_rubrics=None):
    """Evaluate solution using 2-stage evaluation system."""
    if not stage1_rubrics or not stage2_rubrics:
        # Generate rubrics if not provided
        stage1_rubrics = await generate_stage1_rubrics(goal)
        stage2_rubrics = await generate_stage2_rubrics(goal, stage1_rubrics)

    total_score = 0.0
    feedback_parts = []

    # STAGE 1: Evaluate with all 7 rubrics (70 points total)
    stage1_combined_rubric = "\n\n".join([f"RUBRIC {i+1} ({STAGE_1_SETTINGS['TOTAL_POINTS'] // STAGE_1_SETTINGS['CHUNKS']} points):\n{rubric}" for i, rubric in enumerate(stage1_rubrics)])

    stage1_prompt = f"""
EVALUATE SOLUTION USING STAGE 1 RUBRICS - BE CRITICAL AND STRICT!

GOAL: {goal}

SOLUTION TO EVALUATE:
{solution}

STAGE 1 RUBRICS (Total: {STAGE_1_SETTINGS['TOTAL_POINTS']} points):
{stage1_combined_rubric}

INSTRUCTIONS - STAGE 1 EVALUATION:
1. Evaluate the solution using EACH of the {STAGE_1_SETTINGS['CHUNKS']} rubrics above
2. Be STRICT and find flaws in each evaluation dimension
3. Assign scores for EACH rubric (0-{STAGE_1_SETTINGS['TOTAL_POINTS'] // STAGE_1_SETTINGS['CHUNKS']} points each)
4. Sum all rubric scores to get STAGE 1 TOTAL (0-{STAGE_1_SETTINGS['TOTAL_POINTS']} points)
5. Only exceptional solutions should score above {STAGE_1_SETTINGS['MINIMUM_SCORE_TO_PASS_STAGE_1']} points

REQUIRED FORMAT:
STAGE 1 SCORES:
RUBRIC 1: [score] - [brief reason]
RUBRIC 2: [score] - [brief reason]
... etc
STAGE 1 TOTAL: [sum]/{STAGE_1_SETTINGS['TOTAL_POINTS']}
"""

    messages = [{"role": "user", "content": stage1_prompt}]
    response = await make_api_call_with_retry(MODEL_NAME, messages)

    if not response:
        return {"score": 0.0, "feedback": "Stage 1 evaluation failed - API error", "stage1_passed": False}

    stage1_text = response.choices[0].message.content.strip()
    feedback_parts.append(f"STAGE 1 EVALUATION:\n{stage1_text}")

    # Parse stage 1 results
    stage1_total = 0.0
    try:
        lines = stage1_text.split('\n')
        for line in lines:
            if 'STAGE 1 TOTAL:' in line:
                # Extract number before the slash
                total_part = line.split('STAGE 1 TOTAL:')[1].split('/')[0].strip()
                numbers = re.findall(r'\d+\.?\d*', total_part)
                if numbers:
                    stage1_total = float(numbers[0])
                break
    except Exception as e:
        log_message(f"⚠️ Failed to parse Stage 1 score: {e}", "yellow")
        stage1_total = 0.0

    total_score += stage1_total
    stage1_passed = stage1_total >= STAGE_1_SETTINGS["MINIMUM_SCORE_TO_PASS_STAGE_1"]

    if not stage1_passed:
        feedback_parts.append(f"\n❌ FAILED STAGE 1: {stage1_total:.1f}/{STAGE_1_SETTINGS['TOTAL_POINTS']} < {STAGE_1_SETTINGS['MINIMUM_SCORE_TO_PASS_STAGE_1']} minimum")
        return {
            "score": total_score,
            "feedback": "\n".join(feedback_parts),
            "stage1_passed": False,
            "stage1_score": stage1_total,
            "stage2_score": 0.0
        }

    # STAGE 2: Evaluate with multiple complementary rubrics
    stage2_combined_rubric = "\n\n".join([f"RUBRIC {i+1} ({STAGE_2_INCREMENTS} points):\n{rubric}" for i, rubric in enumerate(stage2_rubrics)])

    stage2_prompt = f"""
EVALUATE SOLUTION USING ALL STAGE 2 RUBRICS - COMPLEMENTARY PERSPECTIVES!

GOAL: {goal}

SOLUTION TO EVALUATE:
{solution}

STAGE 2 RUBRICS (Total: {100 - STAGE_1_SETTINGS['TOTAL_POINTS']} points):
{stage2_combined_rubric}

INSTRUCTIONS - STAGE 2 EVALUATION:
1. Evaluate the solution using EACH of the {len(stage2_rubrics)} Stage 2 rubrics above
2. Use DIFFERENT evaluation criteria than Stage 1
3. Focus on ADDITIONAL aspects not covered in Stage 1
4. Each rubric allocates exactly {STAGE_2_INCREMENTS} points
5. Be fair but thorough - good solutions can score well in these rubrics

REQUIRED FORMAT:
STAGE 2 SCORES:
RUBRIC 1: [score] - [brief reason]
RUBRIC 2: [score] - [brief reason]
RUBRIC 3: [score] - [brief reason]
[... for each rubric ...]
STAGE 2 TOTAL: [sum]/{100 - STAGE_1_SETTINGS['TOTAL_POINTS']}
"""

    messages = [{"role": "user", "content": stage2_prompt}]
    response = await make_api_call_with_retry(MODEL_NAME, messages)

    stage2_score = 0.0
    if response:
        stage2_text = response.choices[0].message.content.strip()
        feedback_parts.append(f"\nSTAGE 2 EVALUATION:\n{stage2_text}")

        # Parse stage 2 results
        try:
            lines = stage2_text.split('\n')
            for line in lines:
                if 'STAGE 2 TOTAL:' in line:
                    # Extract number before the slash
                    total_part = line.split('STAGE 2 TOTAL:')[1].split('/')[0].strip()
                    numbers = re.findall(r'\d+\.?\d*', total_part)
                    if numbers:
                        stage2_score = float(numbers[0])
                    break
        except Exception as e:
            log_message(f"⚠️ Failed to parse Stage 2 score: {e}", "yellow")
            stage2_score = 0.0
    else:
        feedback_parts.append("\n❌ Stage 2 evaluation failed - API error")

    total_score += stage2_score

    # Ensure total score is within bounds
    total_score = max(MINIMUM_QUALITY_THRESHOLD, min(MAXIMUM_QUALITY_SCORE, total_score))

    feedback_parts.insert(0, f"✅ PASSED STAGE 1: {stage1_total:.1f}/{STAGE_1_SETTINGS['TOTAL_POINTS']} ≥ {STAGE_1_SETTINGS['MINIMUM_SCORE_TO_PASS_STAGE_1']}")
    feedback_parts.append(f"\nFINAL SCORE: {total_score:.1f}/100 (Stage 1: {stage1_total:.1f}, Stage 2: {stage2_score:.1f})")

    return {
        "score": total_score,
        "feedback": "\n".join(feedback_parts),
        "stage1_passed": True,
        "stage1_score": stage1_total,
        "stage2_score": stage2_score
    }

def save_solution_with_quality(solution, quality_score, feedback, node_id):
    """Save solution to enumerated file with quality information."""
    if not os.path.exists(SOLUTIONS_FOLDER):
        os.makedirs(SOLUTIONS_FOLDER)

    filename = f"{SOLUTIONS_FOLDER}/solution_{node_id}_{quality_score:.1f}.txt"

    header_content = f"""SOLUTION {node_id}
Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}
Quality Score: {quality_score:.1f}/100
Goal: {GOAL}

FEEDBACK:
{feedback}

{'='*80}

SOLUTION:
{solution}
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(header_content)

    log_message(f"💾 Solution {node_id} saved ({quality_score:.1f}/100)", "cyan")
    return filename

def save_best_solution(solution, quality_score, feedback):
    """Save the best solution found to a dedicated file."""
    if not os.path.exists(SOLUTIONS_FOLDER):
        os.makedirs(SOLUTIONS_FOLDER)

    filename = f"{SOLUTIONS_FOLDER}/best_solution.txt"

    header_content = f"""🏆 BEST SOLUTION FOUND
Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}
Quality Score: {quality_score:.1f}/100
Goal: {GOAL}

FEEDBACK:
{feedback}

{'='*80}

BEST SOLUTION:
{solution}
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(header_content)

    log_message(f"🏆 BEST SOLUTION saved to {filename} ({quality_score:.1f}/100)", "green")
    return filename

def extract_top_performers(cycle_results):
    """Extract the top performing solutions from a cycle."""
    if not cycle_results:
        return []

    sorted_results = sorted(cycle_results, key=lambda x: x['quality_score'], reverse=True)
    top_performers = sorted_results[:TOP_PERFORMERS_TO_KEEP]

    log_message(f"🏆 Top {len(top_performers)} performers extracted:", "green")
    for i, performer in enumerate(top_performers, 1):
        log_message(f"  {i}. Score: {performer['quality_score']:.1f}/100 (Node {performer['node_id']})", "green")

    return top_performers

def collect_success_examples(top_performers, all_cycle_results):
    """Collect success examples from the top performers."""
    success_examples = {}

    for performer in top_performers:
        node_id = performer['node_id']
        performer_key = f"node_{node_id}"

        performer_result = next((r for r in all_cycle_results if r['node_id'] == node_id), None)

        if performer_result:
            success_examples[performer_key] = {
                'quality_score': performer['quality_score'],
                'solution': performer['solution'],
                'feedback': performer.get('feedback', ''),
                'node_id': node_id
            }
            log_message(f"📝 Collected success example for Node {node_id}", "cyan")

    return success_examples

def create_improved_prompt(base_prompt, feedback, node_id, eval_results=None, success_examples=None, cycle_number=1):
    """Create an improved prompt that includes feedback and top performers from previous cycles."""
    if not feedback and not success_examples:
        return base_prompt

    improvement_message = f"""
🔧 CYCLE {cycle_number} IMPROVEMENT REQUEST

GOAL: {GOAL}

PREVIOUS SOLUTION ANALYSIS:
{feedback}

📚 LEARNING OBJECTIVES:
1. Study the feedback and identify specific improvement areas
2. Analyze successful patterns from top performers when available
3. Build incrementally upon proven successful approaches
4. Balance proven techniques with creative innovation
5. Focus on clear, comprehensive solutions that fully address the goal

🎨 CREATIVITY GUIDELINES:
- Study previous high-quality solutions for inspiration, not imitation
- Explore novel approaches while maintaining goal relevance
- Combine the best elements from high-performing solutions with new innovations
- Build incrementally upon proven successful approaches
- Be intelligently creative while staying focused on the goal

{f'''🎯 CROSS-CYCLE LEARNING - CYCLE {cycle_number}
From previous cycles, here are the top performing solutions and their patterns.
Study these successful approaches:

''' + "\n".join([
    f"""TOP PERFORMER #{i+1} (Score: {performer_data['quality_score']:.1f}/100):
Solution Summary: {performer_data['solution'][:300]}...
Feedback: {performer_data['feedback']}

Key Learning: This solution excelled because {performer_data['feedback'].split('.')[0] if '.' in performer_data['feedback'] else performer_data['feedback']}
"""
    for i, (performer_key, performer_data) in enumerate((success_examples or {}).items())
]) + '''

🔬 CROSS-CYCLE INSIGHTS:
- Analyze the patterns that made these top performers successful
- Identify common success factors across different approaches
- Combine the strengths of multiple successful solutions
- Avoid the issues mentioned in previous feedback
- Build upon proven successful approaches while innovating new combinations

''' if success_examples else ''}

Generate an improved solution that addresses the previous feedback and maintains quality on the broader goal requirements.

💡 FINAL NOTE: If high-quality solutions exist so far, you can use parts of them for inspiration. Build incrementally upon proven approaches while adding creative innovations. Never repeat solutions in their entirety - always modify and improve upon successful patterns.
"""

    return base_prompt + improvement_message

def get_rank_score(node, all_nodes):
    """Get rank-normalized score for a node across all evaluated nodes."""
    if not all_nodes:
        return 0.0

    evaluated_nodes = [n for n in all_nodes if n.quality_score > MINIMUM_QUALITY_THRESHOLD]

    if not evaluated_nodes:
        return 0.0

    sorted_nodes = sorted(evaluated_nodes, key=lambda x: x.quality_score, reverse=True)

    try:
        rank = sorted_nodes.index(node) + 1
        total_nodes = len(sorted_nodes)
        return 1.0 - (rank - 1) / max(1, total_nodes - 1)
    except ValueError:
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

def puct_score(node, total_visits, c_puct=C_PUCT, parent=None, all_nodes=None):
    """Calculate PUCT score for a node using Q-values and exploration."""
    if node.visits == 0:
        return float('inf')

    q_value = (node.value / max(1, node.visits)) / MAXIMUM_QUALITY_SCORE

    if all_nodes:
        rank_score = get_rank_score(node, all_nodes)
        q_value = 0.7 * q_value + 0.3 * rank_score

    exploration = c_puct * math.sqrt(math.log(total_visits + 1) / (node.visits + 1))

    if parent and parent.children:
        prior_factor = 1.0 / max(1, len(parent.children))
        exploration *= prior_factor

    return q_value + exploration

def select_multiple_nodes(root, num_branches=PARALLEL_BRANCHES):
    """Select multiple nodes to expand in parallel using PUCT, ensuring unique leaves."""
    selected_nodes_and_paths = []
    selected_leaves = set()

    # If tree only has root (no children), allow multiple branches to start from root
    if not root.children:
        # For initial exploration, allow all branches to start from root
        # They will expand different children once created
        for _ in range(num_branches):
            selected_nodes_and_paths.append((root, [root]))
        log_message(f"🌱 Starting {num_branches} branches from root (initial expansion)", "cyan")
        return selected_nodes_and_paths

    # Tree has children - try to find unique exploration paths
    for branch_idx in range(num_branches):
        current = root
        path = [current]
        found_unique_path = False

        # Try multiple times to find a unique path
        for attempt in range(5):  # Reduced attempts for efficiency
            current = root
            path = [current]
            branch_path_taken = set()  # Track nodes visited in this branch

            while current.children:
                total_visits = sum(child.visits for child in current.children)
                all_nodes = collect_all_nodes(root)
                available_children = [child for child in current.children
                                    if child not in selected_leaves and child not in branch_path_taken]

                if not available_children:
                    # No available children in this subtree, try different approach
                    break

                best_child = max(available_children, key=lambda child: puct_score(child, total_visits, parent=current, all_nodes=all_nodes))
                current = best_child
                path.append(current)
                branch_path_taken.add(current)

            # Check if we found a path that ends at a unique leaf
            if current not in selected_leaves:
                selected_leaves.add(current)
                selected_nodes_and_paths.append((current, path))
                found_unique_path = True
                break

        # If we couldn't find a unique path, use the root as fallback
        if not found_unique_path:
            selected_nodes_and_paths.append((root, [root]))
            log_message(f"⚠️ Branch {branch_idx + 1} using root as fallback", "yellow")

    return selected_nodes_and_paths

def backpropagate(path, value):
    """Backpropagate the value up the tree (thread-safe)."""
    for node in reversed(path):
        with node.lock:
            node.visits += 1
            node.value += value

async def process_single_branch(branch_id, selected_node, path, conversation_histories, quality_history, cycle_number,
                              success_examples, global_node_id_counter, base_prompt, best_quality, best_node, node_count, stage1_rubrics, stage2_rubrics):
    """Process a single branch with parallel children generation and evaluation."""
    log_message(f"🌿 BRANCH {branch_id}: Selected node with quality: {selected_node.quality_score:.1f}", "cyan")

    # Check for stagnation using utility function
    is_stagnant = False
    stuck_score = None
    if node_count % STAGNATION_CHECK_FREQUENCY == 0:
        is_stagnant, stuck_score = check_stagnation_pattern(quality_history)
        if is_stagnant:
            log_message(f"🔄 BRANCH {branch_id}: STAGNATION DETECTED: {stuck_score:.1f} quality repeated 3 times", "yellow")

    # Hybridization
    is_hybridization = False
    hybridization_prompt = None
    if node_count % HYBRIDIZATION_FREQUENCY == 0 and len(quality_history) > 1:
        all_nodes = collect_all_nodes(path[0])
        top_nodes = sorted([n for n in all_nodes if n.quality_score > MINIMUM_QUALITY_THRESHOLD], key=lambda x: x.quality_score, reverse=True)
        if len(top_nodes) >= 2:
            top1, top2 = top_nodes[0], top_nodes[1]
            hybridization_prompt = f"""
🎯 HYBRIDIZATION REQUEST: Combine the best elements from these two successful solutions:

TOP PERFORMER 1 (Score: {top1.quality_score:.1f}/100):
{top1.solution[:300]}...

TOP PERFORMER 2 (Score: {top2.quality_score:.1f}/100):
{top2.solution[:300]}...

Create a new, improved solution that takes the best parts from both approaches.
"""
            is_hybridization = True
            log_message(f"🔗 BRANCH {branch_id}: Attempting hybridization of top two performers", "magenta")

    # Generate current prompt
    current_prompt = selected_node.prompt

    # Apply stagnation feedback
    if is_stagnant and stuck_score:
        current_prompt = create_stagnation_feedback_prompt(stuck_score, global_node_id_counter['value'], current_prompt)
        log_message(f"💡 BRANCH {branch_id}: Applied stagnation feedback", "yellow")

    # Apply hybridization prompt
    if hybridization_prompt:
        current_prompt = hybridization_prompt
        log_message(f"🔗 BRANCH {branch_id}: Using hybridization prompt", "magenta")

    # Get conversation history
    with state_lock:
        if selected_node in conversation_histories:
            conversation_history = conversation_histories[selected_node].copy()
        else:
            conversation_history = [{"role": "user", "content": current_prompt}]

    # Inject best solution context
    best_solution_context = ""
    if best_node and best_node.solution and best_quality > 0:
        best_solution_context = f"""

💡 CURRENT BEST SOLUTION (Score: {best_quality:.1f}/100):
{best_node.solution[:800]}...

LEARN FROM THIS SUCCESS: Study the patterns that made this solution effective.
"""

    # Create improved prompt if node has feedback
    if selected_node.feedback:
        improved_base_prompt = base_prompt + best_solution_context
        current_prompt = create_improved_prompt(
            improved_base_prompt,
            selected_node.feedback,
            global_node_id_counter['value'],
            selected_node.eval_results,
            success_examples if cycle_number > 1 else None,
            cycle_number
        )

    # Always append current prompt to conversation history
    conversation_history.append({"role": "user", "content": current_prompt})

    log_message(f"🤖 BRANCH {branch_id}: Sending request to {MODEL_NAME}...", "yellow")

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
        'quality_score': 0.0
    }

    if response:
        generated_solution = response.choices[0].message.content.strip()

        if not generated_solution:
            log_message(f"❌ BRANCH {branch_id}: Empty response from model", "red")
            backpropagate(path, 0.0)
            return branch_results

        log_message(f"✅ BRANCH {branch_id}: Received solution from model", "green")

        # Update conversation history (don't write back to shared selected_node to prevent context bleeding)
        conversation_history.append({"role": "assistant", "content": generated_solution})

        log_message(f"\n📊 BRANCH {branch_id}: Evaluating solution with 2-stage system...", "yellow")
        eval_results = await evaluate_solution_2stage(generated_solution, GOAL, stage1_rubrics, stage2_rubrics)

        branch_results['eval_results'] = eval_results

        if eval_results:
            current_quality = eval_results['score']
            branch_results['quality_score'] = current_quality
            log_message(f"🎯 BRANCH {branch_id}: Solution quality: {current_quality:.1f}/100", "cyan")

            # Generate variations in parallel
            log_message(f"🌿 BRANCH {branch_id}: Generating and evaluating {TREE_CHILDREN_PER_EXPANSION} variations", "cyan")

            # Main child data
            with global_node_id_counter['lock']:
                main_child_node_id = global_node_id_counter['value']
                global_node_id_counter['value'] += 1

            children_data = [{
                'type': 'main',
                'node_id': main_child_node_id,
                'branch_id': branch_id,
                'solution': generated_solution,
                'prompt': current_prompt,
                'conversation_history': conversation_history,
                'eval_results': eval_results,
                'quality_score': current_quality
            }]

            # Generate variation prompts and data
            for child_idx in range(TREE_CHILDREN_PER_EXPANSION - 1):
                with global_node_id_counter['lock']:
                    variation_node_id = global_node_id_counter['value']
                    global_node_id_counter['value'] += 1

                varied_prompt = current_prompt + f"\n\nVARIATION {child_idx + 1}: Provide a different but equally good solution to the same goal."
                variation_history = [{"role": "user", "content": base_prompt}]

                children_data.append({
                    'type': 'variation',
                    'node_id': variation_node_id,
                    'branch_id': branch_id,
                    'prompt': varied_prompt,
                    'conversation_history': variation_history,
                    'solution': None,
                    'eval_results': None,
                    'quality_score': None
                })

            # Generate variations in parallel
            generation_tasks = []
            for child_data in children_data:
                if child_data['type'] == 'variation':
                    task = make_api_call_with_retry(
                        MODEL_NAME,
                        child_data['conversation_history'] + [{"role": "user", "content": child_data['prompt']}]
                    )
                    generation_tasks.append((child_data, task))

            if generation_tasks:
                log_message(f"🤖 BRANCH {branch_id}: Generating {len(generation_tasks)} variation solutions", "yellow")
                generation_results = await asyncio.gather(*[task for _, task in generation_tasks])

                for (child_data, _), response in zip(generation_tasks, generation_results):
                    if response:
                        variation_solution = response.choices[0].message.content.strip()
                        if variation_solution:
                            child_data['solution'] = variation_solution

            # Evaluate variations in parallel
            evaluation_tasks = []
            valid_children_data = []

            for child_data in children_data:
                if child_data['solution'] or child_data['type'] == 'main':
                    valid_children_data.append(child_data)

            for child_data in valid_children_data:
                if child_data['type'] == 'variation':
                    task = evaluate_solution_2stage(child_data['solution'], GOAL, stage1_rubrics, stage2_rubrics)
                    evaluation_tasks.append((child_data, task))

            if evaluation_tasks:
                log_message(f"📊 BRANCH {branch_id}: Evaluating {len(evaluation_tasks)} variations", "yellow")
                evaluation_results = await asyncio.gather(*[task for _, task in evaluation_tasks])

                for (child_data, _), eval_result in zip(evaluation_tasks, evaluation_results):
                    if eval_result:
                        child_data['eval_results'] = eval_result
                        child_data['quality_score'] = eval_result['score']

            branch_results['children_data'] = valid_children_data

        else:
            log_message(f"❌ BRANCH {branch_id}: Evaluation failed", "red")
    else:
        log_message(f"❌ BRANCH {branch_id}: Failed to get response from model", "red")

    return branch_results

async def generate_solution():
    """Main function for parallel tree search solution generation."""
    log_message(f"🎯 Starting goal-oriented solution generation", "blue")
    log_message(f"Goal: {GOAL}", "yellow")

    # Generate 2-stage evaluation rubrics in parallel (2 API calls total)
    log_message("📋 Generating Stage 1 and Stage 2 rubrics in parallel (2 API calls)...", "blue")

    # Run both rubric generations in parallel
    stage1_task = generate_stage1_rubrics(GOAL)
    # Stage 2 needs stage 1 results, so we generate a placeholder task that will be called after stage 1 completes
    stage1_rubrics_result = await stage1_task

    stage2_task = generate_stage2_rubrics(GOAL, stage1_rubrics_result)
    stage2_rubrics_result = await stage2_task

    stage1_rubrics = stage1_rubrics_result
    stage2_rubrics = stage2_rubrics_result

    log_message("✅ 2-Stage evaluation rubrics generated with 2 API calls", "green")

    # Save the evaluation rubrics for transparency (separate files for each stage)
    if not os.path.exists(RUBRICS_FOLDER):
        os.makedirs(RUBRICS_FOLDER)

    # Save Stage 1 rubrics to separate file
    stage1_filename = f"{RUBRICS_FOLDER}/stage1_rubrics.txt"
    with open(stage1_filename, "w", encoding="utf-8") as f:
        f.write(f"STAGE 1 EVALUATION RUBRICS FOR GOAL:\n{GOAL}\n\n")
        f.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Stage 1 points: {STAGE_1_SETTINGS['TOTAL_POINTS']} ({STAGE_1_SETTINGS['CHUNKS']} rubrics × {STAGE_1_SETTINGS['TOTAL_POINTS'] // STAGE_1_SETTINGS['CHUNKS']} points each)\n")
        f.write(f"Stage 1 pass threshold: {STAGE_1_SETTINGS['MINIMUM_SCORE_TO_PASS_STAGE_1']}/{STAGE_1_SETTINGS['TOTAL_POINTS']} points\n\n")
        f.write(f"{'='*80}\n\n")
        for i, rubric in enumerate(stage1_rubrics):
            f.write(f"RUBRIC {i+1} ({STAGE_1_SETTINGS['TOTAL_POINTS'] // STAGE_1_SETTINGS['CHUNKS']} points):\n{rubric}\n")
            f.write(f"{'-'*40}\n\n")

    # Save Stage 2 rubrics to separate file
    stage2_filename = f"{RUBRICS_FOLDER}/stage2_rubrics.txt"
    with open(stage2_filename, "w", encoding="utf-8") as f:
        f.write(f"STAGE 2 EVALUATION RUBRICS FOR GOAL:\n{GOAL}\n\n")
        f.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        remaining_points = 100 - STAGE_1_SETTINGS['TOTAL_POINTS']
        num_stage2_rubrics = remaining_points // STAGE_2_INCREMENTS
        f.write(f"Total Stage 2 points: {remaining_points} ({num_stage2_rubrics} rubrics × {STAGE_2_INCREMENTS} points each)\n\n")
        f.write(f"{'='*80}\n\n")
        for i, rubric in enumerate(stage2_rubrics):
            f.write(f"STAGE 2 RUBRIC {i+1} ({STAGE_2_INCREMENTS} points):\n{rubric}\n")
            f.write(f"{'-'*40}\n\n")

    log_message(f"📋 Stage 1 rubrics saved to {stage1_filename}", "cyan")
    log_message(f"📋 Stage 2 rubrics saved to {stage2_filename}", "cyan")

    base_prompt = f"""
{GOAL}

Provide a direct, high-quality solution to the above request.
"""

    # Tree Search variables
    root = TreeNode(prompt=base_prompt)
    best_quality = 0.0
    best_node = root
    quality_history = []
    cycle_number = 1
    success_examples = {}
    reflection_history = []

    # Plotting tracking variables
    plot_quality_scores = []
    plot_evaluation_numbers = []
    plot_best_qualities = []
    evaluation_counter = 0

    # Thread-safe global node ID counter
    global_node_id_counter = {'value': 0, 'lock': threading.Lock()}

    # Conversation history for the tree
    conversation_histories = {root: [{"role": "user", "content": base_prompt}]}

    for node_count in range(1, TOTAL_NODES + 1):
        log_message(f"\n🌳 PARALLEL TREE SEARCH - NODE {node_count}/{TOTAL_NODES} (Cycle {cycle_number})", "blue")
        log_message(f"🌿 Processing {PARALLEL_BRANCHES} branches in parallel", "cyan")

        # Select multiple nodes to expand in parallel
        selected_branches = select_multiple_nodes(root, PARALLEL_BRANCHES)

        # Pad to target concurrency if fewer branches were selected
        if len(selected_branches) < PARALLEL_BRANCHES:
            deficit = PARALLEL_BRANCHES - len(selected_branches)
            selected_branches += [(root, [root])] * deficit
            log_message(f"📈 Padded to {PARALLEL_BRANCHES} branches (added {deficit} root branches)", "cyan")

        # Create tasks for parallel branch processing
        branch_tasks = []
        for branch_id, (selected_node, path) in enumerate(selected_branches, 1):
            task = process_single_branch(
                branch_id, selected_node, path, conversation_histories, quality_history,
                cycle_number, success_examples, global_node_id_counter, base_prompt, best_quality, best_node, node_count, stage1_rubrics, stage2_rubrics
            )
            branch_tasks.append(task)

        # Execute branches in parallel
        log_message(f"🚀 Executing {len(branch_tasks)} branches concurrently", "green")
        branch_results = await asyncio.gather(*branch_tasks)

        # Process results from all branches
        all_children_data = []
        for branch_result in branch_results:
            all_children_data.extend(branch_result['children_data'])

        # Process all children from parallel branches
        for child_data in all_children_data:
            selected_node = None
            child_path = None
            for branch_result in branch_results:
                if branch_result['branch_id'] == child_data['branch_id']:
                    selected_node = branch_result['selected_node']
                    child_path = branch_result['path']
                    break

            if not selected_node:
                continue

            # Plot ALL evaluations (even failed ones)
            if child_data.get('eval_results') and child_data.get('quality_score', 0) > MINIMUM_QUALITY_THRESHOLD:
                evaluation_counter += 1
                plot_quality_scores.append(child_data['quality_score'])
                plot_evaluation_numbers.append(evaluation_counter)
                plot_best_qualities.append(best_quality)

                # Update progress plot for EVERY evaluation
                plot_progress(plot_quality_scores, plot_evaluation_numbers, plot_best_qualities, evaluation_counter)

            # Only create and add nodes that have successful evaluations AND passed Stage 1
            if (child_data.get('eval_results') and
                child_data.get('quality_score', 0) > MINIMUM_QUALITY_THRESHOLD and
                child_data['eval_results'].get('stage1_passed', False)):
                # Create tree node
                child_node = TreeNode(
                    solution=child_data['solution'],
                    parent=selected_node,
                    prompt=child_data['prompt']
                )

                child_node.quality_score = child_data['quality_score']
                child_node.feedback = child_data['eval_results']['feedback']
                child_node.eval_results = child_data['eval_results']

                # Update best quality
                if child_node.quality_score > best_quality:
                    best_quality = child_node.quality_score
                    best_node = child_node
                    log_message(f"🏆 New best: {best_quality:.1f}/100", "green")

                quality_history.append(child_node.quality_score)

                # Only save solutions that pass Stage 1
                save_solution_with_quality(
                    solution=child_node.solution,
                    quality_score=child_node.quality_score,
                    feedback=child_node.feedback,
                    node_id=child_data['node_id']
                )
                log_message(f"💾 Solution {child_data['node_id']} saved (passed Stage 1)", "cyan")

                # Add to conversation histories
                child_conversation_history = child_data['conversation_history'] + [
                    {"role": "assistant", "content": child_node.solution}
                ]
                with state_lock:
                    conversation_histories[child_node] = child_conversation_history

                # Add to tree
                with selected_node.lock:
                    selected_node.children.append(child_node)

                # Backpropagate
                if child_path:
                    backpropagate(child_path + [child_node], child_node.quality_score)
            else:
                # Failed evaluation or Stage 1 failure - only backpropagate zero value without adding node
                log_message(f"❌ Node {child_data['node_id']} evaluation failed or below threshold - skipping tree addition", "yellow")
                if child_path:
                    backpropagate(child_path, 0.0)

        # Update success examples for cross-cycle learning
        if all_children_data and cycle_number > 1:
            # Extract successful solutions from this cycle
            cycle_results = []
            for child_data in all_children_data:
                if child_data.get('eval_results') and child_data.get('quality_score', 0) > MINIMUM_QUALITY_THRESHOLD:
                    cycle_results.append({
                        'node_id': child_data['node_id'],
                        'quality_score': child_data['quality_score'],
                        'solution': child_data['solution'],
                        'feedback': child_data['eval_results']['feedback']
                    })

            if cycle_results:
                # Get top performers from this cycle
                top_performers = extract_top_performers(cycle_results)

                # Update success examples with cross-cycle learning
                success_examples = collect_success_examples(top_performers, cycle_results)

        # Check if target quality reached
        max_child_quality = max((c.get('quality_score', 0) for c in all_children_data), default=0)
        if max_child_quality >= TARGET_QUALITY_THRESHOLD:
            log_message(f"🎯 Target quality reached: {max_child_quality:.1f}/100 in Node {node_count}", "green")
            break

        # Periodic reflection
        if REFLECTION_FREQUENCY > 0 and node_count % REFLECTION_FREQUENCY == 0 and node_count > 0:
            log_message(f"\n🧠 PERIODIC REFLECTION - NODE {node_count}", "magenta")

            reflection_prompt = f"""
CYCLE {cycle_number} PROGRESS REFLECTION (Node {node_count})

Current Progress:
- Best quality: {best_quality:.1f}/100
- Total nodes explored: {node_count}
- Parallel branches: {PARALLEL_BRANCHES}

Strategic Analysis:
1. What patterns are emerging in successful solutions?
2. Are there specific approaches that consistently perform better?
3. What types of feedback are most common?
4. What new strategies should be prioritized?

GOAL: {GOAL}

Provide strategic insights for the remaining parallel tree search.
"""

            best_context = ""
            if best_node and best_node.solution:
                best_context = f"""
Current Best Solution (Score: {best_quality:.1f}/100):
{best_node.solution[:500]}..."""

            full_reflection_prompt = reflection_prompt + best_context

            log_message("🤔 Requesting periodic reflection from model...", "magenta")
            reflection_response = await make_api_call_with_retry(MODEL_NAME, [{"role": "user", "content": full_reflection_prompt}])

            if reflection_response:
                reflection_text = reflection_response.choices[0].message.content.strip()

                # Save reflection
                if not os.path.exists(REFLECTIONS_FOLDER):
                    os.makedirs(REFLECTIONS_FOLDER)

                reflection_filename = f"{REFLECTIONS_FOLDER}/reflection_node_{node_count}.txt"
                with open(reflection_filename, "w", encoding="utf-8") as f:
                    f.write(f"NODE {node_count} REFLECTION\n")
                    f.write(f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                    f.write(f"Best Quality: {best_quality:.1f}/100\n")
                    f.write(f"Total Nodes: {node_count}\n")
                    f.write(f"Parallel Branches: {PARALLEL_BRANCHES}\n\n")
                    f.write("=" * 80 + "\n\n")
                    f.write(reflection_text)

                log_message(f"📝 Periodic reflection saved to {reflection_filename}", "magenta")

                reflection_history.append({
                    'node': node_count,
                    'content': reflection_text,
                    'filename': reflection_filename,
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
                })

                if len(reflection_history) > REFLECTIONS_TO_KEEP:
                    reflection_history = reflection_history[-REFLECTIONS_TO_KEEP:]

        # Increment cycle number for cross-cycle learning (after reflection)
        cycle_number += 1

    log_message("✨ Parallel tree search complete!", "blue")
    log_message(f"🏆 Best quality achieved: {best_quality:.1f}/100", "green")
    log_message(f"🌿 Used {PARALLEL_BRANCHES} parallel branches per iteration", "cyan")

    # Summary
    log_message("\n" + "="*60, "green")
    log_message("🎯 SOLUTION GENERATION SUMMARY", "green")
    log_message("="*60, "green")
    log_message(f"GOAL: {GOAL}", "yellow")
    log_message(f"BEST QUALITY SCORE: {best_quality:.1f}/100", "green")
    log_message(f"TOTAL NODES EXPLORED: {len(collect_all_nodes(root))}", "cyan")
    log_message(f"SOLUTIONS GENERATED: {len([n for n in collect_all_nodes(root) if n.quality_score > MINIMUM_QUALITY_THRESHOLD])}", "cyan")

    if best_node and best_node.solution:
        log_message(f"\n🏆 BEST SOLUTION PREVIEW:", "green")
        preview = best_node.solution[:500] + "..." if len(best_node.solution) > 500 else best_node.solution
        log_message(preview, "white")

        # Save the best solution to a dedicated file
        save_best_solution(best_node.solution, best_quality, best_node.feedback)

if __name__ == "__main__":
    log_message("🚀 Starting goal-oriented solution generation with Parallel Tree Search...", "blue")
    asyncio.run(generate_solution())
    log_message("✨ Process complete!", "blue")

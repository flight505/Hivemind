import subprocess
import json
from openai import OpenAI
import pandas as pd
import re
from termcolor import colored
import os
import shutil
from datetime import datetime
from collections import deque

# Constants
ITERATIONS = 25
ERROR_HISTORY_SIZE = 3  # Keep track of last 3 errors
SOLUTION_HISTORY_SIZE = 3   # Keep track of last 3 solutions
error_history = deque(maxlen=ERROR_HISTORY_SIZE)
solution_history = deque(maxlen=SOLUTION_HISTORY_SIZE)  # Store tuples of (solution_code, progress_report)
OPENROUTER_MODEL = "x-ai/grok-code-fast-1"
MAX_RUNTIME_MINUTES = 30  # Maximum runtime in minutes
IMPROVEMENT_EFFORT = "high"

# Prompt scaffolding
SYSTEM_PROMPT_MAIN = (
    "You are an elite ML scientist and senior Python engineer. Produce COMPLETE, runnable Python scripts. "
    "Follow these rules strictly: "
    "- Return ONLY a single code block fenced with ```python and ```; no prose. "
    "- Include all imports and utility functions. "
    "- Make solutions fast, memory-efficient, and reproducible (set seeds). "
    "- Prefer gradient boosting libraries (LightGBM/XGBoost/CatBoost) with GPU if available; otherwise robust CPU fallback. "
    "- Always split train into train/validation via KFold (classification: StratifiedKFold); 5 folds unless constrained by time. "
    "- Detect task type automatically (classification vs regression) from target heuristics. "
    "- Choose metric: classification=accuracy (also report F1/AUC if class imbalance); regression=RMSE and MAE. "
    "- Handle missing data, categorical encoding, and scaling via simple, reliable defaults (e.g., imputation, CatBoost encoder or one-hot, StandardScaler only for linear models). "
    "- Prevent leakage (fit transforms on training folds only; use ColumnTransformer or per-fold fit). "
    "- Use early stopping where supported; cap estimator counts/iterations to meet runtime. "
    "- Print fold metrics and overall mean/std. "
    "- Save progress_report.json with: best_model, cv_scores, mean_cv, std_cv, validation_scheme, features_used, feature_importances (top 30 if available), training_time_seconds, oof_score (if available), notes. "
    "- Save submission.csv in required format. "
    "- Ensure the script completes within the given time budget. "
)

SYSTEM_PROMPT_OPTIMIZE = (
    "You are optimizing an ML pipeline to fit within a strict runtime while preserving accuracy. Return a COMPLETE, runnable script in one ```python block. "
    "Prioritize: fast feature processing (vectorized pandas, minimal copies), using LightGBM/CatBoost GPU, early stopping, fewer estimators, reduced CV folds (e.g., 3), and smaller hyperparameter search. "
    "Avoid removing core features or changing output contract (must write progress_report.json and submission.csv). Keep the same I/O and file names."
)

SYSTEM_PROMPT_FIX = (
    "You are a precise Python troubleshooter. Return ONLY the FULL corrected script in one ```python block. "
    "Keep behavior the same: still train, evaluate, and write progress_report.json and submission.csv. "
    "If a module is missing, add a guarded pip install using subprocess.check_call at the top, then import. "
    "Add GPU checks when possible; keep transformations fit only on training folds to avoid leakage. "
    "Do not add explanations or extra text."
)

OPTIONAL_INSTRUCTIONS = (
    "Think carefully about feature engineering and leakage. Favor robust encoders (e.g., CatBoost or target-safe encodings) and simple wins: ratio features, counts, interactions controlled by variance thresholds. "
    "If accuracy surpasses ~82-83%, allocate some budget to model scaling/hyperparameter tuning. "
    "The machine has limited VRAM (8GB) and RAM (~30GB); be memory-conscious. Maintain a 70-30 train-test methodology internally (fold splits approximate this). Avoid overfitting."
)

print(colored("Phase 1: Setting up OpenRouter Client", "cyan"))
# Initialize OpenAI client with OpenRouter base URL
openai_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY")  # Make sure to set this environment variable
)

# Create dedicated run directory
RUN_BASE_DIR = os.path.join("runs", "grok_ml_scientist")
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
RUN_DIR = os.path.join(RUN_BASE_DIR, timestamp)
OLDER_SOLUTIONS_DIR = os.path.join(RUN_DIR, "older_solutions")
os.makedirs(OLDER_SOLUTIONS_DIR, exist_ok=True)

# Clear execution outputs file at start (within run directory)
output_file = os.path.join(RUN_DIR, "execution_outputs.txt")
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(f"=== New Run Started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n\n")
print(colored(f"Created run directory at {RUN_DIR}", "green"))

class TimeoutException(Exception):
    pass

def run_with_timeout(cmd, timeout_minutes, working_dir=None):
    """Run command with timeout"""
    start_time = datetime.now()
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=working_dir
    )
    try:
        stdout, stderr = process.communicate(timeout=timeout_minutes * 60)
        execution_time = (datetime.now() - start_time).total_seconds()
        return stdout, stderr, process.returncode, execution_time
    except subprocess.TimeoutExpired:
        process.kill()
        return "", "Execution timed out after {} minutes".format(timeout_minutes), -1, timeout_minutes * 60

def get_timeout_improvement(code, train_sample, additional_info, execution_time, max_runtime):
    """Get improvements from Grok via OpenRouter for timeout issues"""
    print(colored("Getting performance improvement suggestions...", "yellow"))
    try:
        # Format solution history for context
        solution_history_text = "\n\nPrevious solutions and their performance:\n"
        for idx, (prev_code, prev_progress) in enumerate(solution_history, 1):
            solution_history_text += f"\nSolution {idx} Progress:\n{json.dumps(prev_progress, indent=2)}\n"
            solution_history_text += f"\nSolution {idx} Code:\n```python\n{prev_code}\n```\n"

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_OPTIMIZE},
            {"role": "user", "content": f"""The machine learning code is taking too long to execute. It ran for {execution_time:.2f} seconds but needs to complete within {max_runtime * 60} seconds.
IMPORTANT: Optimize runtime while maintaining accuracy. Consider:
1. Use GPU-accelerated LightGBM/CatBoost with early stopping and fewer iterations
2. Prefer 3-fold CV under tight budgets; keep leakage prevention
3. Vectorize preprocessing; avoid repeated DataFrame copies
4. Simplify feature set if necessary but keep key signals
5. Keep the same outputs: progress_report.json and submission.csv

Training data sample:
{train_sample}

Additional info:
{additional_info}

{solution_history_text}

Current code:
```python
{code}

{OPTIONAL_INSTRUCTIONS}
```

Return ONLY the complete optimized code wrapped in ```python and ``` markers."""}
        ]

        response = openai_client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=messages,
            reasoning_effort=IMPROVEMENT_EFFORT
        )

        return response.choices[0].message.content
    except Exception as e:
        print(colored(f"Error getting timeout improvements: {str(e)}", "red"))
        return None

def is_actual_error(stderr_text):
    """Check if stderr contains actual errors and not just warnings"""
    error_indicators = [
        "Traceback (most recent call last)",
        "Error:",
        "Exception:",
        "SyntaxError:",
        "NameError:",
        "TypeError:",
        "ValueError:",
        "ImportError:",
        "ModuleNotFoundError:",
        "IndexError:",
        "KeyError:",
        "AttributeError:",
        "IndentationError:"
    ]
    return any(indicator in stderr_text for indicator in error_indicators)

def get_gpt5_fix(error_message, code, train_sample, additional_info):
    """Get code fix from Grok via OpenRouter for the error"""
    print(colored("Getting Grok fix via OpenRouter...", "yellow"))
    try:
        # Get the last 5000 characters of the error message
        truncated_error = error_message[-5000:] if len(error_message) > 5000 else error_message
        if len(error_message) > 5000:
            truncated_error = "...(earlier error output truncated)...\n" + truncated_error

        # Format error history for context
        error_history_text = "\n\nPrevious errors encountered:\n"
        for idx, prev_error in enumerate(error_history, 1):
            error_history_text += f"\nError {idx}:\n{prev_error}\n"

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_FIX},
            {
                "role": "user",
                "content": f"""Fix this Python code error. Return ONLY the complete fixed code wrapped in ```python and ``` markers.
If there are missing imports (ModuleNotFoundError or ImportError), add pip install commands at the start using subprocess.check_call but keep the ML logic unchanged otherwise.
Ensure GPU availability checks (when frameworks apply) and leakage-safe preprocessing.

Training data sample:
{train_sample}

Additional info:
{additional_info}

Current Error:
{truncated_error}
{error_history_text}

Code:
{code}"""
            }
        ]

        response = openai_client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=messages,
            reasoning_effort=IMPROVEMENT_EFFORT
        )
        fixed_code = response.choices[0].message.content
        if not fixed_code or not fixed_code.strip().startswith("```python") or not fixed_code.strip().endswith("```"):
            print(colored("Warning: Grok response is not properly formatted with code blocks", "red"))
            return None
        return fixed_code
    except Exception as e:
        print(colored(f"Error getting Grok fix: {str(e)}", "red"))
        return None

print(colored("Phase 2: Data Loading and Preparation", "cyan"))
# Read the first 10 rows of train.csv
train_data = pd.read_csv('train.csv', nrows=10)
train_sample = train_data.to_string(index=False)

# Read additional info
with open('additional_info.txt', 'r', encoding='utf-8') as file:
    additional_info = file.read()

# Copy required data files into the run directory so the generated script can run with RUN_DIR as CWD
for data_file in ["train.csv", "test.csv", "sample_submission.csv", "additional_info.txt"]:
    if os.path.exists(data_file):
        try:
            shutil.copy2(data_file, os.path.join(RUN_DIR, os.path.basename(data_file)))
        except Exception as copy_err:
            print(colored(f"Warning: Could not copy {data_file} into run directory: {copy_err}", "yellow"))

print(colored("Phase 3: ML Solution Generation and Execution", "cyan"))
previous_code = ""
output_file = "execution_outputs.txt"

for i in range(ITERATIONS):
    print(colored(f"Iteration {i+1}/{ITERATIONS}", "yellow"))

    # Move old solution, progress report, and submission to older_solutions folder (within run directory)
    if i > 0:
        older_solutions_dir = OLDER_SOLUTIONS_DIR
        os.makedirs(older_solutions_dir, exist_ok=True)

        # Move files with iteration number
        files_to_move = {
            os.path.join(RUN_DIR, "solution.py"): f"solution_{i}.py",
            os.path.join(RUN_DIR, "progress_report.json"): f"progress_report_{i}.json",
            os.path.join(RUN_DIR, "submission.csv"): f"submission_{i}.csv"
        }

        for src, dst in files_to_move.items():
            if os.path.exists(src):
                shutil.move(src, os.path.join(older_solutions_dir, dst))
                print(colored(f"Moved {os.path.basename(src)} to {older_solutions_dir}/{dst}", "green"))

    initial_prompt = f"""You are an expert ML scientist. Write a COMPLETE, runnable Python script to solve the supervised ML challenge.
Rules:
1) Return ONLY a single code block fenced with ```python and ```.
2) Include all imports and utilities; no external explanations.
3) Auto-detect task type (classification vs regression) from the target.
4) Perform leakage-safe preprocessing: impute, encode categoricals, scale if needed, fit transforms inside CV folds only.
5) Use robust models: prefer LightGBM/CatBoost (GPU if available), else XGBoost/RandomForest/LogReg.
6) Use 5-fold CV (Stratified for classification). If time is tight, fall back to 3-fold. Use a fixed seed.
7) Use early stopping for boosting models. Cap iterations to fit in {MAX_RUNTIME_MINUTES} minutes.
8) Metrics: classification=accuracy (+F1/AUC if imbalanced); regression=RMSE and MAE. Print per-fold and overall mean/std.
9) Engineer simple, high-signal features: ratios, counts, interactions (guard with variance checks). Avoid heavy, slow features.
10) Save outputs (UTF-8): progress_report.json and submission.csv.
11) progress_report.json must include: best_model, cv_scores, mean_cv, std_cv, validation_scheme, features_used, feature_importances (top 30 if available), training_time_seconds, oof_score (if available), notes.
12) Print whether GPU or CPU is used.

Challenge information:
{additional_info}

First 10 rows of training data:
{train_sample}

Data files available: train.csv and test.csv. Pay attention to column names.

{OPTIONAL_INSTRUCTIONS}

Return ONLY the complete code solution wrapped in ```python and ``` markers."""

    if i == 0:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT_MAIN},
            {"role": "user", "content": initial_prompt}
        ]
    else:
        # Read the previous progress report if present
        older_solutions_dir = OLDER_SOLUTIONS_DIR
        prev_progress_path = os.path.join(older_solutions_dir, f"progress_report_{i}.json")
        prev_progress = None
        if os.path.exists(prev_progress_path):
            try:
                with open(prev_progress_path, 'r', encoding='utf-8') as f:
                    prev_progress = json.load(f)
            except Exception as read_err:
                print(colored(f"Warning: Could not read previous progress report: {read_err}", "yellow"))

        # Format solution history for context
        solution_history_text = "\n\nPrevious solutions and their performance:\n"
        for idx, (prev_code, prev_prog) in enumerate(solution_history, 1):
            solution_history_text += f"\nSolution {idx} Progress:\n{json.dumps(prev_prog, indent=2)}\n"
            solution_history_text += f"\nSolution {idx} Code:\n```python\n{prev_code}\n```\n"

        if prev_progress is not None:
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT_MAIN},
                {"role": "user", "content": initial_prompt},
                {"role": "assistant", "content": f"Here's the previous code I generated:\n\n```python\n{previous_code}\n```"},
                {"role": "user", "content": f"""Improve this code based on the previous results. Your goal is to maximize generalization performance under the time budget. Return ONLY the complete improved code wrapped in ```python and ``` markers.
Maintain GPU checks and leakage-safe CV. Keep output contracts (progress_report.json, submission.csv).

Training data sample:
{train_sample}

Additional information:
{additional_info}

{solution_history_text}

Previous model performance:
{json.dumps(prev_progress, indent=2)}
"""}
            ]
        else:
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT_MAIN},
                {"role": "user", "content": initial_prompt},
                {"role": "assistant", "content": f"Here's the previous code I generated:\n\n```python\n{previous_code}\n```"},
                {"role": "user", "content": f"""Improve this code based on the previous results. Your goal is to maximize generalization performance under the time budget. Return ONLY the complete improved code wrapped in ```python and ``` markers.
Maintain GPU checks and leakage-safe CV. Keep output contracts (progress_report.json, submission.csv).

Training data sample:
{train_sample}

Additional information:
{additional_info}

{solution_history_text}
"""}
            ]

    response = openai_client.chat.completions.create(
        model=OPENROUTER_MODEL,
        messages=messages,
        reasoning_effort=IMPROVEMENT_EFFORT
    )

    print(colored("ML Scientist's Solution:", "cyan"))
    solution_content = response.choices[0].message.content
    print(solution_content)

    code_blocks = re.findall(r'```python(.*?)```', solution_content, re.DOTALL)
    if not code_blocks:
        print(colored("Error: No properly formatted Python code blocks found in the solution.", "red"))
        print(colored("Raw response:", "yellow"))
        print(solution_content)
        break

    current_code = '\n'.join(code_blocks).strip()
    has_error = True

    while has_error:  # Keep trying with Grok until no errors
        with open(os.path.join(RUN_DIR, 'solution.py'), 'w', encoding='utf-8') as file:
            file.write(current_code)
        print(colored(f"Solution saved to {os.path.join(RUN_DIR, 'solution.py')}", "green"))

        # Execute the generated code with timeout
        print(colored("Executing generated code:", "cyan"))
        stdout, stderr, returncode, execution_time = run_with_timeout(
            ['python', 'solution.py'],
            MAX_RUNTIME_MINUTES,
            working_dir=RUN_DIR
        )

        print(colored("Execution output:", "green"))
        print(stdout)

        if returncode == -1:  # Timeout occurred
            print(colored(f"Execution timed out after {MAX_RUNTIME_MINUTES} minutes", "red"))

            # Get optimization suggestions from Grok via OpenRouter
            optimized_code = get_timeout_improvement(
                current_code,
                train_sample,
                additional_info,
                execution_time,
                MAX_RUNTIME_MINUTES
            )

            if optimized_code and "```python" in optimized_code:
                code_blocks = re.findall(r'```python(.*?)```', optimized_code, re.DOTALL)
                if code_blocks:
                    current_code = code_blocks[0].strip()
                    print(colored("Applied performance optimizations. Retrying...", "green"))
                    continue
                else:
                    print(colored("Error: Optimization response was not properly formatted", "red"))
                    break
            else:
                print(colored("Could not get optimization suggestions. Moving to next iteration.", "red"))
                break

        if stderr:
            # Check if stderr contains actual errors or just warnings
            if is_actual_error(stderr):
                print(colored("Execution errors:", "red"))
                print(stderr)

                # Add current error to history
                error_history.append(stderr)

                # Try to get fix from Grok via OpenRouter
                fixed_code = get_gpt5_fix(stderr, current_code, train_sample, additional_info)

                if fixed_code and "```python" in fixed_code:
                    # Extract code from markdown if present
                    code_blocks = re.findall(r'```python(.*?)```', fixed_code, re.DOTALL)
                    if code_blocks:
                        current_code = code_blocks[0].strip()
                        print(colored("Applied Grok fix. Retrying...", "green"))
                    else:
                        print(colored("Error: Grok fix was not properly formatted", "red"))
                        break
                else:
                    print(colored("Could not get fix from Grok. Moving to next iteration.", "red"))
                    break
            else:
                print(colored("Warnings (non-critical):", "yellow"))
                print(stderr)
                has_error = False  # Continue if only warnings
        else:
            has_error = False  # No errors or warnings

        # Save execution output to file
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(f"Iteration {i+1}/{ITERATIONS}\n")
            f.write("Execution output:\n")
            f.write(stdout)
            f.write("\nExecution errors:\n")
            f.write(stderr)
            if returncode == -1:
                f.write(f"\nExecution timed out after {MAX_RUNTIME_MINUTES} minutes")
            f.write("\n" + "="*50 + "\n\n")

        # If execution was successful, add to solution history
        if not has_error and returncode != -1:
            try:
                with open(os.path.join(RUN_DIR, 'progress_report.json'), 'r', encoding='utf-8') as f:
                    current_progress = json.load(f)
                solution_history.append((current_code, current_progress))
                print(colored("Added current solution to history", "green"))
            except Exception as e:
                print(colored(f"Warning: Could not add solution to history: {str(e)}", "yellow"))

    # Update previous_code for the next iteration (Grok improvements)
    previous_code = current_code

print(colored("ML Scientist process completed.", "cyan"))
print(f"All execution outputs have been saved to {output_file}")
print(colored(f"All solutions, progress reports, and submissions have been saved inside {RUN_DIR} with iteration numbers in the older_solutions subdirectory.", "green"))

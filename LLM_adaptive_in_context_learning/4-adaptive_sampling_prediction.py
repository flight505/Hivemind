import os
import pandas as pd
import json
import datetime
import matplotlib.pyplot as plt
from openai import OpenAI
from termcolor import colored
import random

# IMPORTANT VARIABLES (ALL CAPS AS REQUESTED)
USE_OPENAI_OR_OPENROUTER = "OPENAI"  # Options: "OPENAI" or "OPENROUTER"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-5-mini"
REASONING_EFFORT = "high"
CSV_FILE_PATH = "complex_dataset.csv"
TRAINING_ROWS = 50  # Number of rows sampled per iteration for training
VALIDATION_ROWS = 50  # Fixed held-out validation size (never enters sampling)
ACCURACY_THRESHOLD = 0.99  # Stop when accuracy reaches this level
MAX_ITERATIONS = 50  # Maximum attempts to reach threshold
MAX_RETRIES = 3  # Maximum retries for parsing/API failures
OUTPUT_FOLDER = f"adaptive_sampling_results_{MODEL_NAME}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
STRATIFIED_SAMPLING_BASE_SEED = random.randint(1, 1000000)  # Base seed for per-iteration stratified sampling
VALIDATION_SPLIT_SEED = random.randint(1, 1000000)  # Seed for fixed validation holdout
ROLLING_AVERAGE_WINDOW = 5  # Number of iterations to include in rolling average curve


def setup_client():
    """Set up OpenAI client for either provider"""
    try:
        if USE_OPENAI_OR_OPENROUTER.upper() == "OPENROUTER":
            client = OpenAI(api_key=OPENROUTER_API_KEY, base_url="https://openrouter.ai/api/v1")
            print(colored("✓ Connected to OpenRouter", "green"))
        elif USE_OPENAI_OR_OPENROUTER.upper() == "OPENAI":
            client = OpenAI(api_key=OPENAI_API_KEY)
            print(colored("✓ Connected to OpenAI", "green"))
        else:
            print(colored("❌ Invalid provider setting", "red"))
            return None
        return client
    except Exception as e:
        print(colored(f"❌ Client setup failed: {e}", "red"))
        return None


def call_llm(client, messages, response_format=None, reasoning_effort=None):
    """Make API call to LLM with retry mechanism"""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            params = {"model": MODEL_NAME, "messages": messages}
            if response_format:
                params["response_format"] = response_format
            if reasoning_effort and USE_OPENAI_OR_OPENROUTER.upper() == "OPENROUTER":
                params["reasoning_effort"] = reasoning_effort

            response = client.chat.completions.create(**params)
            return response.choices[0].message.content

        except Exception as e:
            print(colored(f"⚠️ API call attempt {attempt} failed: {e}", "yellow"))
            if attempt < MAX_RETRIES:
                print(colored("   Retrying API call...", "cyan"))
                import time
                time.sleep(2)
            else:
                print(colored(f"❌ API call failed after {MAX_RETRIES} attempts", "red"))
                return None

    return None


def create_fixed_validation_split(df: pd.DataFrame):
    """Create a fixed held-out validation set via stratified sampling by Output (1-4)."""
    try:
        class_counts = df["Output"].value_counts(dropna=False)
        if len(class_counts) < 2:
            print(colored("⚠️ Stratification not possible (single class) - taking head for validation", "yellow"))
            validation_df = df.sample(n=min(VALIDATION_ROWS, len(df)), random_state=VALIDATION_SPLIT_SEED)
            pool_df = df.drop(validation_df.index)
            validation_df = validation_df.reset_index(drop=True)
            pool_df = pool_df.reset_index(drop=True)
            return pool_df, validation_df

        # Calculate proportional allocation for each class (1-4)
        total = len(df)
        class_props = {}
        for class_val in range(1, 5):  # Classes 1, 2, 3, 4
            class_props[class_val] = class_counts.get(class_val, 0) / total if total > 0 else 0

        # Calculate desired counts per class
        desired_counts = {}
        total_desired = 0
        for class_val in range(1, 5):
            desired_counts[class_val] = int(round(VALIDATION_ROWS * class_props[class_val]))
            total_desired += desired_counts[class_val]

        # Adjust for rounding errors
        remaining = VALIDATION_ROWS - total_desired
        if remaining != 0:
            # Add/subtract from the largest class
            largest_class = max(class_props.keys(), key=lambda k: class_props[k])
            desired_counts[largest_class] += remaining

        # Sample from each class
        samples = []
        for class_val in range(1, 5):
            class_df = df[df["Output"] == class_val]
            n_take = min(len(class_df), desired_counts[class_val])
            if n_take > 0:
                class_sample = class_df.sample(n=n_take, random_state=VALIDATION_SPLIT_SEED)
                samples.append(class_sample)

        if samples:
            validation_df = pd.concat(samples).sample(frac=1, random_state=VALIDATION_SPLIT_SEED).reset_index(drop=True)
            pool_df = df.drop(validation_df.index).reset_index(drop=True)
            return pool_df, validation_df
        else:
            # Fallback
            validation_df = df.sample(n=min(VALIDATION_ROWS, len(df)), random_state=VALIDATION_SPLIT_SEED)
            pool_df = df.drop(validation_df.index)
            validation_df = validation_df.reset_index(drop=True)
            pool_df = pool_df.reset_index(drop=True)
            return pool_df, validation_df

    except Exception as e:
        print(colored(f"⚠️ Failed to create validation split: {e}", "yellow"))
        return df, pd.DataFrame(columns=df.columns)


def stratified_sample(df_pool: pd.DataFrame, n_total: int, seed: int) -> pd.DataFrame:
    """Sample n_total rows from df_pool stratified by Output (1-4) with seed."""
    try:
        class_counts = df_pool["Output"].value_counts(dropna=False)
        if len(class_counts) < 2:
            return df_pool.sample(n=min(n_total, len(df_pool)), random_state=seed).reset_index(drop=True)

        # Calculate proportional allocation for each class (1-4)
        total = len(df_pool)
        class_props = {}
        for class_val in range(1, 5):  # Classes 1, 2, 3, 4
            class_props[class_val] = class_counts.get(class_val, 0) / total if total > 0 else 0

        # Calculate desired counts per class
        desired_counts = {}
        total_desired = 0
        for class_val in range(1, 5):
            desired_counts[class_val] = int(round(n_total * class_props[class_val]))
            total_desired += desired_counts[class_val]

        # Adjust for rounding errors
        remaining = n_total - total_desired
        if remaining != 0:
            # Add/subtract from the largest class
            largest_class = max(class_props.keys(), key=lambda k: class_props[k])
            desired_counts[largest_class] += remaining

        # Sample from each class
        samples = []
        for class_val in range(1, 5):
            class_df = df_pool[df_pool["Output"] == class_val]
            n_take = min(len(class_df), desired_counts[class_val])
            if n_take > 0:
                class_sample = class_df.sample(n=n_take, random_state=seed)
                samples.append(class_sample)

        if samples:
            sample_df = pd.concat(samples).sample(frac=1, random_state=seed).reset_index(drop=True)
            return sample_df
        else:
            # Fallback
            return df_pool.sample(n=min(n_total, len(df_pool)), random_state=seed).reset_index(drop=True)

    except Exception as e:
        print(colored(f"⚠️ Stratified sampling failed: {e}", "yellow"))
        return df_pool.sample(n=min(n_total, len(df_pool)), random_state=seed).reset_index(drop=True)


def generate_rules(client, training_data):
    """Generate predictive rules from training data with retry mechanism"""
    print(colored(f"\n🧠 Generating rules from {len(training_data)} training rows...", "blue"))

    data_summary = training_data.to_string(index=False)

    prompt = f"""
    Analyze this complex interdependent dataset and create GENERAL predictive rules for output classification (1-4):

    TRAINING DATA:
    {data_summary}

    CRITICAL: Create GENERAL PATTERN-BASED rules that will work for ANY input combination, not just the ones in this training data.
    This dataset has COMPLEX INTERDEPENDENT relationships where ALL 5 features (A, B, C, D, E) must be considered together.

    RULES MUST BE BASED ON:
    - Interdependent relationships between ALL features (A, B, C, D, E)
    - Mathematical combinations (sums, products, ratios)
    - Threshold patterns across multiple features
    - Conditional logic involving all 5 inputs
    - Complex interactions that cannot be captured by single-feature rules

    Create GENERAL rules that require considering ALL 5 features simultaneously to predict the output class (1-4).

    Return ONLY the rules in this exact format:
    PREDICTIVE RULES:

    1. [General rule requiring multiple features for class 1]
    2. [General rule requiring multiple features for class 2]
    3. [General rule requiring multiple features for class 3]
    4. [General rule requiring multiple features for class 4]
    [Continue with as many GENERAL interdependent rules as needed]

    Do not include any explanations, analysis, or discussion. Only GENERAL rules requiring ALL features.
    """

    messages = [
        {"role": "system", "content": "You are an expert predictive model that creates GENERAL rules for complex interdependent datasets, not memorizes specific cases. Never create index-specific rules. Focus on patterns requiring ALL 5 features (A, B, C, D, E) simultaneously. Return ONLY general pattern-based rules."},
        {"role": "user", "content": prompt}
    ]

    for attempt in range(1, MAX_RETRIES + 1):
        print(colored(f"   Attempt {attempt}/{MAX_RETRIES}...", "cyan"))

        rules = call_llm(client, messages, reasoning_effort=REASONING_EFFORT)

        if rules and "PREDICTIVE RULES:" in rules.upper():
            print(colored("✓ Rules generated successfully", "green"))
            return rules
        else:
            print(colored(f"⚠️ Attempt {attempt} failed - invalid or missing rules format", "yellow"))
            if attempt < MAX_RETRIES:
                print(colored("   Retrying...", "cyan"))
                import time
                time.sleep(1)
            else:
                print(colored(f"❌ Failed to generate valid rules after {MAX_RETRIES} attempts", "red"))
                return None

    return None


def predict_batch(client, rules, test_data):
    """Predict all test rows in one API call with retry mechanism"""
    print(colored(f"\n🔮 Predicting {len(test_data)} data points...", "blue"))

    # Add row index as identifier since we don't have PassengerId
    test_data_with_index = test_data.copy()
    test_data_with_index['RowIndex'] = test_data.index

    # Remove Output column for prediction (we don't want to give the LLM the labels!)
    if 'Output' in test_data_with_index.columns:
        test_data_with_index = test_data_with_index.drop('Output', axis=1)

    prediction_data = test_data_with_index.to_string(index=False)

    prompt = f"""
    You are a predictive system that must return predictions in PERFECT structured text format.

    PREDICTIVE RULES TO USE:
    {rules}

    DATA TO PREDICT (predict for ALL {len(test_data)} rows):
    {prediction_data}

    CRITICAL REQUIREMENTS:
    1. Return predictions for ALL {len(test_data)} rows by their RowIndex
    2. Each prediction must be a class number: 1, 2, 3, or 4 (integer values only)
    3. Return ONLY the structured predictions - no extra text, no explanations

    REQUIRED OUTPUT FORMAT:
    PREDICTIONS:
    0: 1
    1: 2
    2: 3
    [Continue with ALL {len(test_data)} predictions in this exact format]

    Example for 3 rows:
    PREDICTIONS:
    0: 1
    1: 2
    2: 4

    Make sure to include EXACTLY {len(test_data)} predictions with the correct RowIndex from the data above.
    Each line must be in format: ROWINDEX: PREDICTION
    """

    messages = [
        {"role": "system", "content": "You are a precise predictive system for complex interdependent classification. Return ONLY structured predictions in the exact format requested for classes 1-4. No extra text or explanations."},
        {"role": "user", "content": prompt}
    ]

    for attempt in range(1, MAX_RETRIES + 1):
        print(colored(f"   Attempt {attempt}/{MAX_RETRIES}...", "cyan"))

        response = call_llm(client, messages)

        if response:
            try:
                import re

                predictions_dict = {}

                predictions_match = re.search(r'PREDICTIONS:\s*(.+)', response, re.DOTALL | re.IGNORECASE)
                if not predictions_match:
                    print(colored(f"⚠️ Attempt {attempt} failed - Could not find PREDICTIONS section", "yellow"))
                    if attempt < MAX_RETRIES:
                        print(colored("   Retrying...", "cyan"))
                        import time
                        time.sleep(1)
                        continue
                    else:
                        print(colored(f"❌ Failed to get valid predictions after {MAX_RETRIES} attempts", "red"))
                        return None

                predictions_text = predictions_match.group(1)

                lines = predictions_text.strip().split('\n')
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue

                    match = re.match(r'^([^:]+):\s*([1-4])$', line)
                    if match:
                        row_index_str = match.group(1).strip()
                        prediction_str = match.group(2).strip()

                        try:
                            row_index = int(row_index_str)
                            prediction_class = int(prediction_str)

                            if prediction_class not in [1, 2, 3, 4]:
                                print(colored(f"⚠️ Attempt {attempt} failed - Invalid prediction class '{prediction_str}' for row {row_index}", "yellow"))
                                if attempt < MAX_RETRIES:
                                    print(colored("   Retrying...", "cyan"))
                                    import time
                                    time.sleep(1)
                                    break
                                else:
                                    return None

                            predictions_dict[row_index] = prediction_class
                        except ValueError:
                            print(colored(f"⚠️ Attempt {attempt} failed - Invalid row index '{row_index_str}'", "yellow"))
                            if attempt < MAX_RETRIES:
                                print(colored("   Retrying...", "cyan"))
                                import time
                                time.sleep(1)
                                break
                            else:
                                return None
                    else:
                        continue
                else:
                    expected_indices = set(test_data.index.tolist())
                    received_indices = set(predictions_dict.keys())

                    if len(predictions_dict) == 0:
                        print(colored(f"⚠️ Attempt {attempt} failed - No valid predictions found", "yellow"))
                        if attempt < MAX_RETRIES:
                            print(colored("   Retrying...", "cyan"))
                            import time
                            time.sleep(1)
                            continue
                        else:
                            return None

                    if expected_indices != received_indices:
                        missing = expected_indices - received_indices
                        if missing:
                            print(colored(f"⚠️ Attempt {attempt} failed - Missing predictions for rows: {list(missing)}", "yellow"))
                            print(colored(f"Expected {len(expected_indices)} predictions, got {len(predictions_dict)}", "yellow"))
                            if attempt < MAX_RETRIES:
                                print(colored("   Retrying...", "cyan"))
                                import time
                                time.sleep(1)
                                continue
                            else:
                                return None

                    print(colored(f"✓ Got {len(predictions_dict)} validated index-based predictions", "green"))
                    return predictions_dict

                if attempt >= MAX_RETRIES:
                    print(colored(f"❌ Failed to get valid predictions after {MAX_RETRIES} attempts", "red"))
                    return None

            except Exception as e:
                print(colored(f"⚠️ Attempt {attempt} failed - Parse error: {e}", "yellow"))
                if attempt < MAX_RETRIES:
                    print(colored("   Retrying...", "cyan"))
                    import time
                    time.sleep(1)
                    continue
                else:
                    print(colored(f"❌ Failed to parse predictions after {MAX_RETRIES} attempts", "red"))
                    return None
        else:
            print(colored(f"⚠️ Attempt {attempt} failed - No response from API", "yellow"))
            if attempt < MAX_RETRIES:
                print(colored("   Retrying...", "cyan"))
                import time
                time.sleep(1)
                continue
            else:
                print(colored(f"❌ Failed to get API response after {MAX_RETRIES} attempts", "red"))
                return None

    print(colored(f"❌ All {MAX_RETRIES} prediction attempts failed", "red"))
    return None


def calculate_accuracy(predictions_dict, data_with_labels):
    """Calculate prediction accuracy using index-based matching"""
    if not isinstance(predictions_dict, dict):
        print(colored("❌ Predictions must be a dictionary", "red"))
        return 0.0

    actual_dict = {}
    for idx, row in data_with_labels.iterrows():
        actual_dict[idx] = row['Output']

    if len(predictions_dict) != len(actual_dict):
        print(colored(f"❌ Prediction/actual count mismatch: {len(predictions_dict)} vs {len(actual_dict)}", "red"))
        return 0.0

    correct = 0
    total = 0
    for row_index, predicted in predictions_dict.items():
        if row_index in actual_dict:
            actual = actual_dict[row_index]
            if predicted == actual:
                correct += 1
            total += 1
        else:
            print(colored(f"⚠️ No actual value found for row {row_index}", "yellow"))

    if total == 0:
        print(colored("❌ No matching predictions found", "red"))
        return 0.0

    accuracy = correct / total
    print(colored(f"📊 Accuracy: {accuracy:.1%} ({correct}/{total})", "cyan"))
    return accuracy


def adjust_rules(client, current_rules, training_data, predictions_dict, actual_values_dict):
    """Adjust rules based on prediction errors with retry mechanism"""
    print(colored("\n🔧 Adjusting rules based on errors...", "yellow"))

    formatted_data_rows = []

    for i, row in training_data.iterrows():
        row_index = row.name  # Use DataFrame index
        actual = actual_values_dict.get(row_index)
        predicted = predictions_dict.get(row_index)

        if predicted is None:
            formatted_row = f"""❓ MISSING PREDICTION ROW {i+1} ❓
Row Index: {row_index}
Actual: {actual}
{row.to_string()}
{'─' * 80}"""
        else:
            is_error = predicted != actual

            if is_error:
                formatted_row = f"""🚨 ERROR ROW {i+1} 🚨
Row Index: {row_index}
Predicted: {predicted} | Actual: {actual}
{row.to_string()}
{'─' * 80}"""
            else:
                formatted_row = f"""✅ CORRECT ROW {i+1}
Row Index: {row_index}
Predicted: {predicted} | Actual: {actual}
{row.to_string()}"""

        formatted_data_rows.append(formatted_row)

    formatted_training_data = "\n\n".join(formatted_data_rows)

    error_count = 0
    total_predictions = 0

    for row_index, predicted in predictions_dict.items():
        if row_index in actual_values_dict:
            actual = actual_values_dict[row_index]
            if predicted != actual:
                error_count += 1
            total_predictions += 1

    accuracy = (total_predictions - error_count) / total_predictions if total_predictions > 0 else 0

    prompt = f"""
    Current rules achieved {accuracy:.1%} accuracy.
    {error_count} prediction errors need to be fixed.

    CURRENT RULES:
    {current_rules}

    TRAINING DATA WITH ERRORS:
    {formatted_training_data}

    CRITICAL: Create GENERAL PATTERN-BASED rules that will work for ANY input combination, not just memorizing these specific cases.
    This dataset has COMPLEX INTERDEPENDENT relationships where ALL 5 features (A, B, C, D, E) must be considered together.

    RULES MUST BE BASED ON GENERAL PATTERNS:
    - Interdependent relationships between ALL features (A, B, C, D, E)
    - Mathematical combinations (sums, products, ratios) involving all features
    - Threshold patterns across multiple features simultaneously
    - Conditional logic requiring all 5 inputs together
    - Complex interactions that cannot be captured by single-feature rules

    FORBIDDEN: Do NOT memorize specific row indices or create index-specific rules.
    FORBIDDEN: Do NOT create rules like "If row 0 has A=50 then predict 1"
    FORBIDDEN: Do NOT create rules based on exact matches to training data.
    FORBIDDEN: Do NOT create simple rules based on individual features alone.

    Create GENERAL rules that identify COMPLEX PATTERNS in the error data and correct them for ALL similar cases, requiring ALL 5 features to be considered together.

    Return ONLY the improved GENERAL rules in this exact format:
    IMPROVED PREDICTIVE RULES:

    1. [General rule based on error patterns and corrections]
    2. [General rule addressing common error causes]
    3. [General rule for demographic corrections]
    [Continue with as many GENERAL rules as needed]

    Do not include any explanations, analysis, or discussion. Only GENERAL rules.
    """

    messages = [
        {"role": "system", "content": "You are an expert predictive model that creates GENERAL rules for complex interdependent datasets, not memorizes specific cases. Never create index-specific rules. Focus on COMPLEX PATTERNS requiring ALL 5 features that fix errors for ALL similar cases."},
        {"role": "user", "content": prompt}
    ]

    for attempt in range(1, MAX_RETRIES + 1):
        print(colored(f"   Attempt {attempt}/{MAX_RETRIES}...", "cyan"))

        new_rules = call_llm(client, messages, reasoning_effort=REASONING_EFFORT)

        if new_rules and "IMPROVED PREDICTIVE RULES:" in new_rules.upper():
            print(colored("✓ Rules adjusted successfully", "green"))
            return new_rules
        else:
            print(colored(f"⚠️ Attempt {attempt} failed - invalid or missing rules format", "yellow"))
            if attempt < MAX_RETRIES:
                print(colored("   Retrying...", "cyan"))
                import time
                time.sleep(1)
            else:
                print(colored(f"❌ Failed to adjust rules after {MAX_RETRIES} attempts", "red"))
                return None

    return None


def save_rules_to_file(rules, iteration, is_initial=False):
    """Save rules to a timestamped txt file"""
    try:
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

        if is_initial:
            filename = f"{OUTPUT_FOLDER}/initial_rules.txt"
        else:
            timestamp = datetime.datetime.now().strftime("%H%M%S")
            filename = f"{OUTPUT_FOLDER}/rules_iteration_{iteration}_{timestamp}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"PREDICTIVE RULES - {'INITIAL' if is_initial else f'ITERATION {iteration}'}\n")
            f.write("=" * 60 + "\n\n")
            f.write(rules)
            f.write("\n\n" + "=" * 60)

        print(colored(f"📁 Rules saved: {filename}", "cyan"))
        return filename

    except Exception as e:
        print(colored(f"⚠️ Failed to save rules: {e}", "yellow"))
        return None


def save_metrics_to_json(iteration, accuracy, best_accuracy, timestamp):
    """Save accuracy metrics to JSON file"""
    try:
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        metrics_file = f"{OUTPUT_FOLDER}/accuracy_metrics.json"

        if os.path.exists(metrics_file):
            with open(metrics_file, 'r', encoding='utf-8') as f:
                metrics_data = json.load(f)
        else:
            metrics_data = {
                "training_rows": TRAINING_ROWS,
                "validation_rows": VALIDATION_ROWS,
                "accuracy_threshold": ACCURACY_THRESHOLD,
                "max_iterations": MAX_ITERATIONS,
                "iterations": []
            }

        iteration_data = {
            "iteration": iteration,
            "accuracy": round(accuracy, 4),
            "best_accuracy": round(best_accuracy, 4),
            "timestamp": timestamp,
            "above_threshold": accuracy >= ACCURACY_THRESHOLD
        }

        metrics_data["iterations"].append(iteration_data)

        with open(metrics_file, 'w', encoding='utf-8') as f:
            json.dump(metrics_data, f, indent=2, ensure_ascii=False)

        print(colored(f"📊 Metrics saved: {metrics_file}", "cyan"))
        return metrics_data

    except Exception as e:
        print(colored(f"⚠️ Failed to save metrics: {e}", "yellow"))
        return None


def save_best_rules(best_rules, best_accuracy, best_iteration):
    """Save the best performing rules to a clearly named file"""
    try:
        if not best_rules:
            print(colored("⚠️ No rules to save", "yellow"))
            return None

        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

        accuracy_pct = int(best_accuracy * 100)
        filename = f"{OUTPUT_FOLDER}/best_rules_{accuracy_pct}pct_accuracy.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("BEST PREDICTIVE RULES\n")
            f.write("=" * 50 + "\n")
            f.write(f"Accuracy: {best_accuracy:.1%}\n")
            f.write(f"From Iteration: {best_iteration}\n")
            f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 50 + "\n\n")
            f.write(best_rules)
            f.write("\n\n" + "=" * 50)

        print(colored(f"🏆 Best rules saved: {filename}", "green"))
        print(colored(f"   Accuracy: {best_accuracy:.1%} (Iteration {best_iteration})", "green"))
        return filename

    except Exception as e:
        print(colored(f"⚠️ Failed to save best rules: {e}", "yellow"))
        return None


def plot_accuracy_progress(metrics_data):
    """Plot and save accuracy progress chart"""
    try:
        if not metrics_data or "iterations" not in metrics_data:
            return None

        iterations_data = metrics_data["iterations"]
        if not iterations_data:
            return None

        iterations = [item["iteration"] for item in iterations_data]
        accuracies = [item["accuracy"] for item in iterations_data]
        best_accuracies = [item["best_accuracy"] for item in iterations_data]

        plt.figure(figsize=(12, 8))

        training_iterations = []
        training_accuracies = []
        training_best_accuracies = []
        validation_points = []

        for item in iterations_data:
            if item.get("is_validation", False):
                validation_points.append((item.get("iteration"), item.get("accuracy")))
            else:
                training_iterations.append(item.get("iteration"))
                training_accuracies.append(item.get("accuracy"))
                training_best_accuracies.append(item.get("best_accuracy"))

        if training_iterations:
            plt.plot(training_iterations, training_accuracies, 'b-', linewidth=2, marker='o', markersize=6,
                    label='Training Current Accuracy', alpha=0.8)
            plt.plot(training_iterations, training_best_accuracies, 'r-', linewidth=2, marker='s', markersize=6,
                    label='Training Best Accuracy', alpha=0.8)

            # Add rolling average curve
            if len(training_accuracies) >= 3:
                window_size = min(ROLLING_AVERAGE_WINDOW, len(training_accuracies))
                rolling_avg = []
                for i in range(len(training_accuracies)):
                    start_idx = max(0, i - window_size + 1)
                    avg = sum(training_accuracies[start_idx:i+1]) / (i - start_idx + 1)
                    rolling_avg.append(avg)

                plt.plot(training_iterations, rolling_avg, 'purple', linewidth=3, linestyle='--',
                        label=f'Rolling Avg (last {window_size})', alpha=0.9)

        if validation_points:
            for (v_iter, v_acc) in validation_points:
                if v_iter is None or v_acc is None:
                    continue
                plt.plot([v_iter], [v_acc], 'g-', linewidth=3, marker='*', markersize=15,
                        label='Validation Accuracy' if (v_iter, v_acc) == validation_points[0] else None, alpha=1.0)
                plt.axvline(x=v_iter - 0.5, color='g', linestyle=':', linewidth=2, alpha=0.7)

        plt.axhline(y=ACCURACY_THRESHOLD, color='g', linestyle='--', linewidth=2,
                   label=f'Target ({ACCURACY_THRESHOLD:.0%})', alpha=0.7)

        plt.grid(True, alpha=0.3)
        plt.xlabel('Iteration', fontsize=12)
        plt.ylabel('Accuracy', fontsize=12)
        title = 'Adaptive Prediction Accuracy Progress (Sampling)'
        if validation_points:
            title += ' (with Validation)'
        plt.title(title, fontsize=14, fontweight='bold')
        plt.legend(loc='lower right', fontsize=10)

        plt.ylim(0, 1.0)
        plt.yticks([i/10 for i in range(11)], [f'{i*10}%' for i in range(11)])

        if training_accuracies:
            current_acc = training_accuracies[-1]
            best_acc = training_best_accuracies[-1]
            plt.text(0.02, 0.98, f'Training: {current_acc:.1%}',
                    transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
            plt.text(0.02, 0.90, f'Best: {best_acc:.1%}',
                    transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))

            if validation_points:
                last_val_acc = None
                for (_, v_acc) in validation_points:
                    last_val_acc = v_acc
                if last_val_acc is not None:
                    plt.text(0.02, 0.82, f'Validation: {last_val_acc:.1%}',
                            transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
                            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

        plot_filename = f"{OUTPUT_FOLDER}/accuracy_progress.png"
        plt.savefig(plot_filename, dpi=150, bbox_inches='tight')
        plt.close()

        print(colored(f"📈 Accuracy plot updated: {plot_filename}", "cyan"))
        return plot_filename

    except Exception as e:
        print(colored(f"⚠️ Failed to create accuracy plot: {e}", "yellow"))
        return None


def run_validation_phase(client, validation_df, best_rules, best_accuracy, current_iteration):
    """Run validation on the fixed held-out validation_df and persist metrics/plot."""
    try:
        if best_rules is None or validation_df is None or validation_df.empty:
            print(colored("⚠️ Skipping validation - no rules or validation set", "yellow"))
            return None

        print(colored(f"\n🧪 VALIDATION PHASE - Testing on {len(validation_df)} unseen rows...", "blue"))

        validation_predictions = predict_batch(client, best_rules, validation_df)
        if not validation_predictions:
            print(colored("❌ Validation failed - could not get predictions", "red"))
            return None

        validation_accuracy = calculate_accuracy(validation_predictions, validation_df)
        validation_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        validation_metrics_data = save_metrics_to_json(current_iteration + 1, validation_accuracy, best_accuracy, validation_timestamp)
        if validation_metrics_data and "iterations" in validation_metrics_data and validation_metrics_data["iterations"]:
            validation_metrics_data["iterations"][-1]["is_validation"] = True
            validation_metrics_data["iterations"][-1]["validation_gap"] = abs(validation_accuracy - best_accuracy)
            validation_metrics_data["validation_accuracy"] = validation_accuracy
            metrics_file = f"{OUTPUT_FOLDER}/accuracy_metrics.json"
            with open(metrics_file, 'w', encoding='utf-8') as f:
                json.dump(validation_metrics_data, f, indent=2, ensure_ascii=False)
            plot_accuracy_progress(validation_metrics_data)

        print(colored("\n🎯 VALIDATION RESULTS:", "green"))
        print(colored(f"   📊 Validation Accuracy: {validation_accuracy:.1%}", "yellow"))
        print(colored(f"   🎯 Training Best: {best_accuracy:.1%}", "cyan"))
        print(colored(f"   📈 Accuracy Gap: {abs(validation_accuracy - best_accuracy):.1%}", "magenta"))

        return validation_accuracy

    except Exception as e:
        print(colored(f"⚠️ Validation error: {e}", "yellow"))
        return None


def main():
    """Main prediction loop with per-iteration stratified sampling for complex interdependent dataset"""
    print(colored("🚀 Adaptive Sampling Prediction System for Complex Dataset", "cyan"))
    print(colored("🎯 Solving interdependent classification puzzle (A, B, C, D, E) -> Output (1-4)", "cyan"))
    print(colored(f"🎯 Target accuracy: {ACCURACY_THRESHOLD:.0%}", "cyan"))
    print(colored(f"📊 Train sample size per iteration: {TRAINING_ROWS}", "cyan"))

    # Setup
    client = setup_client()
    if not client:
        return

    # Load data
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        print(colored(f"✓ Loaded {len(df)} rows from dataset", "green"))
    except Exception as e:
        print(colored(f"❌ Failed to load data: {e}", "red"))
        return

    # Ensure we have labels and enough rows
    if 'Output' not in df.columns:
        print(colored("❌ Dataset must include 'Output' column", "red"))
        return

    if len(df) < (TRAINING_ROWS + VALIDATION_ROWS):
        print(colored(f"❌ Not enough data, need at least {TRAINING_ROWS + VALIDATION_ROWS} rows", "red"))
        return

    # Create fixed held-out validation set (never enters sampling)
    df_pool, df_validation = create_fixed_validation_split(df)
    print(colored(f"✓ Fixed validation set: {len(df_validation)} rows (held out)", "green"))
    print(colored(f"✓ Training pool size: {len(df_pool)} rows (sampling source)", "green"))
    print(colored(f"📁 Output folder: {OUTPUT_FOLDER}", "cyan"))

    # Main loop
    best_rules = None
    best_accuracy = 0.0
    best_iteration = 0

    for iteration in range(1, MAX_ITERATIONS + 1):
        print(colored(f"\n{'='*50}", "magenta"))
        print(colored(f"🔄 ITERATION {iteration}/{MAX_ITERATIONS}", "magenta"))

        iteration_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Per-iteration stratified training sample from pool (excludes validation)
        sampling_seed = STRATIFIED_SAMPLING_BASE_SEED + iteration
        training_data = stratified_sample(df_pool, TRAINING_ROWS, seed=sampling_seed)

        # Actual values dict for adjust_rules
        actual_values_dict = {idx: row['Output'] for idx, row in training_data.iterrows()}

        # Generate or adjust rules
        if iteration == 1 or best_rules is None:
            current_rules = generate_rules(client, training_data)
            if current_rules:
                save_rules_to_file(current_rules, iteration, is_initial=True)
        else:
            print(colored(f"   🔄 Iterating from best rules (accuracy: {best_accuracy:.1%})", "cyan"))
            # Compute predictions for best_rules on THIS iteration's training sample
            best_predictions_for_sample = predict_batch(client, best_rules, training_data)
            if best_predictions_for_sample:
                adjustment_accuracy = calculate_accuracy(best_predictions_for_sample, training_data)
                print(colored(f"   📊 Adjustment accuracy (best rules on new sample): {adjustment_accuracy:.1%}", "cyan"))
            current_rules = adjust_rules(client, best_rules, training_data,
                                       best_predictions_for_sample or {}, actual_values_dict)
            if current_rules:
                save_rules_to_file(current_rules, iteration, is_initial=False)

        if not current_rules:
            print(colored("❌ Failed to generate/adjust rules", "red"))
            continue

        # Make predictions with current iteration rules on the sampled training set
        predictions_dict = predict_batch(client, current_rules, training_data)
        if not predictions_dict:
            print(colored("❌ Failed to get predictions", "red"))
            continue

        # Calculate accuracy for this iteration
        accuracy = calculate_accuracy(predictions_dict, training_data)

        # Update best rules only if this iteration is better
        if accuracy > best_accuracy:
            print(colored(f"   🎯 New best accuracy! {best_accuracy:.1%} → {accuracy:.1%}", "green"))
            best_accuracy = accuracy
            best_rules = current_rules
            best_iteration = iteration
            # Save the new best rules immediately
            save_best_rules(best_rules, best_accuracy, best_iteration)
        else:
            print(colored(f"   📉 Accuracy: {accuracy:.1%} (best remains: {best_accuracy:.1%})", "yellow"))

        # Save metrics and plot after each iteration
        metrics_data = save_metrics_to_json(iteration, accuracy, best_accuracy, iteration_timestamp)
        if metrics_data:
            plot_accuracy_progress(metrics_data)

        # Check if we reached the threshold
        if best_accuracy >= ACCURACY_THRESHOLD:
            print(colored("🎉 SUCCESS! Reached target accuracy", "green"))
            # Immediate validation on the fixed holdout
            run_validation_phase(client, df_validation, best_rules, best_accuracy, iteration)
            break

        print(colored(f"📈 Best accuracy so far: {best_accuracy:.1%}", "cyan"))

    # Final results
    print(colored("\n🏁 FINAL RESULTS", "green"))
    print(colored(f"   Best accuracy achieved (training samples): {best_accuracy:.1%}", "yellow"))
    print(colored(f"   Target was: {ACCURACY_THRESHOLD:.0%}", "cyan"))
    print(colored(f"   Iterations used: {best_iteration if best_iteration else 0}", "cyan"))

    # Save the best rules
    best_rules_file = save_best_rules(best_rules, best_accuracy, best_iteration)

    print(colored(f"   📁 All files saved in: {OUTPUT_FOLDER}", "cyan"))
    print(colored(f"   🏆 Best rules: {best_rules_file}", "cyan"))
    print(colored(f"   📊 Accuracy metrics: {OUTPUT_FOLDER}/accuracy_metrics.json", "cyan"))
    print(colored(f"   📈 Progress plot: {OUTPUT_FOLDER}/accuracy_progress.png", "cyan"))

    # Always run an end-of-run validation if we have rules
    if best_rules is not None:
        run_validation_phase(client, df_validation, best_rules, best_accuracy, best_iteration or 0)

    if best_accuracy >= ACCURACY_THRESHOLD:
        print(colored("✅ Mission accomplished!", "green"))
    else:
        print(colored("⚠️  Reached max iterations without hitting target", "yellow"))


if __name__ == "__main__":
    main()



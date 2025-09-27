import os
import random
import pandas as pd
import json
import datetime
import matplotlib.pyplot as plt
from openai import OpenAI
from termcolor import colored

# IMPORTANT VARIABLES (ALL CAPS AS REQUESTED)
USE_OPENAI_OR_OPENROUTER = "OPENAI"  # Options: "OPENAI" or "OPENROUTER"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "openai/gpt-5-mini"
REASONING_EFFORT = "high"
CSV_FILE_PATH = "train.csv"
TRAINING_ROWS = 300  # Number of rows to use for training and testing
ACCURACY_THRESHOLD = 0.75  # Stop when accuracy reaches this level
MAX_ITERATIONS = 20  # Maximum attempts to reach threshold
MAX_RETRIES = 3  # Maximum retries for parsing/API failures
OUTPUT_FOLDER = f"adaptive_results_{MODEL_NAME}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
CONTINUE_FROM_LAST_RUN = False  # Resume from the most recent matching output folder
VALIDATION_ROWS = 50  # Number of unseen rows to use for validation
RANDOM_SEED = random.randint(1, 1000000)

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
            # print(f"!!!!!!!!!{response}!!!!!!!!!!1")
            return response.choices[0].message.content

        except Exception as e:
            print(colored(f"⚠️ API call attempt {attempt} failed: {e}", "yellow"))
            if attempt < MAX_RETRIES:
                print(colored("   Retrying API call...", "cyan"))
                import time
                time.sleep(2)  # Longer pause for API errors
            else:
                print(colored(f"❌ API call failed after {MAX_RETRIES} attempts", "red"))
                return None

    return None

def generate_rules(client, training_data):
    """Generate predictive rules from training data with retry mechanism"""
    print(colored(f"\n🧠 Generating rules from {len(training_data)} training rows...", "blue"))

    data_summary = training_data.to_string(index=False)

    prompt = f"""
    Analyze this Spaceship Titanic dataset and create GENERAL predictive rules for passenger transport:

    TRAINING DATA:
    {data_summary}

    CRITICAL: Create GENERAL PATTERN-BASED rules that will work for ANY passenger, not just the ones in this training data.

    RULES MUST BE BASED ON:
    - HomePlanet patterns
    - CryoSleep status
    - Age ranges and demographics
    - Spending patterns (RoomService, FoodCourt, ShoppingMall, Spa, VRDeck)
    - Destination preferences
    - VIP status
    - Cabin location patterns
    - Family/group relationships

    FORBIDDEN: Do NOT create rules based on specific PassengerIds or memorize individual cases.
    FORBIDDEN: Do NOT create rules like "If PassengerId is 0001_01 then predict True"

    Create GENERAL rules that can predict ANY passenger's transport status based on their characteristics.

    Return ONLY the rules in this exact format:
    PREDICTIVE RULES:

    1. [General rule based on passenger characteristics]
    2. [General rule based on spending patterns]
    3. [General rule based on demographics]
    [Continue with as many GENERAL rules as needed]

    Do not include any explanations, analysis, or discussion. Only GENERAL rules.
    """

    messages = [
        {"role": "system", "content": "You are an expert predictive model that creates GENERAL rules, not memorizes specific cases. Never create PassengerId-specific rules. Return ONLY general pattern-based rules."},
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
                time.sleep(1)  # Brief pause between retries
            else:
                print(colored(f"❌ Failed to generate valid rules after {MAX_RETRIES} attempts", "red"))
                return None

    return None

def predict_batch(client, rules, test_data):
    """Predict all test rows in one API call with retry mechanism"""
    print(colored(f"\n🔮 Predicting {len(test_data)} passengers...", "blue"))

    # Remove actual transported values for prediction
    prediction_data = test_data.drop(columns=['Transported']).to_string(index=False)

    prompt = f"""
    You are a predictive system that must return predictions in PERFECT structured text format.

    PREDICTIVE RULES TO USE:
    {rules}

    PASSENGER DATA TO PREDICT (predict for ALL {len(test_data)} passengers):
    {prediction_data}

    CRITICAL REQUIREMENTS:
    1. Return predictions for ALL {len(test_data)} passengers by their PassengerId
    2. Each prediction must be either true or false (boolean values only)
    3. Return ONLY the structured predictions - no extra text, no explanations

    REQUIRED OUTPUT FORMAT:
    PREDICTIONS:
    0001_01: true
    0001_02: false
    0002_01: true
    [Continue with ALL {len(test_data)} predictions in this exact format]

    Example for 3 passengers:
    PREDICTIONS:
    0001_01: true
    0002_01: false
    0003_01: true

    Make sure to include EXACTLY {len(test_data)} predictions with the correct PassengerIds from the data above.
    Each line must be in format: PASSENGERID: PREDICTION
    """

    messages = [
        {"role": "system", "content": "You are a precise predictive system. Return ONLY structured predictions in the exact format requested. No extra text or explanations."},
        {"role": "user", "content": prompt}
    ]

    for attempt in range(1, MAX_RETRIES + 1):
        print(colored(f"   Attempt {attempt}/{MAX_RETRIES}...", "cyan"))

        response = call_llm(client, messages)

        if response:
            try:
                import re

                # Parse structured text format: PREDICTIONS:\nPASSENGERID: PREDICTION\n...
                predictions_dict = {}

                # Look for the PREDICTIONS section
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

                # Parse each line for passenger ID and prediction
                lines = predictions_text.strip().split('\n')
                for line in lines:
                    line = line.strip()
                    if not line:  # Skip empty lines
                        continue

                    # Match format: PASSENGERID: PREDICTION
                    match = re.match(r'^([^:]+):\s*(true|false)$', line)
                    if match:
                        passenger_id = match.group(1).strip()
                        prediction_str = match.group(2).strip()

                        # Convert string to boolean
                        if prediction_str.lower() == 'true':
                            transported = True
                        elif prediction_str.lower() == 'false':
                            transported = False
                        else:
                            print(colored(f"⚠️ Attempt {attempt} failed - Invalid prediction value '{prediction_str}' for {passenger_id}", "yellow"))
                            if attempt < MAX_RETRIES:
                                print(colored("   Retrying...", "cyan"))
                                import time
                                time.sleep(1)
                                break
                            else:
                                return None

                        predictions_dict[passenger_id] = transported
                    else:
                        # Skip lines that don't match the format (could be extra text)
                        continue
                else:
                    # If we parsed all lines successfully, validate the results
                    # Verify we have predictions for all expected passenger IDs
                    expected_ids = set(test_data['PassengerId'].tolist())
                    received_ids = set(predictions_dict.keys())

                    if len(predictions_dict) == 0:
                        print(colored(f"⚠️ Attempt {attempt} failed - No valid predictions found", "yellow"))
                        if attempt < MAX_RETRIES:
                            print(colored("   Retrying...", "cyan"))
                            import time
                            time.sleep(1)
                            continue
                        else:
                            return None

                    if expected_ids != received_ids:
                        missing = expected_ids - received_ids
                        if missing:
                            print(colored(f"⚠️ Attempt {attempt} failed - Missing predictions for: {list(missing)}", "yellow"))
                            print(colored(f"Expected {len(expected_ids)} predictions, got {len(predictions_dict)}", "yellow"))
                            if attempt < MAX_RETRIES:
                                print(colored("   Retrying...", "cyan"))
                                import time
                                time.sleep(1)
                                continue
                            else:
                                return None

                    # If we get here, parsing was successful
                    print(colored(f"✓ Got {len(predictions_dict)} validated ID-based predictions", "green"))
                    return predictions_dict

                # If we broke out of the loop due to parsing error, continue to next attempt
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

    # If we exhaust all attempts
    print(colored(f"❌ All {MAX_RETRIES} prediction attempts failed", "red"))
    return None

def calculate_accuracy(predictions_dict, training_data):
    """Calculate prediction accuracy using ID-based matching"""
    if not isinstance(predictions_dict, dict):
        print(colored("❌ Predictions must be a dictionary", "red"))
        return 0.0

    # Create actual values dictionary by passenger ID
    actual_dict = {}
    for _, row in training_data.iterrows():
        actual_dict[row['PassengerId']] = row['Transported']

    if len(predictions_dict) != len(actual_dict):
        print(colored(f"❌ Prediction/actual count mismatch: {len(predictions_dict)} vs {len(actual_dict)}", "red"))
        return 0.0

    correct = 0
    total = 0

    # Calculate accuracy by matching passenger IDs
    for passenger_id, predicted in predictions_dict.items():
        if passenger_id in actual_dict:
            actual = actual_dict[passenger_id]
            if predicted == actual:
                correct += 1
            total += 1
        else:
            print(colored(f"⚠️ No actual value found for passenger {passenger_id}", "yellow"))

    if total == 0:
        print(colored("❌ No matching predictions found", "red"))
        return 0.0

    accuracy = correct / total
    print(colored(f"📊 Accuracy: {accuracy:.1%} ({correct}/{total})", "cyan"))
    return accuracy

def adjust_rules(client, current_rules, training_data, predictions_dict, actual_values_dict):
    """Adjust rules based on prediction errors with retry mechanism"""
    print(colored("\n🔧 Adjusting rules based on errors...", "yellow"))

    # Create formatted training data with error highlighting
    formatted_data_rows = []

    for i, row in training_data.iterrows():
        passenger_id = row['PassengerId']
        actual = actual_values_dict.get(passenger_id)
        predicted = predictions_dict.get(passenger_id)

        if predicted is None:
            # Missing prediction
            formatted_row = f"""❓ MISSING PREDICTION ROW {i+1} ❓
PassengerId: {passenger_id}
Actual: {actual}
{row.to_string()}
{'─' * 80}"""
        else:
            is_error = predicted != actual

            if is_error:
                # Highlight error rows with clear markers
                formatted_row = f"""🚨 ERROR ROW {i+1} 🚨
PassengerId: {passenger_id}
Predicted: {predicted} | Actual: {actual}
{row.to_string()}
{'─' * 80}"""
            else:
                # Show correct predictions with checkmark
                formatted_row = f"""✅ CORRECT ROW {i+1}
PassengerId: {passenger_id}
Predicted: {predicted} | Actual: {actual}
{row.to_string()}"""

        formatted_data_rows.append(formatted_row)

    formatted_training_data = "\n\n".join(formatted_data_rows)

    # Count errors for summary
    error_count = 0
    total_predictions = 0

    for passenger_id, predicted in predictions_dict.items():
        if passenger_id in actual_values_dict:
            actual = actual_values_dict[passenger_id]
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

    CRITICAL: Create GENERAL PATTERN-BASED rules that will work for ANY passenger, not just memorizing these specific cases.

    RULES MUST BE BASED ON GENERAL PATTERNS:
    - HomePlanet patterns and behaviors
    - CryoSleep status and its implications
    - Age ranges and demographic trends
    - Spending patterns across all amenities
    - Destination-based transport likelihood
    - VIP status effects
    - Cabin location and ship section patterns
    - Family/group relationship patterns

    FORBIDDEN: Do NOT memorize specific PassengerIds or create ID-specific rules.
    FORBIDDEN: Do NOT create rules like "If PassengerId is 0001_01 then predict True"
    FORBIDDEN: Do NOT create rules based on exact matches to training data.

    Create GENERAL rules that identify PATTERNS in the error data and correct them for ALL similar cases.

    Return ONLY the improved GENERAL rules in this exact format:
    IMPROVED PREDICTIVE RULES:

    1. [General rule based on error patterns and corrections]
    2. [General rule addressing common error causes]
    3. [General rule for demographic corrections]
    [Continue with as many GENERAL rules as needed]

    Do not include any explanations, analysis, or discussion. Only GENERAL rules.
    """

    messages = [
        {"role": "system", "content": "You are an expert predictive model that creates GENERAL rules, not memorizes specific cases. Never create PassengerId-specific rules. Focus on PATTERNS that fix errors for ALL similar cases."},
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
                time.sleep(1)  # Brief pause between retries
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

        # Load existing metrics or create new structure
        if os.path.exists(metrics_file):
            with open(metrics_file, 'r', encoding='utf-8') as f:
                metrics_data = json.load(f)
        else:
            metrics_data = {
                "training_rows": TRAINING_ROWS,
                "accuracy_threshold": ACCURACY_THRESHOLD,
                "max_iterations": MAX_ITERATIONS,
                "iterations": []
            }

        # Add new iteration data
        iteration_data = {
            "iteration": iteration,
            "accuracy": round(accuracy, 4),
            "best_accuracy": round(best_accuracy, 4),
            "timestamp": timestamp,
            "above_threshold": accuracy >= ACCURACY_THRESHOLD
        }

        metrics_data["iterations"].append(iteration_data)

        # Save updated metrics
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

        # Create a clear filename with the best accuracy
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

        # Extract data for plotting
        iterations = [item["iteration"] for item in iterations_data]
        accuracies = [item["accuracy"] for item in iterations_data]
        best_accuracies = [item["best_accuracy"] for item in iterations_data]

        plt.figure(figsize=(12, 8))

        # Separate training vs validation data (using is_validation flag if present)
        training_iterations = []
        training_accuracies = []
        training_best_accuracies = []
        validation_points = []  # list of tuples (iteration, accuracy)

        for item in iterations_data:
            if item.get("is_validation", False):
                validation_points.append((item.get("iteration"), item.get("accuracy")))
            else:
                training_iterations.append(item.get("iteration"))
                training_accuracies.append(item.get("accuracy"))
                training_best_accuracies.append(item.get("best_accuracy"))

        # Plot training accuracy progression
        if training_iterations:
            plt.plot(training_iterations, training_accuracies, 'b-', linewidth=2, marker='o', markersize=6,
                    label='Training Current Accuracy', alpha=0.8)

            plt.plot(training_iterations, training_best_accuracies, 'r-', linewidth=2, marker='s', markersize=6,
                    label='Training Best Accuracy', alpha=0.8)

        # Plot validation result(s) if available
        if validation_points:
            for (v_iter, v_acc) in validation_points:
                if v_iter is None or v_acc is None:
                    continue
                plt.plot([v_iter], [v_acc], 'g-', linewidth=3, marker='*', markersize=15,
                        label='Validation Accuracy' if (v_iter, v_acc) == validation_points[0] else None, alpha=1.0)
                plt.axvline(x=v_iter - 0.5, color='g', linestyle=':', linewidth=2, alpha=0.7)

        # Add threshold line
        plt.axhline(y=ACCURACY_THRESHOLD, color='g', linestyle='--', linewidth=2,
                   label=f'Target ({ACCURACY_THRESHOLD:.0%})', alpha=0.7)

        # Styling
        plt.grid(True, alpha=0.3)
        plt.xlabel('Iteration', fontsize=12)
        plt.ylabel('Accuracy', fontsize=12)
        title = 'Adaptive Prediction Accuracy Progress'
        if validation_points:
            title += ' (with Validation)'
        plt.title(title, fontsize=14, fontweight='bold')
        plt.legend(loc='lower right', fontsize=10)

        # Set y-axis limits
        plt.ylim(0, 1.0)
        plt.yticks([i/10 for i in range(11)], [f'{i*10}%' for i in range(11)])

        # Add current values as text
        if training_accuracies:
            current_acc = training_accuracies[-1]
            best_acc = training_best_accuracies[-1]
            plt.text(0.02, 0.98, f'Training: {current_acc:.1%}',
                    transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))
            plt.text(0.02, 0.90, f'Best: {best_acc:.1%}',
                    transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
                    bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))

            # Add validation result if available
            if validation_points:
                last_val_acc = None
                for (_, v_acc) in validation_points:
                    last_val_acc = v_acc
                if last_val_acc is not None:
                    plt.text(0.02, 0.82, f'Validation: {last_val_acc:.1%}',
                            transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
                            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

        # Save plot
        plot_filename = f"{OUTPUT_FOLDER}/accuracy_progress.png"
        plt.savefig(plot_filename, dpi=150, bbox_inches='tight')
        plt.close()

        print(colored(f"📈 Accuracy plot updated: {plot_filename}", "cyan"))
        return plot_filename

    except Exception as e:
        print(colored(f"⚠️ Failed to create accuracy plot: {e}", "yellow"))
        return None


def _resolve_results_search_paths():
    """Resolve parent directory and subfolder prefix for results based on MODEL_NAME."""
    try:
        if "/" in MODEL_NAME:
            vendor, model_id = MODEL_NAME.split("/", 1)
            parent_dir = f"adaptive_results_{vendor}"
            sub_prefix = f"{model_id}_"
            return parent_dir, sub_prefix
        # Fallback: results are top-level like adaptive_results_MODELNAME_YYYYMMDD_HHMMSS
        return ".", f"adaptive_results_{MODEL_NAME}_"
    except Exception:
        return ".", f"adaptive_results_{MODEL_NAME}_"


def find_last_run_folder_for_model():
    """Find the most recent results folder for the current MODEL_NAME.

    Returns absolute/relative path to the folder or None.
    """
    parent_dir, sub_prefix = _resolve_results_search_paths()

    try:
        if parent_dir != "." and os.path.isdir(parent_dir):
            candidates = [
                d for d in os.listdir(parent_dir)
                if os.path.isdir(os.path.join(parent_dir, d)) and d.startswith(sub_prefix)
            ]
            if not candidates:
                return None
            # Newest by lexicographic order due to timestamp format in name
            candidates.sort(reverse=True)
            for d in candidates:
                folder_path = os.path.join(parent_dir, d)
                if os.path.exists(os.path.join(folder_path, "accuracy_metrics.json")):
                    return folder_path
            return None

        # Fallback: scan top-level for adaptive_results_MODEL_
        if parent_dir == ".":
            candidates = [
                d for d in os.listdir('.')
                if os.path.isdir(d) and d.startswith(sub_prefix)
            ]
            if not candidates:
                return None
            candidates.sort(reverse=True)
            for d in candidates:
                folder_path = d
                if os.path.exists(os.path.join(folder_path, "accuracy_metrics.json")):
                    return folder_path
            return None

    except Exception:
        return None

    return None


def load_resume_state(folder_path):
    """Load state from a previous run folder.

    Returns dict with keys:
      - start_iteration
      - best_rules (str or None)
      - best_accuracy (float)
      - best_iteration (int)
      - best_predictions_dict (dict or None)
      - metrics_data (dict)
    """
    state = {
        "start_iteration": 1,
        "best_rules": None,
        "best_accuracy": 0.0,
        "best_iteration": 0,
        "best_predictions_dict": None,
        "metrics_data": None,
    }

    try:
        metrics_file = os.path.join(folder_path, "accuracy_metrics.json")
        if not os.path.exists(metrics_file):
            return state

        with open(metrics_file, 'r', encoding='utf-8') as f:
            metrics_data = json.load(f)
        state["metrics_data"] = metrics_data

        iterations = metrics_data.get("iterations", [])
        training_iters = [it.get("iteration") for it in iterations if not it.get("is_validation", False)]
        last_training_iter = max(training_iters) if training_iters else 0
        state["start_iteration"] = min(last_training_iter + 1, MAX_ITERATIONS + 1)

        # Determine best accuracy and iteration
        best_acc = 0.0
        best_iter = 0
        for it in iterations:
            if not it.get("is_validation", False):
                if it.get("best_accuracy", 0.0) >= best_acc:
                    best_acc = it.get("best_accuracy", 0.0)
                    best_iter = it.get("iteration", 0)
        state["best_accuracy"] = float(best_acc)
        state["best_iteration"] = int(best_iter)

        # Load best predictions if available
        best_preds_path = os.path.join(folder_path, "best_predictions.json")
        if os.path.exists(best_preds_path):
            try:
                with open(best_preds_path, 'r', encoding='utf-8') as f:
                    state["best_predictions_dict"] = json.load(f)
            except Exception:
                state["best_predictions_dict"] = None

        # Load best rules if available; fallback to most recent rules file
        best_rules_file = None
        try:
            files = os.listdir(folder_path)
            best_rule_files = [fn for fn in files if fn.startswith("best_rules_") and fn.endswith(".txt")]
            if best_rule_files:
                # Prefer the one with highest percentage in filename by lexical order
                best_rule_files.sort(reverse=True)
                best_rules_file = os.path.join(folder_path, best_rule_files[0])
            else:
                rule_files = [fn for fn in files if (fn.startswith("rules_iteration_") or fn == "initial_rules.txt") and fn.endswith(".txt")]
                if rule_files:
                    rule_files.sort(reverse=True)
                    best_rules_file = os.path.join(folder_path, rule_files[0])
        except Exception:
            best_rules_file = None

        if best_rules_file and os.path.exists(best_rules_file):
            try:
                with open(best_rules_file, 'r', encoding='utf-8') as f:
                    state["best_rules"] = f.read()
            except Exception:
                state["best_rules"] = None

    except Exception:
        # Return whatever we could fetch
        return state

    return state


def run_validation_phase(client, df, best_rules, best_accuracy, current_iteration):
    """Run validation on the next VALIDATION_ROWS after TRAINING_ROWS and persist metrics/plot."""
    try:
        if best_rules is None:
            print(colored("⚠️ Skipping validation - no rules available", "yellow"))
            return None

        validation_start = TRAINING_ROWS
        validation_end = TRAINING_ROWS + VALIDATION_ROWS

        if len(df) <= validation_start:
            print(colored("⚠️ Not enough data for validation phase", "yellow"))
            return None

        validation_rows = df.iloc[validation_start:validation_end].copy()
        print(colored(f"\n🧪 VALIDATION PHASE - Testing on {len(validation_rows)} unseen rows...", "blue"))

        validation_predictions = predict_batch(client, best_rules, validation_rows)
        if not validation_predictions:
            print(colored("❌ Validation failed - could not get predictions", "red"))
            return None

        validation_accuracy = calculate_accuracy(validation_predictions, validation_rows)
        validation_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save validation as a separate metrics entry (mark last entry as validation)
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
    """Main prediction loop"""
    print(colored("🚀 Simple Adaptive Prediction System", "cyan"))
    print(colored(f"🎯 Target accuracy: {ACCURACY_THRESHOLD:.0%}", "cyan"))
    print(colored(f"📊 Training rows: {TRAINING_ROWS}", "cyan"))

    # Setup
    client = setup_client()
    if not client:
        return

    # Load data
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        print(colored(f"✓ Loaded {len(df)} rows from dataset", "green"))

        # Shuffle the dataset for better generalization
        df = df.sample(frac=1, random_state=RANDOM_SEED).reset_index(drop=True)
        print(colored("✓ Dataset shuffled for better generalization", "green"))
    except Exception as e:
        print(colored(f"❌ Failed to load data: {e}", "red"))
        return

    # Use first TRAINING_ROWS for both training and testing
    if len(df) < TRAINING_ROWS:
        print(colored(f"❌ Not enough data, need at least {TRAINING_ROWS} rows", "red"))
        return

    training_data = df.head(TRAINING_ROWS).copy()

    # Create actual values dictionary by passenger ID
    actual_values_dict = {}
    for _, row in training_data.iterrows():
        actual_values_dict[row['PassengerId']] = row['Transported']

    # Determine output folder (resume if requested)
    global OUTPUT_FOLDER
    start_iteration = 1
    best_rules = None
    best_accuracy = 0.0
    best_iteration = 0
    best_predictions_dict = None  # Predictions produced by best_rules
    last_predictions_dict = None  # Predictions produced by current_rules (may be non-best)
    metrics_data = None

    if CONTINUE_FROM_LAST_RUN:
        resume_folder = find_last_run_folder_for_model()
        if resume_folder:
            OUTPUT_FOLDER = resume_folder
            print(colored(f"🔁 Resuming from: {OUTPUT_FOLDER}", "cyan"))
            resume_state = load_resume_state(OUTPUT_FOLDER)
            start_iteration = resume_state.get("start_iteration", 1)
            best_rules = resume_state.get("best_rules")
            best_accuracy = resume_state.get("best_accuracy", 0.0)
            best_iteration = resume_state.get("best_iteration", 0)
            best_predictions_dict = resume_state.get("best_predictions_dict")
            metrics_data = resume_state.get("metrics_data")
        else:
            print(colored("ℹ️ No previous run found for this model. Starting fresh.", "cyan"))

    print(colored(f"📁 Output folder: {OUTPUT_FOLDER}", "cyan"))

    # Main loop
    last_completed_iteration = 0
    for iteration in range(start_iteration, MAX_ITERATIONS + 1):
        print(colored(f"\n{'='*50}", "magenta"))
        print(colored(f"🔄 ITERATION {iteration}/{MAX_ITERATIONS}", "magenta"))

        iteration_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Generate or adjust rules (always iterate from best rules)
        if iteration == 1:
            # First iteration: generate initial rules
            current_rules = generate_rules(client, training_data)
            if current_rules:
                save_rules_to_file(current_rules, iteration, is_initial=True)
        else:
            # Subsequent iterations: adjust from best rules using predictions from best rules
            print(colored(f"   🔄 Iterating from best rules (accuracy: {best_accuracy:.1%})", "cyan"))
            # Ensure we have predictions that correspond to best_rules
            if best_predictions_dict is None:
                # Compute predictions for best_rules if missing
                best_predictions_dict = predict_batch(client, best_rules, training_data)
            current_rules = adjust_rules(client, best_rules, training_data,
                                       best_predictions_dict, actual_values_dict)
            if current_rules:
                save_rules_to_file(current_rules, iteration, is_initial=False)

        if not current_rules:
            print(colored("❌ Failed to generate/adjust rules", "red"))
            continue

        # Make predictions with current iteration rules
        predictions_dict = predict_batch(client, current_rules, training_data)

        if not predictions_dict:
            print(colored("❌ Failed to get predictions", "red"))
            continue

        # Calculate accuracy for this iteration
        accuracy = calculate_accuracy(predictions_dict, training_data)

        # Store predictions for next iteration's rule adjustment
        last_predictions_dict = predictions_dict

        # Update best rules only if this iteration is better
        if accuracy > best_accuracy:
            print(colored(f"   🎯 New best accuracy! {best_accuracy:.1%} → {accuracy:.1%}", "green"))
            best_accuracy = accuracy
            best_rules = current_rules
            best_iteration = iteration
            # Store predictions associated with the new best rules
            best_predictions_dict = predictions_dict
        else:
            print(colored(f"   📉 Accuracy: {accuracy:.1%} (best remains: {best_accuracy:.1%})", "yellow"))

        # Save metrics and plot after each iteration
        metrics_data = save_metrics_to_json(iteration, accuracy, best_accuracy, iteration_timestamp)
        if metrics_data:
            plot_accuracy_progress(metrics_data)

        # Check if we reached the threshold
        if best_accuracy >= ACCURACY_THRESHOLD:
            print(colored("🎉 SUCCESS! Reached target accuracy", "green"))
            # Run immediate validation when threshold is reached
            run_validation_phase(client, df, best_rules, best_accuracy, iteration)
            last_completed_iteration = iteration
            break

        print(colored(f"📈 Best accuracy so far: {best_accuracy:.1%}", "cyan"))
        last_completed_iteration = iteration

    # Final results
    print(colored("\n🏁 FINAL RESULTS", "green"))
    print(colored(f"   Best accuracy achieved: {best_accuracy:.1%}", "yellow"))
    print(colored(f"   Target was: {ACCURACY_THRESHOLD:.0%}", "cyan"))
    print(colored(f"   Iterations used: {last_completed_iteration if last_completed_iteration else 0}", "cyan"))

    # Save the best rules
    best_rules_file = save_best_rules(best_rules, best_accuracy, best_iteration)

    # Save the best predictions dict for reproducibility/debugging
    try:
        if best_predictions_dict is not None:
            best_preds_file = f"{OUTPUT_FOLDER}/best_predictions.json"
            with open(best_preds_file, 'w', encoding='utf-8') as f:
                json.dump(best_predictions_dict, f, indent=2, ensure_ascii=False)
            print(colored(f"   🗂️ Best predictions saved: {best_preds_file}", "cyan"))
    except Exception as e:
        print(colored(f"⚠️ Failed to save best predictions: {e}", "yellow"))

    print(colored(f"   📁 All files saved in: {OUTPUT_FOLDER}", "cyan"))
    print(colored(f"   🏆 Best rules: {best_rules_file}", "cyan"))
    print(colored(f"   📊 Accuracy metrics: {OUTPUT_FOLDER}/accuracy_metrics.json", "cyan"))
    print(colored(f"   📈 Progress plot: {OUTPUT_FOLDER}/accuracy_progress.png", "cyan"))

    # Count saved rule files
    try:
        rule_files = [f for f in os.listdir(OUTPUT_FOLDER) if f.startswith('rules_') or f.startswith('initial_') or f.startswith('best_')]
        print(colored(f"   📝 Rule files saved: {len(rule_files)}", "cyan"))
    except:
        pass

    # Validation Phase: Always run at end with best rules if available
    if best_rules:
        run_validation_phase(client, df, best_rules, best_accuracy, last_completed_iteration or 0)

    if best_accuracy >= ACCURACY_THRESHOLD:
        print(colored("✅ Mission accomplished!", "green"))
    else:
        print(colored("⚠️  Reached max iterations without hitting target", "yellow"))

if __name__ == "__main__":
    main()

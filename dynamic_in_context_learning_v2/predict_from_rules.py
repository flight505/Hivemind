import os
import pandas as pd
import json
import threading
from openai import OpenAI
from termcolor import colored

# IMPORTANT VARIABLES (ALL CAPS AS REQUESTED)
USE_OPENAI_OR_OPENROUTER = "OPENROUTER"  # Options: "OPENAI" or "OPENROUTER"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "openai/gpt-5-mini"
REASONING_EFFORT = "high"
CSV_FILE_PATH = "train.csv"
RULES_FILE_PATH = r"adaptive_sampling_results_gpt-5_20250903_142149\best_rules_96pct_accuracy.txt"  # Path to rules file - using raw string to handle backslashes
RULES_FILE_PATH = RULES_FILE_PATH.replace('\\', '/')  # Convert backslashes to forward slashes for cross-platform compatibility


SAMPLE_SIZE = 50  # Number of random samples to predict on
PARALLEL_RUNS = 5  # Number of parallel predictions on the same sample
MAX_RETRIES = 3  # Maximum retries for API failures


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


def load_rules_from_file(rules_file_path):
    """Load rules from a text file"""
    try:
        with open(rules_file_path, 'r', encoding='utf-8') as f:
            rules_content = f.read()
        print(colored(f"✓ Rules loaded from: {rules_file_path}", "green"))
        return rules_content
    except Exception as e:
        print(colored(f"❌ Failed to load rules: {e}", "red"))
        return None


def predict_batch(client, rules, test_data):
    """Predict all test rows in one API call with retry mechanism"""
    print(colored(f"\n🔮 Predicting {len(test_data)} passengers...", "blue"))

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

                    match = re.match(r'^([^:]+):\s*(true|false)$', line)
                    if match:
                        passenger_id = match.group(1).strip()
                        prediction_str = match.group(2).strip()

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
                        continue
                else:
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

                    print(colored(f"✓ Got {len(predictions_dict)} validated ID-based predictions", "green"))
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
    """Calculate prediction accuracy using ID-based matching"""
    if not isinstance(predictions_dict, dict):
        print(colored("❌ Predictions must be a dictionary", "red"))
        return 0.0

    actual_dict = {}
    for _, row in data_with_labels.iterrows():
        actual_dict[row['PassengerId']] = row['Transported']

    if len(predictions_dict) != len(actual_dict):
        print(colored(f"❌ Prediction/actual count mismatch: {len(predictions_dict)} vs {len(actual_dict)}", "red"))
        return 0.0

    correct = 0
    total = 0
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


def main():
    """Predict on random samples using rules from file"""
    print(colored("🚀 Predict from Rules Script", "cyan"))
    print(colored(f"📊 Sample size: {SAMPLE_SIZE}", "cyan"))
    print(colored(f"📁 Rules file: {RULES_FILE_PATH}", "cyan"))

    # Setup
    client = setup_client()
    if not client:
        return

    # Load rules
    rules = load_rules_from_file(RULES_FILE_PATH)
    if not rules:
        return

    # Load data
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        print(colored(f"✓ Loaded {len(df)} rows from dataset", "green"))
    except Exception as e:
        print(colored(f"❌ Failed to load data: {e}", "red"))
        return

    # Ensure we have labels
    if 'Transported' not in df.columns:
        print(colored("❌ Dataset must include 'Transported' column", "red"))
        return

    if len(df) < SAMPLE_SIZE:
        print(colored(f"❌ Not enough data, need at least {SAMPLE_SIZE} rows", "red"))
        return

    # Sample random rows (stratified by Transported for balance)
    try:
        class_counts = df["Transported"].value_counts(dropna=False)
        if len(class_counts) >= 2:
            pos_prop = class_counts.get(True, 0) / len(df) if len(df) > 0 else 0
            desired_pos = int(round(SAMPLE_SIZE * pos_prop))
            desired_neg = max(SAMPLE_SIZE - desired_pos, 0)

            pos_df = df[df["Transported"] == True]
            neg_df = df[df["Transported"] == False]

            pos_take = min(len(pos_df), desired_pos)
            neg_take = min(len(neg_df), desired_neg)

            remaining = max(SAMPLE_SIZE - (pos_take + neg_take), 0)
            if remaining > 0:
                if len(pos_df) - pos_take >= len(neg_df) - neg_take:
                    pos_take = min(len(pos_df), pos_take + remaining)
                else:
                    neg_take = min(len(neg_df), neg_take + remaining)

            pos_sample = pos_df.sample(n=pos_take, random_state=42)
            neg_sample = neg_df.sample(n=neg_take, random_state=42)
            sample_df = pd.concat([pos_sample, neg_sample]).sample(frac=1, random_state=42).reset_index(drop=True)
        else:
            sample_df = df.sample(n=SAMPLE_SIZE, random_state=42).reset_index(drop=True)

        print(colored(f"✓ Sampled {len(sample_df)} rows (stratified by Transported)", "green"))

    except Exception as e:
        print(colored(f"⚠️ Sampling failed: {e} - falling back to random sample", "yellow"))
        sample_df = df.sample(n=min(SAMPLE_SIZE, len(df)), random_state=42).reset_index(drop=True)

    # Predict in parallel
    print(colored(f"\n🔄 Running {PARALLEL_RUNS} parallel predictions on {len(sample_df)} samples...", "blue"))

    accuracies = {}
    threads = []

    def predict_and_calculate(run_id):
        """Thread function to predict and calculate accuracy for one run"""
        predictions = predict_batch(client, rules, sample_df)
        if predictions:
            accuracy = calculate_accuracy(predictions, sample_df)
            accuracies[run_id] = accuracy
        else:
            accuracies[run_id] = None

    for i in range(1, PARALLEL_RUNS + 1):
        thread = threading.Thread(target=predict_and_calculate, args=(i,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Print results sequentially
    print(colored("\n🏁 PARALLEL PREDICTION RESULTS", "green"))
    print(colored(f"   🤖 Model: {MODEL_NAME}", "cyan"))
    for run_id in sorted(accuracies.keys()):
        accuracy = accuracies[run_id]
        if accuracy is not None:
            print(colored(f"   Run {run_id}: 📊 Accuracy: {accuracy:.1%}", "yellow"))
        else:
            print(colored(f"   Run {run_id}: ❌ Failed", "red"))

    # Calculate and print average accuracy
    valid_accuracies = [acc for acc in accuracies.values() if acc is not None]
    avg_accuracy = None
    if valid_accuracies:
        avg_accuracy = sum(valid_accuracies) / len(valid_accuracies)
        print(colored(f"   📈 Average Accuracy: {avg_accuracy:.1%} (from {len(valid_accuracies)}/{PARALLEL_RUNS} successful runs)", "magenta"))
    else:
        print(colored("   ❌ No successful runs to calculate average", "red"))

    print(colored(f"   📁 Rules used: {RULES_FILE_PATH}", "cyan"))

    # Save accuracies summary to JSON
    try:
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        # Include average accuracy in filename if available
        avg_pct_str = ""
        if avg_accuracy is not None:
            avg_pct = int(avg_accuracy * 100)
            avg_pct_str = f"{avg_pct}pct_avg_"

        summary_file = f"accuracies_summary_{avg_pct_str}{SAMPLE_SIZE}_samples_{PARALLEL_RUNS}_runs_{timestamp}.json"
        summary = {
            "sample_size": SAMPLE_SIZE,
            "parallel_runs": PARALLEL_RUNS,
            "rules_file": RULES_FILE_PATH,
            "accuracies": accuracies,
            "average_accuracy": round(avg_accuracy, 4) if avg_accuracy is not None else None,
            "successful_runs": len(valid_accuracies) if valid_accuracies else 0
        }
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        print(colored(f"   🗂️ Accuracies summary saved: {summary_file}", "cyan"))
    except Exception as e:
        print(colored(f"⚠️ Failed to save accuracies summary: {e}", "yellow"))


if __name__ == "__main__":
    main()

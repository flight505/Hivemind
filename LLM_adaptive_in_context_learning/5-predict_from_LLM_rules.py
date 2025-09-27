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
CSV_FILE_PATH = "complex_dataset.csv"
RULES_FILE_PATH = r"adaptive_sampling_results_gpt-5_20250904_201135\best_rules_50pct_accuracy.txt"  # Path to our LLM-generated rules
RULES_FILE_PATH = RULES_FILE_PATH.replace('\\', '/')  # Convert backslashes to forward slashes for cross-platform compatibility


SAMPLE_SIZE = 50  # Number of rows per random sample
NUM_SAMPLES = 5  # Number of different random samples to test
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


def main():
    """Predict on random samples using LLM-generated rules for complex dataset"""
    print(colored("🚀 Predict from LLM Rules - Complex Dataset", "cyan"))
    print(colored("🎯 Testing LLM-generated rules on interdependent classification (A,B,C,D,E) -> Output (1-4)", "cyan"))
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
    if 'Output' not in df.columns:
        print(colored("❌ Dataset must include 'Output' column", "red"))
        return

    if len(df) < SAMPLE_SIZE:
        print(colored(f"❌ Not enough data, need at least {SAMPLE_SIZE} rows", "red"))
        return

    # Sample random rows (stratified by Output for balance across 4 classes)
    try:
        class_counts = df["Output"].value_counts(dropna=False)
        if len(class_counts) >= 2:
            # Calculate proportional allocation for each class (1-4)
            total = len(df)
            class_props = {}
            for class_val in range(1, 5):  # Classes 1, 2, 3, 4
                class_props[class_val] = class_counts.get(class_val, 0) / total if total > 0 else 0

            # Calculate desired counts per class
            desired_counts = {}
            total_desired = 0
            for class_val in range(1, 5):
                desired_counts[class_val] = int(round(SAMPLE_SIZE * class_props[class_val]))
                total_desired += desired_counts[class_val]

            # Adjust for rounding errors
            remaining = SAMPLE_SIZE - total_desired
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
                    class_sample = class_df.sample(n=n_take, random_state=42)
                    samples.append(class_sample)

            if samples:
                sample_df = pd.concat(samples).sample(frac=1, random_state=42).reset_index(drop=True)
            else:
                sample_df = df.sample(n=SAMPLE_SIZE, random_state=42).reset_index(drop=True)
        else:
            sample_df = df.sample(n=SAMPLE_SIZE, random_state=42).reset_index(drop=True)

        print(colored(f"✓ Sampled {len(sample_df)} rows (stratified by Output)", "green"))

    except Exception as e:
        print(colored(f"⚠️ Sampling failed: {e} - falling back to random sample", "yellow"))
        sample_df = df.sample(n=min(SAMPLE_SIZE, len(df)), random_state=42).reset_index(drop=True)

    # Test multiple different random samples in parallel
    print(colored(f"\n🔄 Testing {NUM_SAMPLES} different random samples of {SAMPLE_SIZE} rows each in parallel...", "blue"))

    accuracies = {}
    threads = []

    def predict_sample(sample_id):
        """Thread function to generate sample, predict, and calculate accuracy"""
        print(colored(f"📊 Sample {sample_id}/{NUM_SAMPLES}:", "cyan"))

        # Generate a different random sample for this thread
        sample_seed = 42 + sample_id  # Different seed for each sample
        try:
            class_counts = df["Output"].value_counts(dropna=False)
            if len(class_counts) >= 2:
                # Calculate proportional allocation for each class (1-4)
                total = len(df)
                class_props = {}
                for class_val in range(1, 5):  # Classes 1, 2, 3, 4
                    class_props[class_val] = class_counts.get(class_val, 0) / total if total > 0 else 0

                # Calculate desired counts per class
                desired_counts = {}
                total_desired = 0
                for class_val in range(1, 5):
                    desired_counts[class_val] = int(round(SAMPLE_SIZE * class_props[class_val]))
                    total_desired += desired_counts[class_val]

                # Adjust for rounding errors
                remaining = SAMPLE_SIZE - total_desired
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
                        class_sample = class_df.sample(n=n_take, random_state=sample_seed)
                        samples.append(class_sample)

                if samples:
                    sample_df = pd.concat(samples).sample(frac=1, random_state=sample_seed).reset_index(drop=True)
                else:
                    sample_df = df.sample(n=SAMPLE_SIZE, random_state=sample_seed).reset_index(drop=True)
            else:
                sample_df = df.sample(n=SAMPLE_SIZE, random_state=sample_seed).reset_index(drop=True)

            print(colored(f"   ✓ Sampled {len(sample_df)} rows (stratified by Output)", "green"))

        except Exception as e:
            print(colored(f"   ⚠️ Sampling failed: {e} - falling back to random sample", "yellow"))
            sample_df = df.sample(n=min(SAMPLE_SIZE, len(df)), random_state=sample_seed).reset_index(drop=True)

        # Predict on this sample
        predictions = predict_batch(client, rules, sample_df)
        if predictions:
            accuracy = calculate_accuracy(predictions, sample_df)
            accuracies[sample_id] = accuracy
            print(colored(f"   📊 Accuracy: {accuracy:.1%}", "yellow"))
        else:
            accuracies[sample_id] = None
            print(colored(f"   ❌ Failed", "red"))

    # Start parallel threads
    for sample_id in range(1, NUM_SAMPLES + 1):
        thread = threading.Thread(target=predict_sample, args=(sample_id,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Print final results
    print(colored("\n🏁 MULTI-SAMPLE TEST RESULTS", "green"))
    print(colored(f"   🤖 Model: {MODEL_NAME}", "cyan"))

    # Calculate and print average accuracy
    valid_accuracies = [acc for acc in accuracies.values() if acc is not None]
    avg_accuracy = None
    if valid_accuracies:
        avg_accuracy = sum(valid_accuracies) / len(valid_accuracies)
        print(colored(f"   📈 Average Accuracy: {avg_accuracy:.1%} (from {len(valid_accuracies)}/{NUM_SAMPLES} successful samples)", "magenta"))
    else:
        print(colored("   ❌ No successful samples to calculate average", "red"))

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

        summary_file = f"accuracies_summary_{avg_pct_str}{SAMPLE_SIZE}_samples_{NUM_SAMPLES}_different_{timestamp}.json"
        summary = {
            "sample_size": SAMPLE_SIZE,
            "num_samples": NUM_SAMPLES,
            "rules_file": RULES_FILE_PATH,
            "accuracies": accuracies,
            "average_accuracy": round(avg_accuracy, 4) if avg_accuracy is not None else None,
            "successful_samples": len(valid_accuracies) if valid_accuracies else 0
        }
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        print(colored(f"   🗂️ Accuracies summary saved: {summary_file}", "cyan"))
    except Exception as e:
        print(colored(f"⚠️ Failed to save accuracies summary: {e}", "yellow"))


if __name__ == "__main__":
    main()

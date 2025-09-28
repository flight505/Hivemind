import os
import pandas as pd
import json
from openai import OpenAI
from termcolor import colored
import datetime

# IMPORTANT VARIABLES (ALL CAPS AS REQUESTED)
USE_OPENAI_OR_OPENROUTER = "OPENROUTER"  # Options: "OPENAI" or "OPENROUTER"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "deepseek/deepseek-chat-v3.1"
REASONING_EFFORT = "high"
CSV_FILE_PATH = "train.csv"
FIRST_ROWS_TO_ANALYZE = 10  # Initial rows for metrics generation
ITERATIONS = 100  # Number of iterative predictions to perform
ROLLING_WINDOW_SIZE = 20  # Number of predictions to track for rolling accuracy
PREDICTION_FOLDER = "prediction_metrics_ds3-1"

# CREATE PREDICTION METRICS FOLDER
os.makedirs(PREDICTION_FOLDER, exist_ok=True)

def setup_openai_client():
    """Set up OpenAI client based on provider selection"""
    try:
        if USE_OPENAI_OR_OPENROUTER.upper() == "OPENROUTER":
            client = OpenAI(
                api_key=OPENROUTER_API_KEY,
                base_url="https://openrouter.ai/api/v1"
            )
            print(colored("✓ OpenAI client configured for OpenRouter", "green"))
        elif USE_OPENAI_OR_OPENROUTER.upper() == "OPENAI":
            client = OpenAI(api_key=OPENAI_API_KEY)
            print(colored("✓ OpenAI client configured for OpenAI", "green"))
        else:
            print(colored(f"⚠️  Invalid provider '{USE_OPENAI_OR_OPENROUTER}'. Use 'OPENAI' or 'OPENROUTER'", "yellow"))
            return None

        return client
    except Exception as e:
        print(colored(f"✗ Failed to setup OpenAI client: {e}", "red"))
        return None

def unified_api_call(client, messages, response_format=None, reasoning_effort=None):
    """Unified function for making API calls to either OpenAI or OpenRouter"""
    try:
        # Build the request parameters
        request_params = {
            "model": MODEL_NAME,
            "messages": messages
        }

        # Add optional parameters if provided
        if response_format:
            request_params["response_format"] = response_format

        if reasoning_effort and USE_OPENAI_OR_OPENROUTER.upper() == "OPENROUTER":
            request_params["reasoning_effort"] = reasoning_effort

        # Make the API call
        response = client.chat.completions.create(**request_params)

        return response.choices[0].message.content

    except Exception as e:
        print(colored(f"✗ API call failed: {e}", "red"))
        return None

def generate_predictive_metrics(client, data_rows):
    """Generate initial predictive metrics from first 10 rows"""
    try:
        print(colored("\n🔍 Generating predictive metrics from first 10 rows...", "blue"))

        data_summary = data_rows.to_string(index=False)

        prompt = f"""
You are creating  predictive metrics for Spaceship Titanic passenger transport prediction.

DATA: {data_summary}

OUTPUT FORMAT:
**Predictive Rules:**
- Rule 1: [condition] → [prediction] (confidence: high/medium/low)
- Rule 2: [condition] → [prediction] (confidence: high/medium/low)

**Key Probabilities:**
- Baseline transport rate: X%
- [Feature]: [value] → X% transport probability
- [Feature]: [value] → X% transport probability

**Critical Patterns:**
- [Pattern] → [prediction confidence]
- [Pattern] → [prediction confidence]

Keep it focused and actionable for prediction. No verbose analysis.
"""

        messages = [
            {"role": "system", "content": "You are a concise predictive model. Provide only essential prediction rules, probabilities, and patterns. No verbose analysis or recommendations."},
            {"role": "user", "content": prompt}
        ]

        metrics = unified_api_call(client, messages, reasoning_effort=REASONING_EFFORT)

        if metrics:
            print(colored("✓ Predictive metrics generated successfully", "green"))
            return metrics
        else:
            print(colored("✗ Failed to generate predictive metrics", "red"))
            return None

    except Exception as e:
        print(colored(f"✗ Metrics generation failed: {e}", "red"))
        return None

def predict_single_row(client, metrics, passenger_data):
    """Predict transported status for a single passenger using current metrics"""
    try:
        passenger_summary = passenger_data.to_string(index=False)

        prompt = f"""
Using the following predictive metrics, predict whether this passenger will be transported:

CURRENT PREDICTIVE METRICS:
{metrics}

PASSENGER DATA TO PREDICT:
{passenger_summary}

Based on the predictive metrics above, analyze this passenger's data and provide:
1. Your prediction (true/false for transported)
2. Confidence level (high/medium/low)
3. Key factors that influenced your decision
4. Any uncertainties or caveats

Return your response in JSON format:
{{"prediction": true, "confidence": "high", "reasoning": "brief explanation"}}
"""

        messages = [
            {"role": "system", "content": "You are a predictive analyst using established metrics to make individual predictions. Always respond with valid JSON."},
            {"role": "user", "content": prompt}
        ]

        prediction_raw = unified_api_call(client, messages, response_format={"type": "json_object"})

        if prediction_raw:
            try:
                prediction_data = json.loads(prediction_raw)
                return prediction_data
            except json.JSONDecodeError:
                print(colored("⚠️ Failed to parse prediction JSON", "yellow"))
                return None
        else:
            return None

    except Exception as e:
        print(colored(f"✗ Single row prediction failed: {e}", "red"))
        return None

def adjust_metrics_with_error(client, current_metrics, passenger_data, actual_result, predicted_result):
    """Adjust predictive metrics based on prediction error"""
    try:
        print(colored(f"\n🔧 Adjusting metrics after prediction error...", "yellow"))

        passenger_summary = passenger_data.to_string(index=False)

        prompt = f"""
ADJUST METRICS FOR PREDICTION ERROR:

CURRENT METRICS: {current_metrics}

ERROR CASE:
Data: {passenger_summary}
Predicted: {predicted_result}
Actual: {actual_result}

Provide UPDATED predictive metrics that fix this error:

**Updated Predictive Rules:**
- Rule 1: [condition] → [prediction] (confidence: high/medium/low)
- Rule 2: [condition] → [prediction] (confidence: high/medium/low)

**Updated Key Probabilities:**
- Baseline transport rate: X%
- [Feature]: [value] → X% transport probability

**Updated Critical Patterns:**
- [Pattern] → [prediction confidence]

Focus only on essential changes needed for better prediction. Keep concise.
"""

        messages = [
            {"role": "system", "content": "You are a concise adaptive model. Update only essential prediction rules, probabilities, and patterns based on the error. No verbose analysis."},
            {"role": "user", "content": prompt}
        ]

        updated_metrics = unified_api_call(client, messages, reasoning_effort=REASONING_EFFORT)

        if updated_metrics:
            print(colored("✓ Metrics adjusted successfully", "green"))
            return updated_metrics
        else:
            print(colored("✗ Failed to adjust metrics", "red"))
            return current_metrics  # Return original metrics if adjustment fails

    except Exception as e:
        print(colored(f"✗ Metrics adjustment failed: {e}", "red"))
        return current_metrics

def save_metrics_to_file(metrics, iteration_number):
    """Save metrics to a timestamped file in prediction_metrics folder"""
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{PREDICTION_FOLDER}/metrics_iteration_{iteration_number}_{timestamp}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"PREDICTIVE METRICS - ITERATION {iteration_number}\n")
            f.write("=" * 60 + "\n\n")
            f.write(metrics)
            f.write("\n\n" + "=" * 60)

        print(colored(f"📁 Metrics saved to: {filename}", "cyan"))
        return filename

    except Exception as e:
        print(colored(f"⚠️ Failed to save metrics: {e}", "yellow"))
        return None

def load_and_prepare_data():
    """Load the dataset and prepare first 10 rows for metrics generation"""
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        print(colored(f"✓ Loaded dataset with {len(df)} total rows", "green"))

        # Get first 10 rows for metrics generation
        initial_rows = df.head(FIRST_ROWS_TO_ANALYZE)
        print(colored(f"✓ Prepared first {FIRST_ROWS_TO_ANALYZE} rows for metrics generation", "green"))

        # Get remaining rows for iterative prediction (with actual values for validation)
        remaining_rows = df.iloc[FIRST_ROWS_TO_ANALYZE:].copy()
        print(colored(f"✓ Prepared {len(remaining_rows)} rows for iterative prediction", "green"))

        return initial_rows, remaining_rows
    except Exception as e:
        print(colored(f"✗ Failed to load data: {e}", "red"))
        return None, None







def main():
    """Main execution function with iterative adaptive prediction"""
    print(colored("🚀 Starting Spaceship Titanic Iterative Adaptive Prediction", "cyan"))
    print(colored(f"📡 Using {USE_OPENAI_OR_OPENROUTER} API provider", "cyan"))
    print(colored(f"🎯 Target: {ITERATIONS} iterative predictions", "cyan"))
    print(colored("=" * 60, "cyan"))

    # Check if API key is set based on provider
    if USE_OPENAI_OR_OPENROUTER.upper() == "OPENROUTER":
        if not OPENROUTER_API_KEY or OPENROUTER_API_KEY == "YOUR_OPENROUTER_API_KEY_HERE":
            print(colored("⚠️  Please set your OpenRouter API key in the OPENROUTER_API_KEY environment variable", "yellow"))
            print(colored("   Get your API key from: https://openrouter.ai/keys", "yellow"))
            return
    elif USE_OPENAI_OR_OPENROUTER.upper() == "OPENAI":
        if not OPENAI_API_KEY or OPENAI_API_KEY == "YOUR_OPENAI_API_KEY_HERE":
            print(colored("⚠️  Please set your OpenAI API key in the OPENAI_API_KEY environment variable", "yellow"))
            print(colored("   Get your API key from: https://platform.openai.com/api-keys", "yellow"))
            return
    else:
        print(colored(f"⚠️  Invalid provider '{USE_OPENAI_OR_OPENROUTER}'. Please set USE_OPENAI_OR_OPENROUTER to 'OPENAI' or 'OPENROUTER'", "yellow"))
        return

    # Setup OpenAI client
    client = setup_openai_client()
    if not client:
        return

    # Load and prepare data
    initial_rows, remaining_rows = load_and_prepare_data()
    if initial_rows is None or remaining_rows is None:
        return

    # Generate initial predictive metrics
    current_metrics = generate_predictive_metrics(client, initial_rows)
    if not current_metrics:
        return

    # Save initial metrics
    save_metrics_to_file(current_metrics, 0)

    # Display initial metrics
    print(colored("\n📊 INITIAL PREDICTIVE METRICS:", "magenta"))
    print(colored("-" * 40, "magenta"))
    print(current_metrics[:500] + "..." if len(current_metrics) > 500 else current_metrics)

    # Initialize tracking variables
    correct_predictions = 0
    total_predictions = 0
    adjustments_made = 0

    # Rolling accuracy tracking (last 20 predictions)
    rolling_window_size = ROLLING_WINDOW_SIZE
    recent_predictions = []

    print(colored(f"\n🔄 Starting {ITERATIONS} iterative predictions...", "blue"))
    print(colored(f"📊 Rolling accuracy window: {rolling_window_size} predictions", "blue"))

    # Iterative prediction loop
    for iteration in range(1, ITERATIONS + 1):
        print(colored(f"\n📍 ITERATION {iteration}/{ITERATIONS}", "blue"))

        # Check if we have enough remaining rows
        if len(remaining_rows) == 0:
            print(colored(f"⚠️  Ran out of data after {iteration-1} iterations", "yellow"))
            break

        # Get next passenger to predict (exclude Transported column)
        current_passenger = remaining_rows.iloc[0:1].drop(columns=['Transported'])
        actual_transported = remaining_rows.iloc[0]['Transported']

        print(colored(f"🎯 Predicting Passenger ID: {current_passenger.iloc[0]['PassengerId']}", "cyan"))

        # Make prediction using current metrics
        prediction_result = predict_single_row(client, current_metrics, current_passenger)

        if not prediction_result:
            print(colored("⚠️  Prediction failed, skipping this iteration", "yellow"))
            remaining_rows = remaining_rows.iloc[1:]  # Remove this row and continue
            continue

        predicted_transported = prediction_result['prediction']
        confidence = prediction_result.get('confidence', 'unknown')

        print(colored(f"🔮 Prediction: {predicted_transported} (confidence: {confidence})", "white"))
        print(colored(f"🎯 Actual: {actual_transported}", "white"))

        # Check if prediction was correct
        is_correct = predicted_transported == actual_transported
        total_predictions += 1

        # Add to rolling window
        recent_predictions.append(is_correct)
        if len(recent_predictions) > rolling_window_size:
            recent_predictions.pop(0)

        if is_correct:
            correct_predictions += 1
            print(colored("✅ CORRECT PREDICTION!", "green"))
        else:
            adjustments_made += 1
            print(colored("❌ INCORRECT PREDICTION - Adjusting metrics...", "red"))

            # Adjust metrics based on error
            current_metrics = adjust_metrics_with_error(
                client,
                current_metrics,
                current_passenger,
                actual_transported,
                predicted_transported
            )

            # Save updated metrics
            save_metrics_to_file(current_metrics, iteration)

        # Remove this passenger from remaining rows
        remaining_rows = remaining_rows.iloc[1:]

        # Calculate and display rolling accuracy metrics
        cumulative_accuracy = correct_predictions / total_predictions if total_predictions > 0 else 0
        rolling_correct = sum(recent_predictions)
        rolling_accuracy = rolling_correct / len(recent_predictions) if recent_predictions else 0

        print(colored(f"📊 Cumulative: {cumulative_accuracy:.1%} ({correct_predictions}/{total_predictions})", "yellow"))
        print(colored(f"📈 Rolling ({len(recent_predictions)}): {rolling_accuracy:.1%} ({rolling_correct}/{len(recent_predictions)})", "cyan"))
        print(colored(f"🔧 Adjustments: {adjustments_made}", "magenta"))

    # Final results
    print(colored("\n🎉 ITERATIVE PREDICTION COMPLETED!", "green"))
    print(colored("=" * 60, "green"))

    final_accuracy = correct_predictions / total_predictions if total_predictions > 0 else 0

    # Calculate final rolling accuracy
    final_rolling_correct = sum(recent_predictions)
    final_rolling_accuracy = final_rolling_correct / len(recent_predictions) if recent_predictions else 0

    print(colored(f"📊 FINAL RESULTS:", "cyan"))
    print(colored(f"   Total Predictions: {total_predictions}", "white"))
    print(colored(f"   Correct Predictions: {correct_predictions}", "white"))
    print(colored(f"   Final Accuracy: {final_accuracy:.1%}", "yellow"))
    print(colored(f"   Final Rolling ({len(recent_predictions)}): {final_rolling_accuracy:.1%}", "cyan"))
    print(colored(f"   Metrics Adjustments: {adjustments_made}", "white"))
    print(colored(f"   Metrics Files Saved: {adjustments_made + 1} (including initial)", "white"))

    print(colored("\n✅ Adaptive learning prediction system completed!", "green"))

if __name__ == "__main__":
    main()

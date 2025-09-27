import os
import pandas as pd
import json
from openai import OpenAI
from termcolor import colored
import os
import datetime

# IMPORTANT VARIABLES (ALL CAPS AS REQUESTED)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = "x-ai/grok-4"
REASONING_EFFORT = "high"
CSV_FILE_PATH = "train.csv"
FIRST_ROWS_TO_ANALYZE = 500
ROWS_TO_PREDICT = 50

# DYNAMICALLY CALCULATE PREDICTION ROWS (right after analysis rows)
START_PREDICTION_ROW = FIRST_ROWS_TO_ANALYZE + 1  # First row after analysis
END_PREDICTION_ROW = START_PREDICTION_ROW + ROWS_TO_PREDICT - 1  # Last row to predict

def setup_openai_client():
    """Set up OpenAI client configured for OpenRouter"""
    try:
        client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )
        print(colored("✓ OpenAI client configured for OpenRouter", "green"))
        return client
    except Exception as e:
        print(colored(f"✗ Failed to setup OpenAI client: {e}", "red"))
        return None

def load_and_prepare_data():
    """Load the dataset and prepare first 50 rows for analysis"""
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        print(colored(f"✓ Loaded dataset with {len(df)} total rows", "green"))

        # Get first 50 rows for analysis
        first_50_rows = df.head(FIRST_ROWS_TO_ANALYZE)
        print(colored(f"✓ Prepared first {FIRST_ROWS_TO_ANALYZE} rows for analysis", "green"))

        # Get rows 51-100 for prediction (EXCLUDE the Transported column!)
        prediction_rows = df.iloc[START_PREDICTION_ROW-1:END_PREDICTION_ROW].drop(columns=['Transported'])
        print(colored(f"✓ Prepared rows {START_PREDICTION_ROW}-{END_PREDICTION_ROW} for prediction (without labels) - {ROWS_TO_PREDICT} rows total", "green"))

        return first_50_rows, prediction_rows
    except Exception as e:
        print(colored(f"✗ Failed to load data: {e}", "red"))
        return None, None

def create_analysis_prompt(data_rows):
    """Create prompt for analyzing the dataset patterns"""
    data_summary = data_rows.to_string(index=False)

    prompt = f"""
You are analyzing a Spaceship Titanic dataset. The target variable is "Transported" which indicates whether passengers were transported to another dimension.

Please analyze the first {len(data_rows)} rows of this dataset and identify patterns that determine whether a passenger gets transported:

DATASET COLUMNS:
- PassengerId: Unique passenger identifier
- HomePlanet: Origin planet (Earth, Europa, Mars)
- CryoSleep: Whether passenger was in cryogenic sleep
- Cabin: Cabin location (deck/section/side)
- Destination: Travel destination
- Age: Passenger age
- VIP: VIP status
- RoomService, FoodCourt, ShoppingMall, Spa, VRDeck: Spending on amenities
- Name: Passenger name
- Transported: Target - whether transported to another dimension

FIRST {len(data_rows)} ROWS OF DATA:
{data_summary}

Please analyze these patterns:
1. What factors most strongly correlate with being transported?
2. Are there any clear patterns in spending, age, home planet, or cabin location?
3. What are the key indicators that suggest a passenger will or won't be transported?

Provide a detailed analysis that I can use to predict the next 50 rows.
"""

    return prompt

def create_prediction_prompt(analysis, prediction_data):
    """Create prompt for predicting the next rows (dynamically calculated)"""
    prediction_summary = prediction_data.to_string(index=False)

    prompt = f"""
Based on your analysis of the first {FIRST_ROWS_TO_ANALYZE} rows, predict the "Transported" status for the next {ROWS_TO_PREDICT} rows (rows {START_PREDICTION_ROW}-{END_PREDICTION_ROW}).

ANALYSIS: {analysis}

PASSENGER DATA TO PREDICT:
{prediction_summary}

Return a JSON object with a single key "predictions" containing an array of objects. Each prediction object must have exactly these fields:
- passengerId: string (the passenger ID)
- prediction: boolean (true/false for transported)

Example: {{"predictions": [{{"passengerId": "0{START_PREDICTION_ROW:03d}_01", "prediction": true}}]}}
"""

    return prompt

def parse_predictions(predictions_json):
    """Parse JSON predictions and return formatted results"""
    try:
        data = json.loads(predictions_json)

        # Handle both nested and direct array formats
        if isinstance(data, dict) and 'predictions' in data:
            predictions = data['predictions']
        elif isinstance(data, list):
            predictions = data
        else:
            print(colored("⚠️ Warning: Unexpected JSON structure", "yellow"))
            return predictions_json

        if not isinstance(predictions, list):
            print(colored("⚠️ Warning: Predictions are not in expected list format", "yellow"))
            return predictions_json

        formatted_predictions = []
        for pred in predictions:
            if isinstance(pred, dict) and 'passengerId' in pred and 'prediction' in pred:
                formatted_predictions.append(f"{pred['passengerId']}: {pred['prediction']}")
            else:
                print(colored(f"⚠️ Warning: Invalid prediction format: {pred}", "yellow"))

        if formatted_predictions:
            return "\n".join(formatted_predictions)
        else:
            return predictions_json

    except json.JSONDecodeError as e:
        print(colored(f"⚠️ JSON parsing failed: {e}", "yellow"))
        print(colored("Falling back to raw text output", "yellow"))
        return predictions_json

def calculate_accuracy(predictions, actual_values):
    """Calculate prediction accuracy and return detailed metrics"""
    try:
        # Parse predictions if they're in JSON format
        if isinstance(predictions, str):
            data = json.loads(predictions)
            if isinstance(data, dict) and 'predictions' in data:
                pred_list = data['predictions']
            elif isinstance(data, list):
                pred_list = data
            else:
                print(colored("⚠️ Unable to parse predictions for accuracy calculation", "yellow"))
                return None
        else:
            pred_list = predictions

        # Extract passenger IDs and predictions
        pred_dict = {}
        for pred in pred_list:
            if isinstance(pred, dict) and 'passengerId' in pred and 'prediction' in pred:
                pred_dict[pred['passengerId']] = pred['prediction']

        # Compare with actual values
        correct = 0
        total = 0
        results = []

        for passenger_id, actual in actual_values.items():
            if passenger_id in pred_dict:
                predicted = pred_dict[passenger_id]
                is_correct = predicted == actual
                if is_correct:
                    correct += 1
                total += 1
                results.append({
                    'passengerId': passenger_id,
                    'predicted': predicted,
                    'actual': actual,
                    'correct': is_correct
                })

        accuracy = correct / total if total > 0 else 0

        return {
            'total_predictions': total,
            'correct_predictions': correct,
            'accuracy': accuracy,
            'results': results
        }

    except Exception as e:
        print(colored(f"⚠️ Error calculating accuracy: {e}", "yellow"))
        return None

def generate_accuracy_report(model_name, accuracy_data):
    """Generate a JSON report with model name, row counts, and accuracy"""
    if not accuracy_data:
        return None

    report = {
        'model_name': model_name,
        'reasoning_effort': REASONING_EFFORT,
        'total_rows_analyzed': FIRST_ROWS_TO_ANALYZE,
        'total_rows_predicted': accuracy_data['total_predictions'],
        'correct_predictions': accuracy_data['correct_predictions'],
        'accuracy_percentage': round(accuracy_data['accuracy'] * 100, 2)
    }
    #save report to json file
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    model_name_clean = MODEL_NAME.replace("/", "_").replace("-", "_")
    reasoning_clean = REASONING_EFFORT.replace("/", "_").replace("-", "_") if REASONING_EFFORT else "none"
    filename = f'accuracy_report_{model_name_clean}_reasoning_{reasoning_clean}_{timestamp}.json'

    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)

    print(colored(f"📁 Report saved to: {filename}", "cyan"))

    return report

def analyze_dataset(client, data_rows):
    """Send analysis request to the AI model"""
    try:
        print(colored("\n🔍 Analyzing first 50 rows for patterns...", "blue"))

        prompt = create_analysis_prompt(data_rows)

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are an expert data analyst specializing in pattern recognition and predictive modeling."},
                {"role": "user", "content": prompt},
                
            ],
            reasoning_effort=REASONING_EFFORT
        )

        analysis = response.choices[0].message.content
        print(colored("✓ Analysis completed successfully", "green"))

        return analysis

    except Exception as e:
        print(colored(f"✗ Analysis failed: {e}", "red"))
        return None

def predict_next_rows(client, analysis, prediction_data):
    """Send prediction request to the AI model"""
    try:
        print(colored("\n🔮 Predicting next 50 rows based on analysis...", "blue"))

        prompt = create_prediction_prompt(analysis, prediction_data)

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are an expert predictive analyst making data-driven predictions based on identified patterns. Always respond with valid JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )

        predictions_raw = response.choices[0].message.content
        print(colored("✓ Predictions completed successfully", "green"))

        # Parse the JSON predictions for better formatting
        predictions_formatted = parse_predictions(predictions_raw)

        # Return both raw (for accuracy) and formatted (for display)
        return predictions_raw, predictions_formatted

    except Exception as e:
        print(colored(f"✗ Prediction failed: {e}", "red"))
        return None

def load_actual_values():
    """Load actual transported values for prediction rows (dynamically calculated)"""
    try:
        df = pd.read_csv(CSV_FILE_PATH)

        # Get prediction rows dynamically (0-indexed)
        actual_rows = df.iloc[START_PREDICTION_ROW-1:END_PREDICTION_ROW]

        # Create dictionary of passenger_id -> transported value
        actual_values = {}
        for _, row in actual_rows.iterrows():
            actual_values[row['PassengerId']] = row['Transported']

        print(colored(f"✓ Loaded actual values for {len(actual_values)} passengers", "green"))
        return actual_values

    except Exception as e:
        print(colored(f"✗ Failed to load actual values: {e}", "red"))
        return None

def main():
    """Main execution function"""
    print(colored("🚀 Starting Spaceship Titanic Analysis & Prediction", "cyan"))
    print(colored("=" * 60, "cyan"))

    # Check if API key is set
    if OPENROUTER_API_KEY == "YOUR_OPENROUTER_API_KEY_HERE":
        print(colored("⚠️  Please set your OpenRouter API key in the OPENROUTER_API_KEY variable", "yellow"))
        print(colored("   Get your API key from: https://openrouter.ai/keys", "yellow"))
        return

    # Setup OpenAI client
    client = setup_openai_client()
    if not client:
        return

    # Load and prepare data
    first_50_rows, prediction_rows = load_and_prepare_data()
    if first_50_rows is None or prediction_rows is None:
        return

    # Load actual values for accuracy calculation
    actual_values = load_actual_values()
    if actual_values is None:
        return

    # Analyze the first 50 rows
    analysis = analyze_dataset(client, first_50_rows)
    if not analysis:
        return

    # Display analysis
    print(colored("\n📊 ANALYSIS RESULTS:", "magenta"))
    print(colored("-" * 40, "magenta"))
    print(analysis)

    # Predict the next 50 rows
    prediction_result = predict_next_rows(client, analysis, prediction_rows)
    if not prediction_result:
        return

    predictions_raw, predictions_formatted = prediction_result

    # Calculate accuracy
    print(colored("\n📈 CALCULATING ACCURACY...", "blue"))
    accuracy_data = calculate_accuracy(predictions_raw, actual_values)

    if accuracy_data:
        print(colored("\n✅ ACCURACY RESULTS:", "green"))
        print(colored("-" * 40, "green"))
        print(f"Total Predictions: {accuracy_data['total_predictions']}")
        print(f"Correct Predictions: {accuracy_data['correct_predictions']}")
        print(colored(f"Accuracy: {accuracy_data['accuracy']:.1%}", "yellow"))

        # Generate JSON report
        report = generate_accuracy_report(MODEL_NAME, accuracy_data)
        if report:
            print(colored("\n📋 JSON REPORT:", "cyan"))
            print(colored("-" * 40, "cyan"))
            print(json.dumps(report, indent=2))

    print(colored("\n✅ Analysis, prediction, and accuracy evaluation completed!", "green"))

if __name__ == "__main__":
    main()

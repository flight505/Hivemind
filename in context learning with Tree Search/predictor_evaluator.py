import pandas as pd
from termcolor import colored
import sys
import os
import importlib.util

async def evaluate_predictor(csv_file="complex_dataset.csv", output_file="generated_predictor.py"):
    """Evaluate the generated predictor function against the entire dataset."""
    try:
        # Load the full dataset
        df = pd.read_csv(csv_file)
        total_rows = len(df)
        print(colored(f"📈 Testing on {total_rows} rows from dataset", "cyan"))

        # Import the generated predictor function
        sys.path.append(os.getcwd())
        spec = importlib.util.spec_from_file_location("predictor_module", output_file)
        predictor_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(predictor_module)
        predict_function = predictor_module.predict_output

        # Make predictions and calculate accuracy
        correct_predictions = 0
        category_correct = {1: 0, 2: 0, 3: 0, 4: 0}
        category_total = {1: 0, 2: 0, 3: 0, 4: 0}
        mistakes = []  # Store prediction mistakes for improvement

        for idx, row in df.iterrows():
            A, B, C, D, E = row['A'], row['B'], row['C'], row['D'], row['E']
            actual_output = row['Output']

            try:
                predicted_output = predict_function(A, B, C, D, E)
                category_total[actual_output] += 1

                if predicted_output == actual_output:
                    correct_predictions += 1
                    category_correct[actual_output] += 1
                else:
                    # Store mistake for improvement
                    mistakes.append({
                        'index': idx,
                        'input': {'A': A, 'B': B, 'C': C, 'D': D, 'E': E},
                        'predicted': predicted_output,
                        'actual': actual_output,
                        'error': None
                    })

            except Exception as e:
                print(colored(f"⚠️  Execution error in row {idx}: {e}", "red"))
                # Store execution error for improvement
                mistakes.append({
                    'index': idx,
                    'input': {'A': A, 'B': B, 'C': C, 'D': D, 'E': E},
                    'predicted': None,
                    'actual': actual_output,
                    'error': str(e)
                })
                continue

        # Calculate and display results
        overall_accuracy = (correct_predictions / total_rows) * 100

        print(colored("\n🎯 PREDICTION RESULTS:", "green"))
        print(colored("=" * 50, "green"))
        print(colored(f"Overall Accuracy: {overall_accuracy:.2f}% ({correct_predictions}/{total_rows})", "green"))
        print(colored("\n📋 Category-wise Accuracy:", "cyan"))

        for category in [1, 2, 3, 4]:
            if category_total[category] > 0:
                category_accuracy = (category_correct[category] / category_total[category]) * 100
                print(colored(f"Category {category}: {category_accuracy:.2f}% ({category_correct[category]}/{category_total[category]})", "cyan"))
            else:
                print(colored(f"Category {category}: No samples", "yellow"))

        # Count execution errors separately
        execution_errors = [m for m in mistakes if m.get('error')]
        prediction_errors = [m for m in mistakes if not m.get('error')]

        # Return evaluation results including mistakes
        return {
            'overall_accuracy': overall_accuracy,
            'correct_predictions': correct_predictions,
            'total_rows': total_rows,
            'mistakes': mistakes,
            'execution_errors': execution_errors,
            'prediction_errors': prediction_errors,
            'num_execution_errors': len(execution_errors),
            'num_prediction_errors': len(prediction_errors)
        }

    except Exception as e:
        print(colored(f"❌ Error during evaluation: {e}", "red"))
        return None

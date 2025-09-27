import csv
from termcolor import colored

# THIS SCRIP WAS CREATED BY GPT-5-THINKING IN CHATGPT. YOU CAN READ THE CHAT HERE: https://chatgpt.com/share/68ba4ec5-6cf0-8009-b1e3-84a1b8f88ccf

def predict_output(a, b, c, d, e):
    """
    Predict Output in {1,2,3,4} from inputs A,B,C,D,E.
    Model: multinomial logistic regression trained on the provided 100 rows.
    Scaling: z = (x - mean) / std for each feature.
    """
    # z-score parameters learned from your data
    means = [49.98, 53.18, 48.98, 46.91, 47.06]
    scales = [28.845443314326097,
              28.65462615355503,
              29.876405406273356,
              29.876778608143148,
              28.905646507213774]

    # coefficients per class in order [1, 2, 3, 4]
    coefs = [
        [ 1.4163089114120992,  1.1050587585598304, -0.22845366847057838, -0.8729060816819886,  0.40140945293440405],  # class 1
        [ 0.1464678738248410, -0.27421643468403195, -0.20405893767534686, -1.0865997292747156,  0.16940082433285147],  # class 2
        [-1.0097344828060157,  0.08882327546310387, -0.01071135339219417,  0.8699412781819507, -0.69116782065363110],  # class 3
        [-0.5530423024309243, -0.91966559933890260,  0.44322395953811930,  1.0895645327747538,  0.12035754338637632],  # class 4
    ]

    intercepts = [-0.14511279613959557,
                  -0.24938691762932835,
                   0.47648096806257884,
                  -0.08198125429365576]

    # standardize
    x = [a, b, c, d, e]
    z = [(x[i] - means[i]) / scales[i] for i in range(5)]

    # linear scores for each class
    scores = []
    for i in range(4):
        s = intercepts[i]
        for j in range(5):
            s += z[j] * coefs[i][j]
        scores.append(s)

    classes = [1, 2, 3, 4]
    return classes[max(range(4), key=lambda i: scores[i])]

def evaluate_on_dataset(csv_file='complex_dataset.csv'):
    """
    Evaluate the ChatGPT predictor on the entire dataset and calculate accuracy.
    """
    print(colored("=== ChatGPT Predictor Evaluation ===", "magenta"))
    print(colored("Evaluating multinomial logistic regression on complex dataset", "cyan"))

    # Read the dataset
    predictions = []
    actuals = []

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)

        for row_num, row in enumerate(reader, 1):
            # Get input features
            a = int(row['A'])
            b = int(row['B'])
            c = int(row['C'])
            d = int(row['D'])
            e = int(row['E'])
            actual = int(row['Output'])

            # Make prediction
            predicted = predict_output(a, b, c, d, e)

            predictions.append(predicted)
            actuals.append(actual)

            # Print progress every 1000 rows
            if row_num % 1000 == 0:
                print(colored(f"Processed {row_num} rows...", "green"))

    # Calculate accuracy
    correct_predictions = sum(1 for pred, act in zip(predictions, actuals) if pred == act)
    total_predictions = len(predictions)
    accuracy = correct_predictions / total_predictions

    # Print results
    print(colored("\n=== RESULTS ===", "magenta"))
    print(colored(f"Total samples evaluated: {total_predictions}", "cyan"))
    print(colored(f"Correct predictions: {correct_predictions}", "green"))
    print(colored(f"Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)", "green"))

    # Class-wise accuracy
    print(colored("\n=== CLASS-WISE ACCURACY ===", "yellow"))
    class_counts = {}
    class_correct = {}

    for pred, act in zip(predictions, actuals):
        if act not in class_counts:
            class_counts[act] = 0
            class_correct[act] = 0
        class_counts[act] += 1
        if pred == act:
            class_correct[act] += 1

    for class_label in sorted(class_counts.keys()):
        class_acc = class_correct[class_label] / class_counts[class_label]
        print(colored(f"Class {class_label}: {class_acc:.4f} ({class_correct[class_label]}/{class_counts[class_label]})", "yellow"))

    return accuracy

# Example usage:
# y_hat = predict_output(82, 15, 4, 95, 36)  # -> 4

if __name__ == "__main__":
    # Run evaluation on the dataset
    evaluate_on_dataset()

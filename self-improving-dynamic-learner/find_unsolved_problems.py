import pandas as pd
import os
import sys
import importlib.util
import traceback
from termcolor import colored
from collections import defaultdict
import multiprocessing as mp
import json
from tqdm import tqdm

# IMPORTANT VARIABLES
FOLDER_TO_TEST = "predictors-SKY"  # Folder containing predictor files
CSV_FILE = "complex_dataset.csv"  # Dataset file
PRINT_INTERVAL = 10  # Print stats every N predictors
TEMP_MODULE_NAME = "temp_predictor"  # Temporary name for dynamic imports
NUM_PROCESSES = 10  # Number of parallel processes
OUTPUT_JSON = "unsolved_rows.json"  # Output file for unsolved row indices

def load_dataset():
    """Load the dataset."""
    if not os.path.exists(CSV_FILE):
        print(colored(f"❌ Dataset file {CSV_FILE} not found!", "red"))
        return None
    try:
        df = pd.read_csv(CSV_FILE)
        print(colored(f"✅ Loaded dataset with {len(df)} rows", "green"))
        return df
    except Exception as e:
        print(colored(f"❌ Error loading dataset: {e}", "red"))
        return None

def load_predictor(filepath):
    """Dynamically load a predictor function from a file."""
    try:
        spec = importlib.util.spec_from_file_location(TEMP_MODULE_NAME, filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, 'predict_output'):
            return module.predict_output
        else:
            print(colored(f"⚠️  No predict_output function in {filepath}", "yellow"))
            return None
    except Exception as e:
        print(colored(f"❌ Error loading {filepath}: {e}", "red"))
        return None

def test_predictor_worker(filepath):
    """Worker function for multiprocessing: load predictor and test it."""
    # Load dataset (done in each process to avoid serialization issues)
    try:
        df = pd.read_csv(CSV_FILE)
    except Exception as e:
        return None  # Failed to load dataset

    # Load predictor
    predictor_func = load_predictor(filepath)
    if predictor_func is None:
        return None  # Failed to load predictor

    # Test predictor
    failed_rows = []
    for idx, row in df.iterrows():
        try:
            inputs = (row['A'], row['B'], row['C'], row['D'], row['E'])
            predicted = predictor_func(*inputs)
            if predicted != row['Output']:
                failed_rows.append(idx)
        except Exception as e:
            # Treat execution errors as failures
            failed_rows.append(idx)
    return failed_rows

def main():
    print(colored("🔍 Starting parallel predictor consistency test...", "cyan"))

    # Load dataset
    df = load_dataset()
    if df is None:
        return

    # Get predictor files
    if not os.path.exists(FOLDER_TO_TEST):
        print(colored(f"❌ Folder {FOLDER_TO_TEST} not found!", "red"))
        return

    predictor_files = [f for f in os.listdir(FOLDER_TO_TEST) if f.endswith('.py')]
    predictor_files.sort()  # Sort for consistent ordering

    if not predictor_files:
        print(colored(f"⚠️  No .py files found in {FOLDER_TO_TEST}", "yellow"))
        return

    print(colored(f"📂 Found {len(predictor_files)} predictor files to test", "cyan"))
    print(colored(f"🔄 Using {NUM_PROCESSES} parallel processes", "cyan"))

    # Create full filepaths
    filepaths = [os.path.join(FOLDER_TO_TEST, filename) for filename in predictor_files]

    # Run parallel testing with progress bar
    print(colored("🚀 Running parallel tests...", "cyan"))
    with mp.Pool(processes=NUM_PROCESSES) as pool:
        results = list(tqdm(
            pool.imap(test_predictor_worker, filepaths),
            total=len(filepaths),
            desc="Testing predictors",
            unit="predictor"
        ))

    # Aggregate results with progress bar
    row_failure_counts = defaultdict(int)
    total_predictors_tested = 0

    print(colored("📊 Aggregating results...", "cyan"))
    for failed_rows in tqdm(results, desc="Processing results", unit="result"):
        if failed_rows is not None:  # Skip if predictor failed to load
            for row_idx in failed_rows:
                row_failure_counts[row_idx] += 1
            total_predictors_tested += 1

    print(colored(f"\n🏁 Testing complete! Successfully tested {total_predictors_tested} predictors.", "green"))

    # Find unsolved rows (failed by ALL predictors)
    unsolved_indices = [idx for idx, count in row_failure_counts.items() if count == total_predictors_tested]
    unsolved_count = len(unsolved_indices)

    print(colored(f"🎯 Found {unsolved_count} rows unsolved by ALL {total_predictors_tested} predictors", "red"))
    print(colored(f"  • Total dataset rows: {len(df)}", "white"))
    print(colored(f"  • Percentage unsolved: {unsolved_count / len(df) * 100:.2f}%", "yellow"))

    # Save to JSON
    output_data = {
        "total_predictors_tested": total_predictors_tested,
        "total_dataset_rows": len(df),
        "unsolved_rows_count": unsolved_count,
        "unsolved_row_indices": unsolved_indices
    }

    with open(OUTPUT_JSON, 'w') as f:
        json.dump(output_data, f, indent=4)

    print(colored(f"💾 Saved unsolved row indices to {OUTPUT_JSON}", "cyan"))

    # Also save the unsolved rows to CSV for convenience
    if unsolved_indices:
        failing_df = df.iloc[unsolved_indices]
        failing_df.to_csv("consistently_failing_rows.csv", index=False)
        print(colored("💾 Also saved unsolved rows data to consistently_failing_rows.csv", "cyan"))

        # Show sample
        print(colored("\n📋 Sample of unsolved rows:", "yellow"))
        for idx in unsolved_indices[:5]:
            row = df.iloc[idx]
            print(colored(f"  Row {idx}: A={row['A']}, B={row['B']}, C={row['C']}, D={row['D']}, E={row['E']} → Output={row['Output']}", "red"))

if __name__ == "__main__":
    main()

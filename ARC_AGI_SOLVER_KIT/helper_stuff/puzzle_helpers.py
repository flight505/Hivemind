"""
ARC-AGI Puzzle Helper Functions

This module contains auxiliary functions for the ARC-AGI puzzle solver.
Functions for loading data, formatting prompts, and managing puzzle files.
"""

import json
import os
import glob
import random
from termcolor import colored


def save_puzzle_failures(api_failed_files, incorrect_files, output_file):
    """Save both API failed and incorrect puzzle file paths to a single Python file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Puzzle failure analysis - API failures and incorrect answers\n")
            f.write("# Generated automatically by solve_arc_puzzle.py\n")
            f.write("# Copy the lists below to retry failed puzzles\n\n")

            # Convert backslashes to forward slashes for better compatibility
            def format_path(path):
                return path.replace('\\', '/')

            # Save API failed puzzles
            f.write("# API Failed Puzzles - Failed during processing/API calls\n")
            f.write("API_FAILED_PUZZLE_FILES = [\n")
            for file_path in api_failed_files:
                f.write(f'    "{format_path(file_path)}",\n')
            f.write("]\n\n")

            # Save incorrect puzzles
            f.write("# Incorrect Puzzles - Successfully processed but gave wrong answers\n")
            f.write("INCORRECT_PUZZLE_FILES = [\n")
            for file_path in incorrect_files:
                f.write(f'    "{format_path(file_path)}",\n')
            f.write("]\n\n")

            # Create a combined list for easy copy-paste
            all_failed = api_failed_files + incorrect_files
            if all_failed:
                f.write("# ALL PROBLEMATIC PUZZLES - Copy this list to retry all failed puzzles\n")
                f.write("ALL_FAILED_PUZZLE_FILES = [\n")
                for file_path in all_failed:
                    f.write(f'    "{format_path(file_path)}",\n')
                f.write("]\n\n")

            # Summary statistics
            f.write(f"# Total API failed puzzles: {len(api_failed_files)}\n")
            f.write(f"# Total incorrect puzzles: {len(incorrect_files)}\n")
            f.write(f"# Total problematic puzzles: {len(api_failed_files) + len(incorrect_files)}\n\n")

            # Usage instructions
            f.write("# HOW TO USE:\n")
            f.write("# 1. Copy one of the lists above\n")
            f.write("# 2. In solve_arc_puzzle.py, replace PUZZLES = [] with:\n")
            if api_failed_files:
                f.write("#    PUZZLES = API_FAILED_PUZZLE_FILES.copy()\n")
            if incorrect_files:
                f.write("#    PUZZLES = INCORRECT_PUZZLE_FILES.copy()\n")
            if all_failed:
                f.write("#    PUZZLES = ALL_FAILED_PUZZLE_FILES.copy()\n")

        print(colored(f"💾 Saved {len(api_failed_files)} API failed and {len(incorrect_files)} incorrect puzzle paths to {output_file}", "yellow"))
        print(colored("💡 Copy the lists from puzzle_failures.py to retry failed puzzles", "cyan"))
        return True
    except Exception as e:
        print(colored(f"❌ Error saving puzzle lists to {output_file}: {str(e)}", "red"))
        return False


def get_puzzle_files(folder_path, count, puzzle_file=None, puzzle_files_list=None):
    """Get a list of puzzle files from the specified folder or use provided files."""
    # If a list of puzzle files is provided, validate and use them
    if puzzle_files_list and len(puzzle_files_list) > 0:
        valid_files = []
        for puzzle_file_path in puzzle_files_list:
            if os.path.exists(puzzle_file_path):
                valid_files.append(puzzle_file_path)
            else:
                print(colored(f"⚠️  Warning: Puzzle file not found: {puzzle_file_path}", "yellow"))

        if valid_files:
            print(colored(f"📂 Using {len(valid_files)} specific puzzle files from provided list", "blue"))
            return valid_files
        else:
            print(colored("❌ Error: No valid puzzle files found in the provided list", "red"))
            return []

    # If a specific single puzzle file is provided, use only that file (backward compatibility)
    if puzzle_file and os.path.exists(puzzle_file):
        print(colored(f"📂 Using specific puzzle file: {os.path.basename(puzzle_file)}", "blue"))
        return [puzzle_file]

    # If no specific files provided, use random selection from folder
    if not os.path.exists(folder_path):
        print(colored(f"❌ Error: Folder {folder_path} not found", "red"))
        return []

    json_files = glob.glob(os.path.join(folder_path, "*.json"))
    if not json_files:
        print(colored(f"⚠️  No JSON files found in {folder_path}", "yellow"))
        return []

    # Randomly select the specified number of files
    selected_files = random.sample(json_files, min(count, len(json_files)))
    print(colored(f"📂 Selected {len(selected_files)} puzzle files from {folder_path}", "blue"))
    return selected_files


def load_puzzle_data(file_path):
    """Load the ARC-AGI puzzle data from JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(colored(f"❌ Error: File {file_path} not found", "red"))
        return None
    except json.JSONDecodeError:
        print(colored(f"❌ Error: Invalid JSON in {file_path}", "red"))
        return None


def get_expected_output_dimensions(puzzle_data):
    """Extract the expected output dimensions from the puzzle data."""
    if "test" in puzzle_data and puzzle_data["test"]:
        expected_output = puzzle_data["test"][0]["output"]
        if expected_output and isinstance(expected_output, list):
            rows = len(expected_output)
            cols = len(expected_output[0]) if expected_output and isinstance(expected_output[0], list) else 0
            return rows, cols
    return None, None


def format_puzzle_for_model(puzzle_data):
    """Format the puzzle data for the AI model."""
    formatted = "ARC-AGI Puzzle Solver - Expert Level\n\n"

    # Get expected output dimensions
    expected_rows, expected_cols = get_expected_output_dimensions(puzzle_data)

    formatted += "TRAINING EXAMPLES (Study these carefully):\n"
    for i, example in enumerate(puzzle_data["train"], 1):
        formatted += f"Example {i}:\n"
        formatted += f"Input Grid: {example['input']}\n"
        formatted += f"Output Grid: {example['output']}\n\n"

    formatted += "YOUR TASK:\n"
    test_input = puzzle_data["test"][0]["input"]
    formatted += f"Input Grid: {test_input}\n"
    formatted += "Find the pattern from the training examples and generate the correct output grid.\n\n"

    formatted += "MANDATORY REQUIREMENTS (Follow these exactly):\n"
    formatted += "1. PATTERN ANALYSIS: Carefully analyze how each input transforms to its corresponding output\n"
    formatted += "2. CONSISTENT TRANSFORMATION: Apply the exact same transformation pattern to the test input\n"
    formatted += "3. OUTPUT FORMAT: Return ONLY a valid JSON array representing the output grid\n"

    if expected_rows and expected_cols:
        formatted += f"4. EXACT DIMENSIONS REQUIRED: Output MUST be exactly {expected_rows}x{expected_cols} (same as all training examples)\n"
        formatted += f"   - Exactly {expected_rows} rows\n"
        formatted += f"   - Each row must have exactly {expected_cols} columns\n"
        formatted += f"   - Count the dimensions twice before finalizing\n"

    formatted += "5. DATA TYPE: All values must be integers (0-9)\n"
    formatted += "6. STRUCTURE: Use proper nested array format [[row1], [row2], ...]\n"
    formatted += "7. NO EXTRA TEXT: Return only the JSON array, no explanations or additional content\n\n"

    formatted += "RESPONSE VALIDATION CHECKLIST:\n"
    formatted += "- [ ] Output is a valid JSON array\n"
    formatted += "- [ ] Contains only integers\n"
    formatted += "- [ ] Has correct dimensions\n"
    formatted += "- [ ] Follows the same pattern as training examples\n"
    formatted += "- [ ] No extra text or formatting\n\n"

    formatted += "CRITICAL: Incorrect dimensions or format will result in complete failure. Double-check your work."

    return formatted

"""
Parallel script to solve multiple ARC-AGI puzzles using OpenRouter/Sonoma Sky Alpha model
"""

import json
import os
import asyncio
import glob
import random
from termcolor import colored
from API_client import make_API_call
from helper_stuff.puzzle_helpers import (
    save_puzzle_failures,
    get_puzzle_files,
    load_puzzle_data,
    get_expected_output_dimensions,
    format_puzzle_for_model
)

# IMPORTANT VARIABLES (ALL CAPS AS REQUESTED)
PUZZLE_FOLDER = "ARC-AGI-2/data/training"
MODEL_NAME = "openrouter/sonoma-sky-alpha"
PROVIDER = "openrouter"
NUM_PUZZLES = 10
PUZZLE_FILE = ""  # Single puzzle file (for backward compatibility)
PUZZLES = []  # List of specific puzzle files to process. If not empty, these will be used instead of random selection
# Example: ["ARC-AGI-2/data/training/1a2e2828.json", "ARC-AGI-2/data/training/0f63c0b9.json"]
PUZZLE_FAILURES_FILE = "puzzle_failures.py" # SAVING BOTH API FAILED AND INCORRECT PUZZLES

async def solve_single_puzzle(puzzle_file):
    """Solve a single ARC-AGI puzzle using AI."""
    puzzle_name = os.path.basename(puzzle_file)
    print(colored(f"🎯 Processing puzzle: {puzzle_name}", "yellow"))

    # Load puzzle data
    puzzle_data = load_puzzle_data(puzzle_file)
    if not puzzle_data:
        return {"file": puzzle_name, "success": False, "error": "Failed to load puzzle"}

    # Format puzzle for the model
    puzzle_text = format_puzzle_for_model(puzzle_data)

    # Prepare messages for the AI
    messages = [
        {
            "role": "system",
            "content": """You are an expert ARC-AGI puzzle solver. Your task is to analyze grid transformation patterns and generate exact output grids. Always return only valid JSON arrays with correct dimensions. Never add extra text or explanations - only the JSON array output.
           """
        },
        {
            "role": "user",
            "content": puzzle_text
        }
    ]

    # Make API call
    response = await make_API_call(MODEL_NAME, messages, PROVIDER)

    result = {"file": puzzle_name, "success": False}

    if response and response.choices:
        ai_response = response.choices[0].message.content

        # Try to parse the AI response as JSON
        try:
            import re
            json_match = re.search(r'\[\[.*?\]\]', ai_response, re.DOTALL)
            if json_match:
                predicted_output = json.loads(json_match.group())
                expected_output = puzzle_data["test"][0]["output"]

                # Validate dimensions
                expected_rows, expected_cols = get_expected_output_dimensions(puzzle_data)
                dimension_match = True
                if expected_rows and expected_cols:
                    actual_rows = len(predicted_output) if isinstance(predicted_output, list) else 0
                    actual_cols = len(predicted_output[0]) if isinstance(predicted_output, list) and predicted_output and isinstance(predicted_output[0], list) else 0
                    dimension_match = (actual_rows == expected_rows and actual_cols == expected_cols)

                result.update({
                    "success": True,
                    "predicted": predicted_output,
                    "expected": expected_output,
                    "correct": predicted_output == expected_output,
                    "dimension_match": dimension_match,
                    "expected_dims": f"{expected_rows}x{expected_cols}" if expected_rows and expected_cols else "unknown",
                    "actual_dims": f"{len(predicted_output)}x{len(predicted_output[0]) if predicted_output and isinstance(predicted_output[0], list) else 0}" if isinstance(predicted_output, list) else "invalid",
                    "ai_response": ai_response[:200] + "..." if len(ai_response) > 200 else ai_response
                })
            else:
                result["error"] = "Could not extract JSON array from AI response"

        except json.JSONDecodeError:
            result["error"] = "Could not parse AI response as JSON"

    else:
        result["error"] = "Failed to get response from AI model"

    return result

async def solve_multiple_puzzles():
    """Solve multiple ARC-AGI puzzles in parallel."""
    print(colored("🚀 Starting Parallel ARC-AGI Puzzle Solver", "cyan"))
    print(colored(f"📂 Folder: {PUZZLE_FOLDER}", "blue"))
    print(colored(f"🔢 Number of puzzles: {NUM_PUZZLES}", "blue"))
    print(colored(f"🤖 Model: {MODEL_NAME}", "yellow"))

    # Get puzzle files
    puzzle_files = get_puzzle_files(PUZZLE_FOLDER, NUM_PUZZLES, PUZZLE_FILE, PUZZLES)
    if not puzzle_files:
        return

    print(colored("📡 Sending parallel requests to OpenRouter API...", "blue"))

    # Process puzzles in parallel
    tasks = [solve_single_puzzle(puzzle_file) for puzzle_file in puzzle_files]
    results = await asyncio.gather(*tasks)

    # Collect failed puzzle file paths (separate API failures from incorrect answers)
    api_failed_puzzle_files = []
    incorrect_puzzle_files = []
    for puzzle_file, result in zip(puzzle_files, results):
        if not result.get("success", False):
            # API or processing failed
            api_failed_puzzle_files.append(puzzle_file)
        elif result.get("success", False) and not result.get("correct", False):
            # Successfully processed but incorrect answer
            incorrect_puzzle_files.append(puzzle_file)

    # Display results
    print(colored("\n" + "="*60, "cyan"))
    print(colored("📊 RESULTS SUMMARY", "cyan", attrs=["bold"]))
    print(colored("="*60, "cyan"))

    correct_count = 0
    total_count = len(results)

    for i, result in enumerate(results, 1):
        print(colored(f"\n🧩 Puzzle {i}: {result['file']}", "white", attrs=["bold"]))

        if result["success"]:
            status = "✅ CORRECT" if result["correct"] else "❌ INCORRECT"
            color = "green" if result["correct"] else "red"
            print(colored(f"   Status: {status}", color))

            # Show dimension validation
            if "dimension_match" in result:
                dim_status = "✅ DIMENSIONS OK" if result["dimension_match"] else "⚠️  DIMENSION MISMATCH"
                dim_color = "green" if result["dimension_match"] else "yellow"
                print(colored(f"   Dimensions: {dim_status}", dim_color))
                print(colored(f"   Expected: {result.get('expected_dims', 'unknown')}", "blue"))
                print(colored(f"   Actual:   {result.get('actual_dims', 'unknown')}", "cyan"))

            if result["correct"]:
                correct_count += 1
            else:
                print(colored(f"   Predicted: {result['predicted']}", "red"))
                print(colored(f"   Expected:  {result['expected']}", "green"))
        else:
            print(colored(f"   Error: {result['error']}", "red"))

    # Overall statistics
    accuracy = (correct_count / total_count) * 100 if total_count > 0 else 0

    # Count dimension matches
    dimension_success_count = sum(1 for result in results if result.get("dimension_match", False))
    dimension_success_rate = (dimension_success_count / total_count) * 100 if total_count > 0 else 0

    # Save failed and incorrect puzzles if any
    if api_failed_puzzle_files or incorrect_puzzle_files:
        save_puzzle_failures(api_failed_puzzle_files, incorrect_puzzle_files, PUZZLE_FAILURES_FILE)

    print(colored("\n" + "="*60, "cyan"))
    print(colored("🏆 FINAL RESULTS", "cyan", attrs=["bold"]))
    print(colored(f"   Correct Solutions: {correct_count}/{total_count} ({accuracy:.1f}%)", "green" if correct_count > 0 else "red"))
    print(colored(f"   Correct Dimensions: {dimension_success_count}/{total_count} ({dimension_success_rate:.1f}%)", "blue"))
    if api_failed_puzzle_files or incorrect_puzzle_files:
        print(colored(f"   API Failed: {len(api_failed_puzzle_files)} | Incorrect: {len(incorrect_puzzle_files)} (saved to {PUZZLE_FAILURES_FILE})", "red"))
    print(colored("="*60, "cyan"))

if __name__ == "__main__":
    # Check if API key is set
    if not os.getenv("OPENROUTER_API_KEY"):
        print(colored("❌ Error: OPENROUTER_API_KEY environment variable not set", "red"))
        print(colored("Please set your OpenRouter API key before running this script", "yellow"))
    else:
        # Run the async function
        asyncio.run(solve_multiple_puzzles())

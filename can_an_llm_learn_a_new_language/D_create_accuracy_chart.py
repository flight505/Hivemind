#!/usr/bin/env python3
"""
Script to create a beautiful bar chart of model accuracy rankings from translation results.

USAGE:
1. Update RESULTS_JSON_PATH at the top of the script with your results file path
2. Run: python create_accuracy_chart.py

EXAMPLE:
RESULTS_JSON_PATH = r"results\comprehensive_translation_results_20250908_185147.json"
"""

import json
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from termcolor import colored
import sys
import os

# IMPORTANT VARIABLES (ALL CAPS)
OUTPUT_IMAGE_PATH = "model_accuracy_chart.png"
FIGURE_SIZE = (18, 14)
DPI = 300
COLOR_PALETTE = "viridis"
TITLE_FONT_SIZE = 18
LABEL_FONT_SIZE = 14
ANNOTATION_FONT_SIZE = 12
MODEL_NAME_FONT_SIZE = 11

# JSON file path - UPDATE THIS LINE with your results file path
RESULTS_JSON_PATH = r"results\comprehensive_translation_results_20250908_210133.json"

def load_results_from_json(json_path):
    """Load model data from a comprehensive translation results JSON file."""
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        print(colored(f"✓ Successfully loaded results from {json_path}", "green"))
        print(colored(f"  📊 Total models tested: {data.get('total_models_tested', 0)}", "cyan"))
        print(colored(f"  📁 Total files tested: {data.get('total_files_tested', 0)}", "cyan"))
        print(colored(f"  📅 Test timestamp: {data.get('test_timestamp', 'Unknown')}", "cyan"))

        return data

    except FileNotFoundError:
        print(colored(f"✗ Error: Results file {json_path} not found", "red"))
        return None
    except json.JSONDecodeError:
        print(colored(f"✗ Error: Invalid JSON format in {json_path}", "red"))
        return None

def get_combined_model_data():
    """Get combined model data from the JSON results file."""
    if not RESULTS_JSON_PATH:
        print(colored("✗ Error: No results JSON file path provided", "red"))
        print(colored("Usage: python create_accuracy_chart.py path/to/results.json", "yellow"))
        return None, None

    # Load data from the JSON file
    data = load_results_from_json(RESULTS_JSON_PATH)
    if not data:
        return None, None

    # Extract model summaries
    model_summaries = data.get('model_summaries', {})

    # Convert to the format expected by extract_model_data
    models_data = {}
    for model_name, summary in model_summaries.items():
        models_data[model_name] = {
            "overall_accuracy": summary.get("overall_accuracy", 0),
            "rank": summary.get("rank", 999)
        }

    print(colored(f"✓ Extracted data for {len(models_data)} models", "green"))
    return models_data, None  # Return None for high_reasoning_data since it's combined

def extract_model_data(medium_data, high_data):
    """Extract and combine model data from datasets."""
    # Create a list to hold model data
    models_data = []

    # Process main model data
    if medium_data:
        for model_name, summary in medium_data.items():
            # Clean model name - remove provider prefix, keep only model name
            clean_model_name = model_name.split('/')[-1] if '/' in model_name else model_name

            # Add reasoning level to display name for GPT models
            if clean_model_name in ['gpt-5', 'gpt-5-mini']:
                display_name = f"{clean_model_name}-medium"
            else:
                display_name = clean_model_name

            models_data.append({
                'model': model_name,  # Keep original for identification
                'display_name': display_name,  # Clean name with reasoning level
                'accuracy': summary.get('overall_accuracy', 0),
                'rank': summary.get('rank', 999),
                'reasoning_level': 'medium'
            })

    # Process high reasoning data (if available)
    if high_data:
        for model_name, summary in high_data.items():
            # Clean model name - remove provider prefix, keep only model name
            clean_model_name = model_name.split('/')[-1] if '/' in model_name else model_name

            # Add high reasoning level
            display_name = f"{clean_model_name}-high"

            models_data.append({
                'model': model_name,  # Keep original for identification
                'display_name': display_name,  # Clean name with reasoning level
                'accuracy': summary.get('overall_accuracy', 0),
                'rank': summary.get('rank', 999),
                'reasoning_level': 'high'
            })

    if not models_data:
        print(colored("✗ Error: No model data found", "red"))
        return []

    # Sort by accuracy descending, then by reasoning level (high first), then by model name
    models_data.sort(key=lambda x: (-x['accuracy'], x.get('reasoning_level', 'medium') != 'high', x['model']))

    # Update ranks after sorting
    for i, model in enumerate(models_data, 1):
        model['rank'] = i

    print(colored(f"✓ Processed data for {len(models_data)} models", "green"))
    return models_data

def create_beautiful_bar_chart(models_data):
    """Create a beautiful bar chart using seaborn."""
    # Set the style with better font settings
    sns.set_style("whitegrid")
    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.rcParams['font.size'] = MODEL_NAME_FONT_SIZE

    plt.figure(figsize=FIGURE_SIZE, dpi=DPI)

    # Create DataFrame for easier plotting
    df = pd.DataFrame(models_data)

    # Create color palette
    colors = sns.color_palette(COLOR_PALETTE, len(df))

    # Simple color scheme: top model in red, rest in green
    top_model_color = '#FF4444'  # Red for top model
    other_models_color = '#4CAF50'  # Green for all other models

    bar_colors = []
    for i, model_row in enumerate(df['model']):
        # Check if this is the top model (rank 1)
        if df['rank'].iloc[i] == 1:
            bar_colors.append(top_model_color)
        else:
            bar_colors.append(other_models_color)

    # Create the bar plot
    ax = sns.barplot(data=df, x='accuracy', y='display_name', palette=bar_colors, orient='h',
                    edgecolor='black', linewidth=0.5)

    # Customize the plot with bigger, more readable text
    plt.title('LLM Translation Accuracy Rankings', fontsize=TITLE_FONT_SIZE, fontweight='bold', pad=30)
    plt.xlabel('Accuracy Score (%)', fontsize=LABEL_FONT_SIZE, fontweight='bold', labelpad=15)
    plt.ylabel('AI Models', fontsize=LABEL_FONT_SIZE, fontweight='bold', labelpad=15)

    # Add value labels on bars with bigger text
    for i, (accuracy, model, display_name) in enumerate(zip(df['accuracy'], df['model'], df['display_name'])):
        # Format accuracy as percentage with bigger text
        accuracy_text = f"{accuracy:.1f}%"

        # Position the text - more spacing for readability
        x_pos = accuracy + 0.15

        # Special styling for top model (rank 1) with bigger, more prominent text
        if df['rank'].iloc[i] == 1:
            plt.text(x_pos, i, accuracy_text, ha='left', va='center',
                    fontsize=ANNOTATION_FONT_SIZE + 2, fontweight='bold', color='white',
                    bbox=dict(boxstyle="round,pad=0.3", facecolor=top_model_color, edgecolor='none', alpha=0.9))
        else:
            plt.text(x_pos, i, accuracy_text, ha='left', va='center',
                    fontsize=ANNOTATION_FONT_SIZE, fontweight='bold', color='black',
                    bbox=dict(boxstyle="round,pad=0.2", facecolor='white', edgecolor='gray', alpha=0.8))

    # Add rank numbers with bigger text - moved further left to avoid covering model names
    for i, rank in enumerate(df['rank']):
        rank_text = f"#{rank}"
        plt.text(-1.5, i, rank_text, ha='right', va='center',
                fontsize=ANNOTATION_FONT_SIZE, fontweight='bold', color='white',
                bbox=dict(boxstyle="round,pad=0.3", facecolor='black', edgecolor='none', alpha=0.7))

    # Set x-axis limits to accommodate all the labels - increased left margin for rank numbers
    plt.xlim(-3.0, max(df['accuracy']) + 6)

    # Remove top and right spines for cleaner look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add subtle gridlines
    ax.grid(axis='x', alpha=0.2, linestyle='--')
    ax.grid(axis='y', alpha=0)

    # Make tick labels bigger
    ax.tick_params(axis='both', which='major', labelsize=MODEL_NAME_FONT_SIZE)

    # Add source information
    json_filename = os.path.basename(RESULTS_JSON_PATH) if RESULTS_JSON_PATH else "Unknown"
    plt.figtext(0.5, 0.02, f"Data source: {json_filename}",
               ha='center', fontsize=11, style='italic', color='gray')

    # Tight layout with more padding for better spacing
    plt.tight_layout(rect=[0, 0.08, 1, 0.92])

    # Save the chart
    plt.savefig(OUTPUT_IMAGE_PATH, bbox_inches='tight', dpi=DPI, facecolor='white')
    print(colored(f"✓ Beautiful, legible chart saved as {OUTPUT_IMAGE_PATH}", "green"))

    # Close the figure to free memory
    plt.close()

def print_summary(models_data):
    """Print a summary of the results."""
    print(colored("\nTRANSLATION ACCURACY SUMMARY", "cyan", attrs=['bold']))
    print(colored("=" * 50, "cyan"))

    for model in models_data:
        print(colored(f"#{model['rank']}: {model['display_name']}", "yellow", attrs=['bold']) +
              colored(f" - {model['accuracy']:.1f}% accuracy", "white"))

    print(colored(f"\nBeautiful chart saved to: {OUTPUT_IMAGE_PATH}", "green"))
    print(colored(f"Total AI models analyzed: {len(models_data)}", "blue"))

def main():
    """Main function to orchestrate the chart creation."""
    print(colored("🚀 LLM Translation Accuracy Chart Generator", "blue", attrs=['bold']))
    print(colored("=" * 60, "blue"))

    # Check if results file exists
    if not os.path.exists(RESULTS_JSON_PATH):
        print(colored(f"✗ Error: Results file '{RESULTS_JSON_PATH}' does not exist", "red"))
        print(colored("Please update RESULTS_JSON_PATH at the top of the script", "yellow"))
        return

    print(colored(f"📄 Using results file: {RESULTS_JSON_PATH}", "green"))

    # Get combined data from the JSON file
    medium_data, high_data = get_combined_model_data()

    if medium_data is None:
        print(colored("✗ Failed to load data from JSON file", "red"))
        return

    # Extract and combine model data
    models_data = extract_model_data(medium_data, high_data)

    if not models_data:
        print(colored("✗ No model data to plot", "red"))
        return

    # Create the beautiful chart
    create_beautiful_bar_chart(models_data)

    # Print summary
    print_summary(models_data)

    print(colored("✅ Chart creation completed successfully!", "green", attrs=['bold']))

if __name__ == "__main__":
    main()

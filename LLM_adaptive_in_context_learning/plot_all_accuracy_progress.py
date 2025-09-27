import os
import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import re
from termcolor import colored

def extract_model_name_from_path(path):
    """Extract model name from the folder path"""
    # Look for model patterns in the path
    path_parts = path.split(os.sep)

    # Common model patterns
    model_patterns = [
        r'gpt-5', r'gpt-4', r'gpt-3', r'claude', r'glm-4\.5', r'grok',
        r'sonoma', r'openai', r'x-ai', r'z-ai', r'meta', r'anthropic'
    ]

    for part in path_parts:
        for pattern in model_patterns:
            if re.search(pattern, part, re.IGNORECASE):
                return part

    # If no specific model found, use the last meaningful folder name
    for part in reversed(path_parts):
        if part and not part.startswith('adaptive_sampling_results') and len(part) > 3:
            return part

    return "Unknown Model"

def load_accuracy_data():
    """Load accuracy data from all accuracy_metrics.json files"""
    accuracy_data = defaultdict(list)
    model_colors = {}
    color_cycle = plt.cm.tab20.colors  # Use tab20 colormap for distinct colors

    # Walk through all directories
    for root, dirs, files in os.walk('.'):
        if 'accuracy_metrics.json' in files:
            json_path = os.path.join(root, 'accuracy_metrics.json')

            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                if 'iterations' not in data:
                    continue

                # Extract model name from path
                model_name = extract_model_name_from_path(root)

                # Assign color if not already assigned
                if model_name not in model_colors:
                    color_idx = len(model_colors) % len(color_cycle)
                    model_colors[model_name] = color_cycle[color_idx]

                # Extract accuracy progression
                iterations = []
                accuracies = []

                for item in data['iterations']:
                    if 'iteration' in item and 'accuracy' in item:
                        iterations.append(item['iteration'])
                        accuracies.append(item['accuracy'])

                if iterations and accuracies:
                    accuracy_data[model_name].append({
                        'iterations': iterations,
                        'accuracies': accuracies,
                        'max_accuracy': max(accuracies),
                        'final_accuracy': accuracies[-1] if accuracies else 0
                    })

                print(colored(f"✓ Loaded {model_name}: {len(accuracies)} iterations", "green"))

            except Exception as e:
                print(colored(f"⚠️ Error loading {json_path}: {e}", "yellow"))
                continue

    return accuracy_data, model_colors

def plot_accuracy_progress(accuracy_data, model_colors):
    """Plot accuracy progression for all models"""
    plt.figure(figsize=(16, 10))

    all_iterations = []
    all_accuracies = []
    model_smoothed_data = {}

    # Plot individual model runs
    for model_name, runs in accuracy_data.items():
        color = model_colors[model_name]

        for i, run in enumerate(runs):
            iterations = run['iterations']
            accuracies = run['accuracies']

            # Plot individual run
            label = f"{model_name}" if i == 0 else ""
            plt.plot(iterations, accuracies, color=color, alpha=0.3, linewidth=1,
                    label=label if i == 0 else "")

            # Collect data for average calculation
            all_iterations.extend(iterations)
            all_accuracies.extend(accuracies)

        # Add model statistics
        if runs:
            max_acc = max(run['max_accuracy'] for run in runs)
            final_acc = np.mean([run['final_accuracy'] for run in runs])
            print(colored(f"📊 {model_name}: {len(runs)} runs, Max: {max_acc:.1%}, Avg Final: {final_acc:.1%}", "cyan"))

            # Add smoothed trend statistics if available
            if model_name in model_smoothed_data:
                smoothed_data = model_smoothed_data[model_name]
                if len(smoothed_data['smoothed']) > 1:
                    trend = smoothed_data['smoothed'][-1] - smoothed_data['smoothed'][0]
                    trend_pct = (trend / smoothed_data['smoothed'][0]) * 100 if smoothed_data['smoothed'][0] > 0 else 0
                    trend_direction = "↗️" if trend > 0 else "↘️" if trend < 0 else "➡️"
                    print(colored(f"   {trend_direction} Smoothed trend: {trend_pct:+.1f}% ({smoothed_data['smoothed'][0]:.1%} → {smoothed_data['smoothed'][-1]:.1%})", "yellow"))

    # Calculate and plot smoothed averages for each model
    for model_name, runs in accuracy_data.items():
        if not runs:
            continue

        color = model_colors[model_name]

        # Collect all iterations and accuracies for this model
        model_iterations = []
        model_accuracies = []

        for run in runs:
            model_iterations.extend(run['iterations'])
            model_accuracies.extend(run['accuracies'])

        # Group by iteration for averaging
        iter_groups = defaultdict(list)
        for iter_num, acc in zip(model_iterations, model_accuracies):
            iter_groups[iter_num].append(acc)

        if iter_groups:
            avg_iterations = sorted(iter_groups.keys())
            avg_accuracies = [np.mean(iter_groups[iter_num]) for iter_num in avg_iterations]

            # Apply smoothing to the model's average curve
            if len(avg_accuracies) >= 3:
                window_size = min(8, len(avg_accuracies))  # Increased window size for smoother curves
                smoothed_accuracies = []

                for i in range(len(avg_accuracies)):
                    start_idx = max(0, i - window_size // 2)
                    end_idx = min(len(avg_accuracies), i + window_size // 2 + 1)
                    smoothed_accuracies.append(np.mean(avg_accuracies[start_idx:end_idx]))

                # Plot model's smoothed average line (thick and prominent)
                plt.plot(avg_iterations, smoothed_accuracies, color=color, linewidth=5, alpha=0.95,
                        linestyle='-', label=f'{model_name} (Smoothed)', zorder=12)

                # Add a subtle fill under the smoothed curve for emphasis
                plt.fill_between(avg_iterations, smoothed_accuracies, alpha=0.1, color=color, zorder=8)

                # Store for later use
                model_smoothed_data[model_name] = {
                    'iterations': avg_iterations,
                    'smoothed': smoothed_accuracies
                }

    # Calculate and plot overall average (thinner, for reference)
    if all_iterations and all_accuracies:
        iter_groups = defaultdict(list)
        for iter_num, acc in zip(all_iterations, all_accuracies):
            iter_groups[iter_num].append(acc)

        avg_iterations = sorted(iter_groups.keys())
        avg_accuracies = [np.mean(iter_groups[iter_num]) for iter_num in avg_iterations]

        if len(avg_accuracies) >= 3:
            window_size = min(8, len(avg_accuracies))  # Increased window size for smoother curves
            smoothed_accuracies = []

            for i in range(len(avg_accuracies)):
                start_idx = max(0, i - window_size // 2)
                end_idx = min(len(avg_accuracies), i + window_size // 2 + 1)
                smoothed_accuracies.append(np.mean(avg_accuracies[start_idx:end_idx]))

            # Plot overall average as dashed line (less prominent)
            plt.plot(avg_iterations, smoothed_accuracies, 'k--', linewidth=3, alpha=0.7,
                    label='Overall Average (Smoothed)', zorder=11)

    # Formatting
    plt.title('Accuracy Progression Across All Models and Runs', fontsize=16, fontweight='bold')
    plt.xlabel('Iteration', fontsize=12)
    plt.ylabel('Accuracy', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='lower right', fontsize=10)

    # Set y-axis limits
    plt.ylim(0, 1.0)
    plt.yticks([i/10 for i in range(11)], [f'{i*10}%' for i in range(11)])

    # Add summary statistics
    total_runs = sum(len(runs) for runs in accuracy_data.values())
    total_models = len(accuracy_data)

    plt.text(0.02, 0.98, f'Total Models: {total_models}',
            transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

    plt.text(0.02, 0.90, f'Total Runs: {total_runs}',
            transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

    plt.tight_layout()

    # Save the plot
    output_file = 'all_models_accuracy_comparison.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(colored(f"📈 Plot saved as: {output_file}", "green"))

    return output_file

def main():
    """Main function to load data and create plots"""
    print(colored("🚀 Loading Accuracy Data from All Models", "cyan"))
    print(colored("=" * 50, "cyan"))

    # Load all accuracy data
    accuracy_data, model_colors = load_accuracy_data()

    if not accuracy_data:
        print(colored("❌ No accuracy data found!", "red"))
        return

    print(colored(f"\n📊 Found {len(accuracy_data)} models with accuracy data", "magenta"))

    # Create the comprehensive plot
    plot_file = plot_accuracy_progress(accuracy_data, model_colors)

    print(colored("\n✅ Analysis Complete!", "green"))
    print(colored(f"   📁 Plot saved: {plot_file}", "cyan"))

if __name__ == "__main__":
    main()

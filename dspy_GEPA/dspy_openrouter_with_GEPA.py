import dspy
from dspy import GEPA
import os
import json
from datasets import load_dataset
from termcolor import cprint

MODEL = "google/gemma-3-12b-it"
REFLECTION_MODEL = "x-ai/grok-4-fast:free"

lm = dspy.LM(
    # you have to put openai/ in front of the model name when using openrouter
    f"openai/{MODEL}", 
    api_key=os.getenv("OPENROUTER_API_KEY"), 
    api_base="https://openrouter.ai/api/v1",
    max_tokens=100_000
)
dspy.configure(lm=lm)


def init_dataset():
    train_split = load_dataset("AI-MO/aimo-validation-aime")['train']
    train_split = [
        dspy.Example({
            "problem": x['problem'],
            'solution': x['solution'],
            'answer': x['answer'],
        }).with_inputs("problem")
        for x in train_split
    ]
    import random
    random.Random(0).shuffle(train_split)
    tot_num = len(train_split)

    test_split = load_dataset("MathArena/aime_2025")['train']
    test_split = [
        dspy.Example({
            "problem": x['problem'],
            'answer': x['answer'],
        }).with_inputs("problem")
        for x in test_split
    ]

    train_set = train_split[:int(0.5 * tot_num)]
    val_set = train_split[int(0.5 * tot_num):]
    test_set = test_split * 5

    return train_set, val_set, test_set

train_set, val_set, test_set = init_dataset()

print(len(train_set), len(val_set), len(test_set))

# Save train_set to JSON
train_set_dicts = [example.toDict() for example in train_set]
with open('train_set.json', 'w', encoding='utf-8') as f:
    json.dump(train_set_dicts, f, indent=2, ensure_ascii=False)

# print("Problem:")
# print(train_set[0]['problem'])
# print("\n\nSolution:")
# print(train_set[0]['solution'])
# print("\n\nAnswer:")
# print(train_set[0]['answer'])

class GenerateResponse(dspy.Signature):
    """Solve the problem and provide the answer in the correct format."""
    problem = dspy.InputField()
    answer = dspy.OutputField()

program = dspy.ChainOfThought(GenerateResponse)
# print(program(problem=train_set[0]['problem']))

def metric_with_feedback(example, prediction, trace=None, pred_name=None, pred_trace=None):
    correct_answer = int(example['answer'])
    written_solution = example.get('solution', '')
    try:
        llm_answer = int(prediction.answer)
    except ValueError as e:
        feedback_text = f"The final answer must be a valid integer and nothing else. You responded with '{prediction.answer}', which couldn't be parsed as a python integer. Please ensure your answer is a valid integer without any additional text or formatting."
        feedback_text += f" The correct answer is '{correct_answer}'."
        if written_solution:
            feedback_text += f" Here's the full step-by-step solution:\n{written_solution}\n\nThink about what takeaways you can learn from this solution to improve your future answers and approach to similar problems and ensure your final answer is a valid integer."
        return dspy.Prediction(score=0, feedback=feedback_text)

    score = int(correct_answer == llm_answer)

    feedback_text = ""
    if score == 1:
        feedback_text = f"Your answer is correct. The correct answer is '{correct_answer}'."
    else:
        feedback_text = f"Your answer is incorrect. The correct answer is '{correct_answer}'."
    
    if written_solution:
        feedback_text += f" Here's the full step-by-step solution:\n{written_solution}\n\nThink about what takeaways you can learn from this solution to improve your future answers and approach to similar problems."

    return dspy.Prediction(score=score, feedback=feedback_text)

train_set = train_set[:30]
val_set = val_set[:30]

optimizer = GEPA(
    metric=metric_with_feedback,
    auto="light",
    num_threads=50,
    track_stats=True,
    reflection_minibatch_size=3,
    # define the reflection LM. make sure to put openai/ in front of the model name when using openrouter
    reflection_lm=dspy.LM(model=f"openai/{REFLECTION_MODEL}", 
    temperature=1.0,
    max_tokens=32000,
    api_key=os.getenv("OPENROUTER_API_KEY"),
    api_base="https://openrouter.ai/api/v1"
    )
)

optimized_program = optimizer.compile(
    program,
    trainset=train_set,
    valset=val_set,
)
print("Optimized program:")
cprint(optimized_program, 'green')
print(optimized_program.predict.signature.instructions)

# Save the optimized prompt to file
with open('optimized_prompt.txt', 'w', encoding='utf-8') as f:
    f.write("OPTIMIZED PROMPT FROM GEPA\n")
    f.write("=" * 50 + "\n\n")
    f.write(optimized_program.predict.signature.instructions)
    f.write("\n\n" + "=" * 50 + "\n")

print("Optimized prompt saved to 'optimized_prompt.txt'")

# Save optimization statistics and create progress plot
if hasattr(optimized_program, 'detailed_results') and optimized_program.detailed_results:
    stats = optimized_program.detailed_results

    # Save detailed optimization statistics
    with open('optimization_stats.txt', 'w', encoding='utf-8') as f:
        f.write("GEPA OPTIMIZATION STATISTICS\n")
        f.write("=" * 50 + "\n\n")

        f.write(f"Total candidates tried: {len(stats.candidates)}\n")
        f.write(f"Total metric calls: {stats.total_metric_calls}\n")
        f.write(f"Number of full validation evaluations: {stats.num_full_val_evals}\n")
        f.write(f"Best candidate index: {stats.best_idx}\n")
        f.write(f"Best validation score: {max(stats.val_aggregate_scores)}\n\n")

        f.write("CANDIDATE SCORES OVER TIME:\n")
        f.write("-" * 30 + "\n")
        for i, score in enumerate(stats.val_aggregate_scores):
            f.write(f"Candidate {i}: {score:.3f}\n")

        f.write("\nDISCOVERY EVALUATION COUNTS:\n")
        f.write("-" * 30 + "\n")
        for i, count in enumerate(stats.discovery_eval_counts):
            f.write(f"Candidate {i}: Found after {count} evaluations\n")

        f.write("\nHIGHEST SCORE PER VALIDATION TASK:\n")
        f.write("-" * 35 + "\n")
        for i, score in enumerate(stats.highest_score_achieved_per_val_task):
            f.write(f"Task {i}: {score:.3f}\n")

    print("Optimization statistics saved to 'optimization_stats.txt'")

    # Create and save optimization progress plot
    try:
        import matplotlib.pyplot as plt

        plt.figure(figsize=(12, 8))

        # Plot 1: Candidate scores over time
        plt.subplot(2, 2, 1)
        plt.plot(stats.val_aggregate_scores, 'b-o', linewidth=2, markersize=4)
        plt.title('GEPA Optimization Progress', fontsize=12, fontweight='bold')
        plt.xlabel('Candidate Number', fontsize=10)
        plt.ylabel('Validation Score', fontsize=10)
        plt.grid(True, alpha=0.3)

        # Plot 2: Cumulative best scores
        plt.subplot(2, 2, 2)
        cumulative_best = [max(stats.val_aggregate_scores[:i+1]) for i in range(len(stats.val_aggregate_scores))]
        plt.plot(cumulative_best, 'r--', linewidth=2, marker='s', markersize=4)
        plt.title('Best Score Found So Far', fontsize=12, fontweight='bold')
        plt.xlabel('Candidate Number', fontsize=10)
        plt.ylabel('Best Score', fontsize=10)
        plt.grid(True, alpha=0.3)

        # Plot 3: Discovery evaluation counts
        plt.subplot(2, 2, 3)
        plt.bar(range(len(stats.discovery_eval_counts)), stats.discovery_eval_counts,
                color='green', alpha=0.7)
        plt.title('Evaluations to Discover Each Candidate', fontsize=12, fontweight='bold')
        plt.xlabel('Candidate Number', fontsize=10)
        plt.ylabel('Evaluations Required', fontsize=10)
        plt.grid(True, alpha=0.3)

        # Plot 4: Per-task best scores
        plt.subplot(2, 2, 4)
        plt.bar(range(len(stats.highest_score_achieved_per_val_task)),
                stats.highest_score_achieved_per_val_task, color='purple', alpha=0.7)
        plt.title('Best Score Per Validation Task', fontsize=12, fontweight='bold')
        plt.xlabel('Validation Task', fontsize=10)
        plt.ylabel('Best Score', fontsize=10)
        plt.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('gepa_optimization_progress.png', dpi=300, bbox_inches='tight')
        print("Optimization progress plot saved to 'gepa_optimization_progress.png'")

        # Also create a simple line plot for just the main progress
        plt.figure(figsize=(10, 6))
        plt.plot(stats.val_aggregate_scores, 'b-', linewidth=3, marker='o', markersize=6,
                label='Candidate Scores')
        plt.plot(cumulative_best, 'r--', linewidth=2, marker='s', markersize=4,
                label='Best So Far')
        plt.title('GEPA Optimization Trajectory', fontsize=14, fontweight='bold')
        plt.xlabel('Optimization Step (Candidate)', fontsize=12)
        plt.ylabel('Validation Score', fontsize=12)
        plt.legend(fontsize=10)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('gepa_trajectory_simple.png', dpi=300, bbox_inches='tight')
        print("Simple trajectory plot saved to 'gepa_trajectory_simple.png'")

    except ImportError:
        print("Matplotlib not available for plotting. Install with: pip install matplotlib")
else:
    print("No detailed results available (track_stats may be False)")
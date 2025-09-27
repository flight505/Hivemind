import asyncio
import json
import os
import matplotlib.pyplot as plt
import numpy as np
from termcolor import colored
from API_client import make_API_call

# Configuration - all caps as per user rules
PROVIDER = "openrouter"
MAX_ITERATIONS = 20
MAX_AVERAGE_SCORE = 9
RESULTS_FOLDER = "results"
LENGTH_TOLERANCE_PERCENT = 10  # Maximum allowed length deviation in percent
MAX_REWRITE_RETRIES = 3  # Maximum retries if length exceeds tolerance
MAX_HISTORY_LENGTH = 3  # Maximum number of message pairs to keep in rewrite history
TOP_SCORING_EXAMPLES = 3  # Number of top-scoring previous versions to show as examples
MODEL = "openrouter/sonoma-sky-alpha"

TEXT = """
LLM learns in context to solve hard problems 🚀
It achieves 15x speed-up & 20% accuracy improvement ‼️

using Parallelized tree search & cyclic self-reflection
code in comment

It uses a Parallelized Tree Search algorithm where each "node" represents a different predictor function,

and the system intelligently explores the space of possible functions while using cyclic memory
and self-reflection  to find the most accurate one.

the system creates Python functions that can predict categorical outputs (1, 2, 3, 4) based on 5 numerical inputs (A, B, C, D, E).

"""

def create_progress_plot(iteration_data_list, current_iteration):
    """Create a beautiful progress plot showing iterative improvement."""
    if not iteration_data_list:
        return

    # Set up the plot with a dark theme
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), facecolor='#1a1a1a')

    # Extract data
    iterations = [data['iteration'] for data in iteration_data_list]
    avg_scores = [data['average_score'] for data in iteration_data_list]

    # Color scheme
    primary_color = '#00ff88'  # Bright green
    secondary_color = '#0088ff'  # Bright blue
    accent_color = '#ff4444'   # Bright red
    bg_color = '#2a2a2a'

    # Top subplot: Average score progression
    ax1.set_facecolor(bg_color)
    ax1.plot(iterations, avg_scores, 'o-', color=primary_color, linewidth=3, markersize=8,
             markerfacecolor=primary_color, markeredgecolor='white', markeredgewidth=2)

    # Add target line
    ax1.axhline(y=MAX_AVERAGE_SCORE, color=accent_color, linestyle='--', alpha=0.7,
                linewidth=2, label=f'Target: {MAX_AVERAGE_SCORE}/10')

    # Fill area under the curve
    ax1.fill_between(iterations, avg_scores, alpha=0.1, color=primary_color)

    ax1.set_title('🎨 Creative Text Evolution', fontsize=16, color='white', pad=20)
    ax1.set_xlabel('Iteration', fontsize=12, color='white')
    ax1.set_ylabel('Average Score (/10)', fontsize=12, color='white')
    ax1.set_xlim(0.5, max(iterations) + 0.5)
    ax1.set_ylim(0, 10)
    ax1.grid(True, alpha=0.2, color='white')
    ax1.legend(facecolor=bg_color, edgecolor='white', fontsize=10)

    # Make ticks white
    ax1.tick_params(colors='white', which='both')

    # Bottom subplot: Latest iteration persona breakdown
    latest_data = iteration_data_list[-1]
    ax2.set_facecolor(bg_color)

    persona_names = []
    persona_scores = []

    for grade in latest_data['individual_grades']:
        # Create short persona labels
        expertise_short = grade['expertise'][:20] + '...' if len(grade['expertise']) > 20 else grade['expertise']
        persona_names.append(f"P{grade['person']}")
        persona_scores.append(grade['total_score'])

    bars = ax2.bar(persona_names, persona_scores, color=secondary_color, alpha=0.8, edgecolor='white', linewidth=1)

    # Add value labels on bars
    for bar, score in zip(bars, persona_scores):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{score:.1f}', ha='center', va='bottom', color='white', fontweight='bold')

    ax2.set_title(f'Persona Scores - Iteration {current_iteration}', fontsize=14, color='white', pad=20)
    ax2.set_xlabel('Persona', fontsize=12, color='white')
    ax2.set_ylabel('Score (/10)', fontsize=12, color='white')
    ax2.set_ylim(0, 10)
    ax2.grid(True, alpha=0.2, color='white', axis='y')

    # Make ticks white
    ax2.tick_params(colors='white', which='both')

    # Add current average line
    current_avg = latest_data['average_score']
    ax2.axhline(y=current_avg, color=primary_color, linestyle='-', alpha=0.8,
                linewidth=2, label=f'Average: {current_avg:.1f}')
    ax2.legend(facecolor=bg_color, edgecolor='white', fontsize=10)

    # Add iteration info text
    fig.text(0.02, 0.02, f'Iteration {current_iteration}/{MAX_ITERATIONS} | Target: {MAX_AVERAGE_SCORE}/10',
             fontsize=10, color='white', alpha=0.7)

    plt.tight_layout()
    plt.savefig(f"{RESULTS_FOLDER}/progress_plot.png", dpi=150, bbox_inches='tight',
                facecolor='#1a1a1a', edgecolor='none')
    plt.close()

async def generate_personas():
    """Generate personas if they don't exist."""
    messages = [
        {
            "role": "user",
            "content": f"Given this text:\n\n{TEXT}\n\nPlease suggest 5 fictional persona descriptions designed to create evaluating tensions against one another. Each persona should represent a fundamentally different approach to creative evaluation that will naturally conflict with the others. For example: a rigid formalist vs. a chaotic experimentalist, a technical perfectionist vs. an emotional intuitive, a traditional critic vs. a postmodern deconstructionist, etc. For each persona, provide their expertise area and why they would be suitable for grading this creative work, emphasizing how their approach creates tension with other possible evaluators. Do not include any names. Format the response as a JSON array of objects."
        }
    ]

    response = await make_API_call(MODEL, messages, PROVIDER)

    if response and response.choices:
        content = response.choices[0].message.content

        # Try to parse as JSON
        try:
            personas = json.loads(content)
            with open("personas.json", "w", encoding='utf-8') as f:
                json.dump(personas, f, indent=2)
            print(colored("Personas generated and saved to personas.json", "green"))
            return personas
        except json.JSONDecodeError:
            # If not valid JSON, save the raw response
            with open("personas.json", "w", encoding='utf-8') as f:
                json.dump({"raw_response": content}, f, indent=2)
            print(colored("Raw response saved to personas.json (could not parse as JSON)", "yellow"))
            return content

async def evaluate_and_suggest(current_text, iteration):
    """Get grades and improvement suggestions from all personas."""
    print(colored(f"\n--- Iteration {iteration} Evaluation ---", "cyan"))

    try:
        with open("personas.json", "r", encoding='utf-8') as f:
            personas = json.load(f)
    except FileNotFoundError:
        print(colored("personas.json not found. Generating personas first...", "yellow"))
        personas = await generate_personas()
        if not personas:
            print(colored("Failed to generate personas.", "red"))
            return None, []

    # Create evaluation tasks for all personas
    tasks = [evaluate_with_persona(persona, i, current_text) for i, persona in enumerate(personas)]
    results = await asyncio.gather(*tasks)

    # Process results
    valid_results = []
    all_suggestions = []

    for result in results:
        if "error" in result:
            print(colored(f"Error for persona {result.get('person', 'unknown')}: {result['error']}", "red"))
            continue

        valid_results.append(result)
        if "suggestions" in result:
            # Include persona info with each suggestion
            persona_info = {
                "persona": f"P{result['person']} ({result['expertise']})",
                "score": result['total_score'],
                "suggestions": result["suggestions"]
            }
            all_suggestions.append(persona_info)

    # Calculate average score
    if valid_results:
        total_scores = [result['total_score'] for result in valid_results]
        average_score = sum(total_scores) / len(total_scores)

        print(colored(f"Average Score: {average_score:.2f}/10", "magenta"))

        return {
            "iteration": iteration,
            "average_score": round(average_score, 2),
            "individual_grades": valid_results,
            "combined_suggestions": all_suggestions
        }, average_score

    return None, 0.0

async def evaluate_with_persona(persona, persona_index, text):
    """Get evaluation and suggestions from a single persona."""
    prompt = f"""You are a {persona['expertise']}.

Evaluate this text and provide both grades and improvement suggestions:

{text}

Choose 3 rubrics that align with your expertise and grade this text on a scale of 1-10 for each rubric (10 being excellent).

Also provide 2-3 specific, actionable suggestions for improving this text from your perspective.

Return your evaluation as a JSON object with:
- "person": "{persona_index + 1}"
- "expertise": "{persona['expertise']}"
- "rubrics": array of 3 objects, each with "name" and "score" fields
- "total_score": average of the 3 rubric scores
- "suggestions": array of 2-3 specific improvement suggestions

Example format:
{{
  "person": "1",
  "expertise": "Example Expertise",
  "rubrics": [
    {{"name": "Creativity", "score": 8}},
    {{"name": "Technical Skill", "score": 7}},
    {{"name": "Emotional Impact", "score": 9}}
  ],
  "total_score": 8.0,
  "suggestions": [
    "Make the metaphors more vivid",
    "Strengthen the rhythmic structure",
    "Add more sensory details"
  ]
}}"""

    messages = [{"role": "user", "content": prompt}]
    response = await make_API_call(MODEL, messages, PROVIDER)

    if response and response.choices:
        content = response.choices[0].message.content
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {"error": f"Failed to parse response for persona {persona_index + 1}", "raw": content}
    else:
        return {"error": f"No response for persona {persona_index + 1}"}

async def rewrite_text(current_text, combined_suggestions, iteration, rewrite_history=None, iteration_data_list=None):
    """Rewrite the text using combined suggestions from all personas with length control."""
    print(colored(f"\n--- Rewriting Text (Iteration {iteration}) ---", "yellow"))

    if rewrite_history is None:
        rewrite_history = []

    original_word_count = len(current_text.split())
    max_word_count = original_word_count * (1 + LENGTH_TOLERANCE_PERCENT / 100)

    # Format suggestions with persona information
    formatted_suggestions = []
    for persona_feedback in combined_suggestions[:5]:  # Limit to top 5 personas
        persona_name = persona_feedback["persona"]
        persona_score = persona_feedback["score"]
        suggestions = persona_feedback["suggestions"]

        formatted_suggestions.append(f"**{persona_name}** (Score: {persona_score}/10):")
        for suggestion in suggestions:
            formatted_suggestions.append(f"  • {suggestion}")

    suggestions_text = "\n".join(formatted_suggestions)

    # Get top scoring examples from previous iterations
    examples_text = ""
    if iteration_data_list and len(iteration_data_list) > 1:  # Need at least 1 previous iteration
        # Sort by average score (excluding current iteration)
        previous_iterations = [data for data in iteration_data_list[:-1] if data['average_score'] > 0]
        top_examples = sorted(previous_iterations, key=lambda x: x['average_score'], reverse=True)[:TOP_SCORING_EXAMPLES]

        if top_examples:
            examples_text = "\n\nHere are examples of high-scoring previous versions for reference:\n\n"
            for i, example in enumerate(top_examples, 1):
                examples_text += f"**Example {i}** (Score: {example['average_score']:.2f}/10):\n{example['text']}\n\n"

    # Calculate length bounds for this iteration
    min_words = max(1, int(original_word_count * (1 - LENGTH_TOLERANCE_PERCENT / 100)))
    max_words = int(original_word_count * (1 + LENGTH_TOLERANCE_PERCENT / 100))

    for retry_attempt in range(MAX_REWRITE_RETRIES + 1):
        # Create stronger length constraint for retries
        if retry_attempt == 0:
            length_instruction = f"IMPORTANT: Keep the length roughly the same as the original text (approximately {original_word_count} words)."
        else:
            length_instruction = f"CRITICAL LENGTH REQUIREMENT: The previous version was too long. You MUST keep the word count under {max_words} words (original was {original_word_count} words). Be concise and focused."

        prompt = f"""TASK: Rewrite the following text to improve it based on evaluator feedback.

OUTPUT REQUIREMENT: Your rewritten text MUST be between {min_words} and {max_words} words. Count your words and ensure compliance.

ORIGINAL TEXT:
{current_text}

EVALUATOR FEEDBACK:
{suggestions_text}{examples_text}

INSTRUCTIONS:
1. PRESERVE EXACT ORIGINAL MEANING: Do NOT add, remove, or modify any facts, claims, or concepts. NO made-up details, examples, or fictional embellishments.
2. REWRITE CREATIVELY: Express the same content in your own improved style - enhance clarity, flow, and impact while staying 100% faithful to the original meaning
3. Incorporate the most valuable suggestions from evaluators while maintaining complete content integrity
4. Consider different evaluator perspectives (technical, creative, emotional, structural) to improve delivery without changing substance
5. Maintain core message, key facts, and intended audience completely intact but express them more effectively
6. Ensure output is exactly {min_words}-{max_words} words

{length_instruction}

Return only the rewritten text, nothing else."""

        # Create messages with system prompt for context
        system_message = {
            "role": "system",
            "content": f"""You are an expert creative writer specializing in iterative text improvement.

ABSOLUTE REQUIREMENTS:
• LENGTH CONTROL: Output MUST be between {min_words} and {max_words} words exactly. Count your words carefully. If your response exceeds this limit, you have failed the task.
• CONTENT INTEGRITY: PRESERVE THE EXACT ORIGINAL MEANING. Do NOT add, remove, or modify facts, claims, or concepts that aren't in the source text. NO made-up details, examples, or fictional embellishments.
• CREATIVE REWRITING: Express the same content in your own improved style - enhance clarity, flow, and impact while staying 100% faithful to the original meaning and intent.

KEY RESPONSIBILITIES:
• EVALUATOR PERSPECTIVES: Consider feedback from different expert evaluators with varying specialties.
• ITERATIVE IMPROVEMENT: Build upon previous iterations while respecting length limits and content integrity.
• QUALITY STANDARDS: Ensure the final text is polished, coherent, and effective within the word limit WITHOUT changing the original meaning."""
        }

        # Limit history to prevent token overflow (keep most recent messages)
        max_history_messages = MAX_HISTORY_LENGTH * 2  # Each iteration adds 2 messages (user + assistant)
        if len(rewrite_history) > max_history_messages:
            # Keep only the most recent messages
            rewrite_history = rewrite_history[-max_history_messages:]

        current_messages = [system_message] + rewrite_history + [{"role": "user", "content": prompt}]

        response = await make_API_call(MODEL, current_messages, PROVIDER)

        if response and response.choices:
            new_text = response.choices[0].message.content.strip()
            new_word_count = len(new_text.split())

            # Check length constraint
            if new_word_count <= max_word_count:
                print(colored(f"Text rewritten successfully ({new_word_count} words)", "green"))

                # Add assistant response to history for future iterations
                rewrite_history.extend([
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": new_text}
                ])

                return new_text, rewrite_history
            else:
                print(colored(f"Text too long ({new_word_count} words > {int(max_word_count)} limit). Retry {retry_attempt + 1}/{MAX_REWRITE_RETRIES}", "yellow"))
                # Don't add failed attempts to history
                continue
        else:
            print(colored(f"Rewrite attempt {retry_attempt + 1} failed", "red"))
            continue

    # If all retries failed, return original text
    print(colored(f"All rewrite attempts failed. Keeping original text.", "red"))
    return current_text, rewrite_history

async def iterative_improvement():
    """Main iterative improvement loop."""
    # Create results folder
    os.makedirs(RESULTS_FOLDER, exist_ok=True)

    current_text = TEXT
    iteration = 1
    rewrite_history = []  # Keep conversation history for rewriter only
    iteration_data_list = []  # Track all iteration data for plotting
    best_iteration = {"score": 0, "text": TEXT, "iteration": 0}  # Track best scoring version

    print(colored("🚀 Starting Iterative Creative Improvement", "green"))
    print(colored(f"Max iterations: {MAX_ITERATIONS}", "cyan"))
    print(colored(f"Target average score: {MAX_AVERAGE_SCORE}/10", "cyan"))

    while iteration <= MAX_ITERATIONS:
        # Evaluate current text
        evaluation_result, average_score = await evaluate_and_suggest(current_text, iteration)

        if not evaluation_result:
            print(colored("Evaluation failed, stopping.", "red"))
            break

        # Save iteration results
        iteration_data = {
            "text": current_text,
            **evaluation_result
        }

        with open(f"{RESULTS_FOLDER}/iteration_{iteration}.json", "w", encoding='utf-8') as f:
            json.dump(iteration_data, f, indent=2)

        # Save text separately for easy reading with accuracy info
        accuracy_info = f"""
Iteration {iteration}
Average Score: {average_score:.2f}/10
Word Count: {len(current_text.split())}

Text Content:
{'-' * 50}

"""
        with open(f"{RESULTS_FOLDER}/text_iteration_{iteration}_score_{average_score:.1f}.txt", "w", encoding='utf-8') as f:
            f.write(accuracy_info + current_text)

        # Track data for plotting
        iteration_data_list.append(iteration_data)

        # Update best scoring version
        if average_score > best_iteration["score"]:
            best_iteration = {
                "score": average_score,
                "text": current_text,
                "iteration": iteration
            }
            print(colored(f"🏆 New best score: {average_score:.2f}/10 (iteration {iteration})", "yellow"))

        # Create/update progress plot
        create_progress_plot(iteration_data_list, iteration)

        print(colored(f"Results saved to {RESULTS_FOLDER}/iteration_{iteration}.json", "green"))
        print(colored(f"Progress plot updated: {RESULTS_FOLDER}/progress_plot.png", "cyan"))

        # Check stopping conditions
        if average_score >= MAX_AVERAGE_SCORE:
            print(colored(f"🎉 Target score {MAX_AVERAGE_SCORE}/10 reached at iteration {iteration}!", "green"))
            break

        if iteration >= MAX_ITERATIONS:
            print(colored(f"📊 Maximum iterations ({MAX_ITERATIONS}) reached.", "yellow"))
            break

        # Get combined suggestions and rewrite
        combined_suggestions = evaluation_result["combined_suggestions"]
        if not combined_suggestions:
            print(colored("No suggestions received, stopping.", "yellow"))
            break

        current_text, rewrite_history = await rewrite_text(current_text, combined_suggestions, iteration, rewrite_history, iteration_data_list)
        iteration += 1

    # Save the best scoring version
    best_info = f"""
Best Iteration Results
======================
Best Score: {best_iteration['score']:.2f}/10
Best Iteration: {best_iteration['iteration']}
Word Count: {len(best_iteration['text'].split())}

Best Text Content:
{'-' * 50}

"""
    with open(f"{RESULTS_FOLDER}/best_version_score_{best_iteration['score']:.1f}.txt", "w", encoding='utf-8') as f:
        f.write(best_info + best_iteration['text'])

    # Save final results summary
    final_summary = {
        "total_iterations": iteration - 1,
        "final_average_score": round(average_score, 2),
        "best_average_score": round(best_iteration['score'], 2),
        "best_iteration_number": best_iteration['iteration'],
        "max_iterations": MAX_ITERATIONS,
        "target_score": MAX_AVERAGE_SCORE,
        "target_achieved": average_score >= MAX_AVERAGE_SCORE,
        "improvement_achieved": best_iteration['score'] > 0  # Any improvement from original
    }

    with open(f"{RESULTS_FOLDER}/final_summary.json", "w", encoding='utf-8') as f:
        json.dump(final_summary, f, indent=2)

    print(colored(f"\n🏁 Iterative improvement complete! Results saved in '{RESULTS_FOLDER}' folder.", "green"))
    print(colored(f"Final average score: {average_score:.2f}/10", "magenta"))
    print(colored(f"Best average score: {best_iteration['score']:.2f}/10 (iteration {best_iteration['iteration']})", "yellow"))
    print(colored(f"Best version saved as: best_version_score_{best_iteration['score']:.1f}.txt", "cyan"))

if __name__ == "__main__":
    asyncio.run(iterative_improvement())

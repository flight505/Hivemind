import asyncio
import json
from termcolor import colored
from API_client import make_API_call

TEXT = """
I not went to school yesterday.
"""

TEXT= """
LLM learns in context to solve hard problems 🚀
It achieves 15x speed-up & 20% accuracy improvement ‼️

using Parallelized tree search & cyclic self-reflection
code in comment

It uses a Parallelized Tree Search algorithm where each "node" represents a different predictor function,

and the system intelligently explores the space of possible functions while using cyclic memory
and self-reflection  to find the most accurate one.

the system creates Python functions that can predict categorical outputs (1, 2, 3, 4) based on 5 numerical inputs (A, B, C, D, E).

"""

async def grade_with_persona(persona, persona_index):
    """Grade the text using a specific persona with 3 rubrics of their choice."""
    prompt = f"""You are a {persona['expertise']}.

Given this text to evaluate:

{TEXT}

Please choose 3 rubrics that align with your expertise and grade this text on a scale of 1-10 for each rubric (10 being excellent).

Return your evaluation as a JSON object with:
- "person": "{persona_index + 1}"
- "expertise": "{persona['expertise']}"
- "rubrics": array of 3 objects, each with "name" and "score" fields
- "total_score": average of the 3 rubric scores

Example format:
{{
  "person": "1",
  "expertise": "Example Expertise",
  "rubrics": [
    {{"name": "Creativity", "score": 8}},
    {{"name": "Technical Skill", "score": 7}},
    {{"name": "Emotional Impact", "score": 9}}
  ],
  "total_score": 8.0
}}"""

    messages = [{"role": "user", "content": prompt}]
    response = await make_API_call("openrouter/sonoma-sky-alpha", messages, "openrouter")

    if response and response.choices:
        content = response.choices[0].message.content
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {"error": f"Failed to parse response for persona {persona_index + 1}", "raw": content}
    else:
        return {"error": f"No response for persona {persona_index + 1}"}

async def grade_text():
    """Load personas and get grades from each in parallel."""
    print(colored("Loading personas...", "cyan"))

    try:
        with open("personas.json", "r", encoding='utf-8') as f:
            personas = json.load(f)
    except FileNotFoundError:
        print(colored("personas.json not found. Generating personas first...", "yellow"))
        personas = await get_personas()
        if not personas:
            print(colored("Failed to generate personas.", "red"))
            return

    print(colored(f"Found {len(personas)} personas. Grading in parallel...", "cyan"))

    # Create tasks for parallel execution
    tasks = [grade_with_persona(persona, i) for i, persona in enumerate(personas)]
    results = await asyncio.gather(*tasks)

    # Process results
    valid_results = []
    all_scores = []

    print(colored("\n" + "="*60, "yellow"))
    print(colored("INDIVIDUAL GRADES", "yellow"))
    print(colored("="*60, "yellow"))

    for result in results:
        if "error" in result:
            print(colored(f"Error for persona {result.get('person', 'unknown')}: {result['error']}", "red"))
            continue

        print(colored(f"\nPersona {result['person']}: {result['expertise']}", "green"))
        for rubric in result['rubrics']:
            print(f"  {rubric['name']}: {rubric['score']}/10")
        print(f"  Total Score: {result['total_score']}/10")

        valid_results.append(result)
        all_scores.extend([rubric['score'] for rubric in result['rubrics']])

    # Calculate averages
    if valid_results:
        individual_averages = [result['total_score'] for result in valid_results]
        overall_average = sum(individual_averages) / len(individual_averages)
        rubric_average = sum(all_scores) / len(all_scores)

        print(colored("\n" + "="*60, "yellow"))
        print(colored("AVERAGES", "yellow"))
        print(colored("="*60, "yellow"))
        print(colored(f"Overall Average Score: {overall_average:.2f}/10", "magenta"))
        print(colored(f"Average Rubric Score: {rubric_average:.2f}/10", "magenta"))

        # Save results
        output_data = {
            "individual_grades": valid_results,
            "averages": {
                "overall_average": round(overall_average, 2),
                "rubric_average": round(rubric_average, 2)
            }
        }

        with open("grades.json", "w", encoding='utf-8') as f:
            json.dump(output_data, f, indent=2)

        print(colored("\nResults saved to grades.json", "green"))
    else:
        print(colored("No valid grades received.", "red"))

async def get_personas():
    messages = [
        {
            "role": "user",
            "content": f"Given this text:\n\n{TEXT}\n\nPlease suggest 5 fictional persona descriptions designed to create evaluating tensions against one another. Each persona should represent a fundamentally different approach to creative evaluation that will naturally conflict with the others. For example: a rigid formalist vs. a chaotic experimentalist, a technical perfectionist vs. an emotional intuitive, a traditional critic vs. a postmodern deconstructionist, etc. For each persona, provide their expertise area and why they would be suitable for grading this creative work, emphasizing how their approach creates tension with other possible evaluators. Do not include any names. Format the response as a JSON array of objects."
        }
    ]

    response = await make_API_call("openrouter/sonoma-sky-alpha", messages, "openrouter")

    if response and response.choices:
        content = response.choices[0].message.content

        # Try to parse as JSON
        try:
            personas = json.loads(content)
            with open("personas.json", "w", encoding='utf-8') as f:
                json.dump(personas, f, indent=2)
            print(colored("Personas saved to personas.json", "green"))
            return personas
        except json.JSONDecodeError:
            # If not valid JSON, save the raw response
            with open("personas.json", "w", encoding='utf-8') as f:
                json.dump({"raw_response": content}, f, indent=2)
            print(colored("Raw response saved to personas.json (could not parse as JSON)", "yellow"))
            return content

if __name__ == "__main__":
    asyncio.run(grade_text())
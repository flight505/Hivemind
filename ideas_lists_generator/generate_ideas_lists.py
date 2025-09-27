"""
Script to generate various types of ideas using LLMs in batches
"""

import asyncio
from termcolor import colored
from API_client import make_API_call

# IMPORTANT VARIABLES
MODEL_NAME = "openrouter/sonoma-sky-alpha"
PROVIDER = "openrouter"
OUTPUT_FILE = "generated_ideas.txt"
N_IDEAS = 10000  # Total number of ideas to generate
IDEAS_PER_CALL = 100  # Number of ideas to generate per API call
USER_INPUT_TYPE = "app ideas that leverage Large Language Models (LLMs)"

async def generate_ideas():
    """Generate ideas in batches to avoid duplicates and token limits."""
    print(colored("🚀 Starting idea generation...", "green"))
    print(colored(f"📋 Target: {N_IDEAS} ideas, {IDEAS_PER_CALL} per call", "cyan"))

    accumulated_ideas = []
    call_count = 0

    # Initialize empty file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        pass  # Create empty file

    while len(accumulated_ideas) < N_IDEAS:
        call_count += 1
        remaining_ideas = N_IDEAS - len(accumulated_ideas)
        current_batch_size = min(IDEAS_PER_CALL, remaining_ideas)

        print(colored(f"\n🔄 Call {call_count}: Generating {current_batch_size} ideas...", "yellow"))
        print(colored(f"📊 Progress: {len(accumulated_ideas)}/{N_IDEAS} ideas accumulated", "blue"))

        # Build the prompt with previous ideas to avoid duplicates
        previous_ideas_text = ""
        if accumulated_ideas:
            previous_ideas_text = "\n\nPREVIOUSLY GENERATED IDEAS (DO NOT REPEAT):\n" + "\n".join(f"- {idea}" for idea in accumulated_ideas)  

        PROMPT = f"""Generate a list of {current_batch_size} creative and innovative ideas for {USER_INPUT_TYPE}.

For each idea, provide just the general concept in about 15 words (minimum 5 words).

Make sure the ideas are diverse, covering different industries, use cases, and innovation levels.

Format: One idea per line, numbered 1 to {current_batch_size}.{previous_ideas_text}"""

        # Prepare messages for API call
        MESSAGES = [
            {"role": "user", "content": PROMPT}
        ]

        print(colored(f"🤖 Calling model: {MODEL_NAME}", "blue"))

        # Make the API call
        response = await make_API_call(MODEL_NAME, MESSAGES, PROVIDER)

        if response:
            # Extract the content from response
            content = response.choices[0].message.content
            print(colored("✅ Successfully generated batch!", "green"))

            # Parse the ideas from the response
            new_ideas = parse_ideas_from_response(content)

            if new_ideas:
                # Save new ideas to file immediately
                with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                    for i, idea in enumerate(new_ideas, len(accumulated_ideas) + 1):
                        f.write(f"{i}. {idea}\n")

                # Add new ideas to accumulated list
                accumulated_ideas.extend(new_ideas)

                print(colored(f"💾 Saved {len(new_ideas)} new ideas to file", "cyan"))
                print(colored(f"📊 Total accumulated: {len(accumulated_ideas)}/{N_IDEAS}", "cyan"))
            else:
                print(colored("⚠️  No valid ideas parsed from response", "yellow"))

        else:
            print(colored(f"❌ Failed to generate ideas in call {call_count}", "red"))
            break

    # Final summary
    if accumulated_ideas:
        print(colored("\n✅ Generation complete!", "green"))
        print(colored(f"📁 All ideas saved to {OUTPUT_FILE}", "green"))
        print(colored(f"📊 Final count: {len(accumulated_ideas)} ideas", "magenta"))
        print(colored(f"📊 Total API calls: {call_count}", "blue"))

    else:
        print(colored("❌ No ideas were generated", "red"))

def parse_ideas_from_response(content):
    """Parse ideas from the API response."""
    ideas = []

    # Split by lines and clean up
    lines = content.strip().split('\n')

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Remove numbering if present (handle 1-3 digit numbers)
        import re
        # Match patterns like "1. ", "10. ", "100. ", "1) ", etc.
        number_pattern = re.match(r'^\d+\.\s+', line)
        if number_pattern:
            line = line[number_pattern.end():]  # Remove the number prefix

        # Alternative pattern for parenthetical numbering
        alt_pattern = re.match(r'^\d+\)\s+', line)
        if alt_pattern:
            line = line[alt_pattern.end():]  # Remove the number prefix

        # Skip if too short (probably not a real idea)
        if len(line.split()) < 3:
            continue

        # Clean up and add
        if line and not line.lower().startswith(('here', 'below', 'generated', 'sure', 'i\'ll')):
            ideas.append(line)

    return ideas

if __name__ == "__main__":
    asyncio.run(generate_ideas())

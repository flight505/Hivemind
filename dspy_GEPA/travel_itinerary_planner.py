import dspy
from dspy import GEPA
import os
import json
from termcolor import cprint

MODEL = "x-ai/grok-4-fast:free"
REFLECTION_MODEL = "openai/x-ai/grok-4-fast:free"

lm = dspy.LM(
    # you have to put openai/ in front of the model name when using openrouter
    f"openai/{MODEL}",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    api_base="https://openrouter.ai/api/v1",
    max_tokens=100_000
)
dspy.configure(lm=lm)


def init_dataset():
    # Custom travel data examples
    travel_examples = [
        {
            "destination": "Tokyo, Japan",
            "duration": "7 days",
            "budget": "$3000",
            "interests": "culture, food, technology",
            "travel_style": "budget backpacker",
            "itinerary": """Day 1-2: Shibuya & Harajuku - Explore Shibuya Crossing, visit Meiji Shrine, shop in Takeshita Street
Day 3-4: Asakusa & Traditional Tokyo - Senso-ji Temple, Tokyo Skytree, Akihabara electronics district
Day 5-6: Modern Tokyo - Shinjuku nightlife, Roppongi art district, Odaiba waterfront
Day 7: Day trip to Mount Fuji area or relax in Ueno Park
Daily budget: $150-200 for food/transport, stay in hostels (~$30/night)""",
            "total_cost": 2850
        },
        {
            "destination": "Paris, France",
            "duration": "5 days",
            "budget": "$2500",
            "interests": "art, history, romance",
            "travel_style": "cultural explorer",
            "itinerary": """Day 1: Eiffel Tower & Champs-Élysées - Iconic landmarks and shopping
Day 2: Louvre & Notre-Dame - World's greatest art museum and Gothic cathedral
Day 3: Montmartre & Sacré-Cœur - Bohemian district, street artists, panoramic views
Day 4: Versailles Palace day trip - Opulent royal residence and gardens
Day 5: Seine River cruise & Latin Quarter - Romantic boat ride and student district
Daily budget: $180-220 for museums/meals, mid-range hotels (~$120/night)""",
            "total_cost": 2380
        },
        {
            "destination": "Bali, Indonesia",
            "duration": "10 days",
            "budget": "$2000",
            "interests": "beach, nature, wellness",
            "travel_style": "relaxed wellness",
            "itinerary": """Day 1-3: Seminyak - Beach clubs, yoga studios, boutique shopping
Day 4-6: Ubud - Rice terraces, monkey forest, traditional dance shows, spa treatments
Day 7-8: Mount Batur sunrise trek - Volcanic hiking adventure with local guide
Day 9-10: Nusa Dua - Luxury beach resort relaxation and water sports
Daily budget: $80-120 for activities/meals, mix of hostels and mid-range hotels (~$40/night)""",
            "total_cost": 1950
        },
        {
            "destination": "New York City, USA",
            "duration": "4 days",
            "budget": "$1800",
            "interests": "urban exploration, food, entertainment",
            "travel_style": "fast-paced urban",
            "itinerary": """Day 1: Manhattan highlights - Times Square, Broadway show, Central Park walk
Day 2: Art & culture - MoMA, MET museum, High Line park
Day 3: Food tour - Multiple boroughs, diverse cuisines, food markets
Day 4: Brooklyn Bridge, Statue of Liberty, rooftop bars
Daily budget: $150-200 for shows/attractions, mid-range hotels (~$150/night)""",
            "total_cost": 1720
        },
        {
            "destination": "Machu Picchu, Peru",
            "duration": "6 days",
            "budget": "$2200",
            "interests": "history, adventure, nature",
            "travel_style": "historical adventurer",
            "itinerary": """Day 1-2: Cusco acclimatization - Colonial city, Sacred Valley, altitude adjustment
Day 3: Aguas Calientes - Hot springs, local markets, Inca trail preparation
Day 4: Machu Picchu visit - Guided tour, sunrise experience, archaeological sites
Day 5: Additional explorations - Rainbow Mountain trek or Inca sites
Day 6: Return to Cusco - More city exploration or relaxation
Daily budget: $120-160 for tours/transport, mid-range hotels (~$60/night)""",
            "total_cost": 2080
        }
    ]

    # Convert to DSPy examples
    examples = [
        dspy.Example({
            "destination": ex["destination"],
            "duration": ex["duration"],
            "budget": ex["budget"],
            "interests": ex["interests"],
            "travel_style": ex["travel_style"],
            "itinerary": ex["itinerary"],
            "total_cost": ex["total_cost"]
        }).with_inputs("destination", "duration", "budget", "interests", "travel_style")
        for ex in travel_examples
    ]

    # Split into train/val/test
    train_set = examples[:3]  # First 3 for training
    val_set = examples[3:4]   # Next 1 for validation
    test_set = examples[4:]   # Last 1 for testing

    return train_set, val_set, test_set

train_set, val_set, test_set = init_dataset()

print(len(train_set), len(val_set), len(test_set))

# Save train_set to JSON
train_set_dicts = [example.toDict() for example in train_set]
with open('travel_train_set.json', 'w', encoding='utf-8') as f:
    json.dump(train_set_dicts, f, indent=2, ensure_ascii=False)

# print("Example:")
# print(train_set[0]['destination'])
# print(train_set[0]['itinerary'])

class PlanItinerary(dspy.Signature):
    """Create a detailed day-by-day travel itinerary with budget breakdown."""
    destination = dspy.InputField()
    duration = dspy.InputField()
    budget = dspy.InputField()
    interests = dspy.InputField()
    travel_style = dspy.InputField()
    itinerary = dspy.OutputField()

program = dspy.ChainOfThought(PlanItinerary)
# print(program(destination=train_set[0]['destination'], duration=train_set[0]['duration'], budget=train_set[0]['budget'], interests=train_set[0]['interests'], travel_style=train_set[0]['travel_style']))

def metric_with_feedback(example, prediction, trace=None, pred_name=None, pred_trace=None):
    try:
        # Parse the predicted itinerary
        predicted_itinerary = prediction.itinerary.strip()

        # Check if itinerary has proper structure (contains "Day" mentions)
        has_days = "day" in predicted_itinerary.lower() or "Day" in predicted_itinerary

        # Check if it includes budget breakdown
        has_budget = "budget" in predicted_itinerary.lower() or "$" in predicted_itinerary or "cost" in predicted_itinerary.lower()

        # Check if it covers the destination properly
        destination_mentioned = example['destination'].split(',')[0].lower() in predicted_itinerary.lower()

        # Calculate quality score based on completeness
        score = 0
        if has_days: score += 0.4
        if has_budget: score += 0.4
        if destination_mentioned: score += 0.2

        # Perfect score if all criteria met and reasonable length
        if score >= 1.0 and len(predicted_itinerary) > 200:
            final_score = 1
        else:
            final_score = 0

        feedback_text = ""
        if final_score == 1:
            feedback_text = f"Excellent itinerary! Well-structured with daily breakdown, budget consideration, and destination focus."
        else:
            issues = []
            if not has_days:
                issues.append("missing day-by-day structure")
            if not has_budget:
                issues.append("missing budget breakdown")
            if not destination_mentioned:
                issues.append("not focused on the destination")
            if len(predicted_itinerary) <= 200:
                issues.append("too brief")

            feedback_text = f"Itinerary needs improvement. Issues: {', '.join(issues)}. Here's the expected format:\n\n{example['itinerary']}\n\nStudy this structure and create more comprehensive, well-organized travel plans."

        return dspy.Prediction(score=final_score, feedback=feedback_text)

    except Exception as e:
        feedback_text = f"Error parsing itinerary: {str(e)}. Expected format should include day-by-day breakdown with budget. Here's a good example:\n\n{example['itinerary']}"
        return dspy.Prediction(score=0, feedback=feedback_text)

train_set = train_set[:3]  # Use all 3 for training
val_set = val_set[:1]      # Use 1 for validation

optimizer = GEPA(
    metric=metric_with_feedback,
    auto="light",
    num_threads=32,
    track_stats=True,
    reflection_minibatch_size=2,
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
print("Optimized travel itinerary planner:")
cprint(optimized_program, 'green')
print(optimized_program.predict.signature.instructions)

# Save the optimized prompt to file
with open('optimized_travel_prompt.txt', 'w', encoding='utf-8') as f:
    f.write("OPTIMIZED TRAVEL ITINERARY PROMPT FROM GEPA\n")
    f.write("=" * 60 + "\n\n")
    f.write(optimized_program.predict.signature.instructions)
    f.write("\n\n" + "=" * 60 + "\n")

print("Optimized travel prompt saved to 'optimized_travel_prompt.txt'")

# Test the optimized program
print("\n" + "="*60)
print("TESTING OPTIMIZED PROGRAM:")
print("="*60)
test_result = optimized_program(
    destination="Rome, Italy",
    duration="6 days",
    budget="$2800",
    interests="history, food, art",
    travel_style="cultural gourmet"
)
print("Generated Itinerary for Rome:")
print(test_result.itinerary)

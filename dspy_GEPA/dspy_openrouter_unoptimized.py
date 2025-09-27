import dspy
import os
import json
from datasets import load_dataset

MODEL = "x-ai/grok-4-fast:free"

lm = dspy.LM(
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

def metric(example, prediction, trace=None, pred_name=None, pred_trace=None):
    correct_answer = int(example['answer'])
    try:
        llm_answer = int(prediction.answer)
    except ValueError as e:
        return 0
    return int(correct_answer == llm_answer)

# we are limiting the test set to 5 for faster testing
test_set = test_set[:5]

# Note: We had to fix a bug in DSPy's evaluate.py where the 'results' variable
# was never assigned before being used in the assertion. Added: results = executor.execute(process_item, devset) before line 161 where it says: assert len(devset) == len(results)
evaluate = dspy.Evaluate(
    devset=test_set,
    metric=metric,
    num_threads=50,
    display_table=True,
    display_progress=True,
    provide_traceback=True
)

result = evaluate(program)
print(result)

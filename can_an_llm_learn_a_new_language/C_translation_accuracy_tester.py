import asyncio
import json
import os
import re
from termcolor import colored
from B_openrouter_client import make_openrouter_call

# Configuration
MODEL_NAMES = [
    # "nvidia/nemotron-nano-9b-v2",
    "openrouter/sonoma-sky-alpha",
    # "x-ai/grok-code-fast-1",
    # "moonshotai/kimi-k2-0905",
    # "qwen/qwen3-max",
    # "deepseek/deepseek-chat-v3.1",
    # "z-ai/glm-4.5",
    # "openai/gpt-5-mini",
    # "openai/gpt-5",
    # "google/gemini-2.5-pro",
    # "anthropic/claude-sonnet-4",
    # "x-ai/grok-4",
]

REASONING_EFFORT = "medium"
DICTIONARY_FILE = "inflated_dictionary.json" # The main dictionary file

JSON_FILES = [
    # "text_10-words.json",
    # "text_200-words.json",
    "text_500-words.json"
]


RETRY_DELAY_SECONDS = 5  # Wait time between retries on API errors
MAX_RETRIES = 3  # Maximum number of retry attempts per request

def load_dictionary():
    """Load the fictional language dictionary"""
    try:
        with open(DICTIONARY_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {DICTIONARY_FILE} not found")
        return {}

# Note: load_sentences() function removed - using load_sentences_from_file() instead

def load_sentences_from_file(json_file):
    """Load sentences from a specific JSON file"""
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # Try different keys for different file formats
            if 'sentences' in data:
                # Handle old format (array of strings)
                return data['sentences']
            elif 'snippets' in data:
                snippets = data['snippets']
                # Handle new format (array of objects with original_text and expected_translation)
                if snippets and isinstance(snippets[0], dict) and 'original_text' in snippets[0]:
                    return [{'text': s['original_text'], 'expected_translation': s.get('expected_translation', '')} for s in snippets]
                else:
                    # Handle old format (array of strings)
                    return snippets
            else:
                print(f"Warning: Could not find 'sentences' or 'snippets' key in {json_file}")
                return []
    except FileNotFoundError:
        print(f"Error: {json_file} not found")
        return []
    except json.JSONDecodeError:
        print(f"Error: {json_file} is not valid JSON")
        return []

def clean_word(word):
    """Clean a word by removing punctuation"""
    return re.sub(r'[^\w]', '', word.lower())

def preserve_punctuation(original_word, translated_word):
    """Preserve punctuation from original word in translated word"""
    # Extract punctuation from original word
    punctuation_start = ''
    punctuation_end = ''

    # Find leading punctuation
    match_start = re.match(r'^[^\w]*', original_word)
    if match_start:
        punctuation_start = match_start.group()

    # Find trailing punctuation
    match_end = re.search(r'[^\w]*$', original_word)
    if match_end:
        punctuation_end = match_end.group()

    # Return translated word with preserved punctuation
    return punctuation_start + translated_word + punctuation_end

def get_expected_translation(text, dictionary):
    """Get the expected translation using our dictionary while preserving punctuation"""
    words = text.split()
    translated_words = []

    for word in words:
        clean_w = clean_word(word)
        if clean_w in dictionary:
            # Use translated word with preserved punctuation
            translated_word = preserve_punctuation(word, dictionary[clean_w])
            translated_words.append(translated_word)
        else:
            # Keep original word if not in dictionary
            translated_words.append(word)

    return ' '.join(translated_words)

def parse_model_response(response_text):
    """Parse the model's response to extract the translated sentence"""
    # Try to extract the translation from the response
    # Look for patterns like "Translation:" or just take the first sentence-like response
    lines = response_text.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('Based on') and not line.startswith('Using'):
            # Clean up any extra formatting
            line = re.sub(r'[*""]', '', line)
            return line.strip()
    return response_text.strip()

def calculate_accuracy(expected, actual):
    """Calculate word-by-word accuracy between expected and actual translation"""
    expected_words = expected.lower().split()
    actual_words = actual.lower().split()

    # Clean both lists
    expected_words = [clean_word(w) for w in expected_words]
    actual_words = [clean_word(w) for w in actual_words]

    # Remove empty strings
    expected_words = [w for w in expected_words if w]
    actual_words = [w for w in actual_words if w]

    # Calculate accuracy
    min_length = min(len(expected_words), len(actual_words))
    correct = 0

    for i in range(min_length):
        if expected_words[i] == actual_words[i]:
            correct += 1

    accuracy = correct / len(expected_words) if expected_words else 0
    return accuracy, correct, len(expected_words)

# Removed unused save_results_to_json function - using save_comprehensive_results instead

def save_comprehensive_results(all_results, model_summaries):
    """Save comprehensive results for all models and files"""
    import time

    # Create results folder if it doesn't exist
    results_folder = "results"
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)
        print(colored(f"📁 Created results folder: {results_folder}", "cyan"))

    # Prepare comprehensive results structure
    comprehensive_data = {
        "test_timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_models_tested": len(model_summaries),
        "total_files_tested": len(all_results),
        "model_summaries": {},
        "detailed_results": []
    }

    # Add model summaries (sorted by accuracy)
    sorted_models = sorted(model_summaries.items(), key=lambda x: x[1]['overall_accuracy'], reverse=True)

    for rank, (model_name, summary) in enumerate(sorted_models, 1):
        comprehensive_data["model_summaries"][model_name] = {
            "rank": rank,
            "overall_accuracy": round(summary['overall_accuracy'], 2),
            "total_correct_words": summary['total_correct_words'],
            "total_words": summary['total_words'],
            "files_tested": summary['files_tested'],
            "file_breakdown": []
        }

        # Add file breakdown for this model
        for file_result in summary['file_results']:
            file_breakdown = {
                "json_file": file_result['json_file'],
                "accuracy": round(file_result['overall_accuracy'], 2),
                "correct_words": file_result['total_correct_words'],
                "total_words": file_result['total_words']
            }
            comprehensive_data["model_summaries"][model_name]["file_breakdown"].append(file_breakdown)

    # Add detailed results for each test
    for result in all_results:
        detailed_result = {
            "model_name": result['model_name'],
            "json_file": result['json_file'],
            "overall_accuracy": round(result['overall_accuracy'], 2),
            "total_correct_words": result['total_correct_words'],
            "total_words": result['total_words'],
            "sentences": []
        }

        # Add individual sentence results
        for sentence_result in result['sentence_results']:
            sentence_detail = {
                "original_text": sentence_result['original_text'],
                "expected_translation": sentence_result['expected_translation'],
                "predicted_translation": sentence_result['predicted_translation'],
                "correct_words": sentence_result['correct_words'],
                "total_words": sentence_result['total_words']
            }
            detailed_result["sentences"].append(sentence_detail)

        comprehensive_data["detailed_results"].append(detailed_result)

    # Generate filename with timestamp
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"comprehensive_translation_results_{timestamp}.json"
    filepath = os.path.join(results_folder, filename)

    # Save comprehensive results
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(comprehensive_data, file, indent=2, ensure_ascii=False)

    print(colored(f"\n📊 Comprehensive results saved to: {filepath}", "green", attrs=["bold", "underline"]))

async def test_translation_accuracy(model_name, json_file):
    """Test translation accuracy for a specific model and JSON file"""

    # Check if API key is set
    if not os.getenv("OPENROUTER_API_KEY"):
        print("Please set your OPENROUTER_API_KEY environment variable")
        return None

    # Load data
    dictionary = load_dictionary()
    sentences = load_sentences_from_file(json_file)

    if not dictionary:
        print("Dictionary not loaded. Exiting.")
        return None

    if not sentences:
        print(f"Sentences not loaded from {json_file}. Skipping.")
        return None

    print(f"  📚 Dictionary: {len(dictionary)} words")
    print(f"  📄 Sentences: {len(sentences)} from {json_file}")
    print(f"  🤖 Model: {model_name}")
    print("  " + "=" * 50)

    # Prepare dictionary for prompt
    dict_sample = dict(list(dictionary.items()))  
    dict_str = json.dumps(dict_sample, indent=2)

    # Create tasks for parallel processing
    tasks = []
    prompts = []  # Store prompts for retry purposes
    for sentence_item in sentences:
        # Handle both old format (string) and new format (dict with 'text' key)
        if isinstance(sentence_item, dict):
            sentence = sentence_item['text']
            expected_translation = sentence_item.get('expected_translation', '')
        else:
            sentence = sentence_item
            expected_translation = ''

        prompt = f"""You are given a dictionary that maps English words to a fictional language.
Here is a sample of the dictionary:

{dict_str}

Your task: Translate the following English sentence to the fictional language using ONLY the dictionary mappings provided above as a pattern. Apply the same transformation rules to each word:

SENTENCE: "{sentence}"

Return only the translated sentence, nothing else. Do not explain your reasoning. Do not output any explanation or anything else other than only the translated sentence."""

        prompts.append(prompt)
        messages = [
            {"role": "user", "content": prompt}
            ]
        tasks.append(make_openrouter_call(model_name, messages, REASONING_EFFORT))

    # Execute all requests in parallel with retry logic
    print(colored("    📡 Sending parallel requests to model...", "cyan"))
    responses = await asyncio.gather(*tasks, return_exceptions=True)

    # Handle retries for failed requests
    for attempt in range(MAX_RETRIES):
        failed_requests = []
        failed_indices = []

        for i, response in enumerate(responses):
            if isinstance(response, Exception):
                failed_requests.append((i, prompts[i]))
                failed_indices.append(i)

        if not failed_requests:
            break  # No more failures, exit retry loop

        if attempt == 0:
            print(colored(f"      Found {len(failed_requests)} failed requests, starting retry process...", "yellow"))
        else:
            print(colored(f"      Retry attempt {attempt + 1}/{MAX_RETRIES} for {len(failed_requests)} failed requests...", "yellow"))

        # Wait before retrying
        if attempt > 0 or len(failed_requests) < len(responses):  # Don't wait on first attempt if all failed
            print(colored(f"        Waiting {RETRY_DELAY_SECONDS} seconds before retry...", "cyan"))
            await asyncio.sleep(RETRY_DELAY_SECONDS)

        # Create retry tasks
        retry_tasks = []
        for idx, prompt in failed_requests:
            messages = [{"role": "user", "content": prompt}]
            retry_tasks.append(make_openrouter_call(model_name, messages))

        # Execute retry batch
        retry_responses = await asyncio.gather(*retry_tasks, return_exceptions=True)

        # Update responses with successful retries
        success_count = 0
        for i, (original_idx, _) in enumerate(failed_requests):
            if not isinstance(retry_responses[i], Exception):
                responses[original_idx] = retry_responses[i]
                success_count += 1
                print(colored(f"        Request {original_idx+1} retry successful", "green"))
            else:
                print(colored(f"        Request {original_idx+1} retry {attempt + 1} failed: {retry_responses[i]}", "red"))

        if success_count > 0:
            print(colored(f"      Retry attempt {attempt + 1}: {success_count}/{len(failed_requests)} requests recovered", "cyan"))

        if attempt == MAX_RETRIES - 1:
            final_failures = sum(1 for resp in responses if isinstance(resp, Exception))
            if final_failures > 0:
                print(colored(f"      Final result: {final_failures} requests failed after {MAX_RETRIES} retry attempts", "red"))

    # Process results
    total_correct_words = 0
    total_words = 0
    results = []

    print("\n" + "=" * 80)
    print(colored("TRANSLATION ACCURACY RESULTS", "yellow", attrs=["bold"]))
    print("=" * 80)

    for i, (sentence_item, response) in enumerate(zip(sentences, responses), 1):
        # Handle both old format (string) and new format (dict)
        if isinstance(sentence_item, dict):
            sentence = sentence_item['text']
            provided_expected = sentence_item.get('expected_translation', '')
        else:
            sentence = sentence_item
            provided_expected = ''

        # print(colored(f"\n      Sentence {i}:", "green", attrs=["bold"]))
        # print(colored(f"      Original: {sentence}", "white"))

        # Use provided expected translation if available, otherwise calculate it
        if provided_expected:
            expected_translation = provided_expected
        else:
            expected_translation = get_expected_translation(sentence, dictionary)

        if isinstance(response, Exception):
            print(colored(f"        ERROR: {response}", "red"))
            model_translation = "ERROR"
            correct_words = 0
            total_words_sentence = len(sentence.split())
        elif response:
            model_translation = parse_model_response(response.choices[0].message.content)

            # Decode Unicode escapes for better display
            try:
                display_predicted = model_translation.encode('utf-8').decode('unicode_escape')
                display_expected = expected_translation.encode('utf-8').decode('unicode_escape')
            except:
                display_predicted = model_translation
                display_expected = expected_translation

            # print(colored(f"        Expected: {display_expected}", "cyan"))
            # print(colored(f"        Predicted: {display_predicted}", "blue"))

            accuracy, correct_words, total_words_sentence = calculate_accuracy(expected_translation, model_translation)

            # Color code the result based on accuracy
            if accuracy >= 0.8:
                color = "green"
            elif accuracy >= 0.6:
                color = "yellow"
            elif accuracy >= 0.4:
                color = "magenta"
            else:
                color = "red"

            # print(colored(f"        Correct words: {correct_words} out of {total_words_sentence}", color, attrs=["bold"]))
        else:
            print(colored("        No response received", "red"))
            model_translation = "NO_RESPONSE"
            correct_words = 0
            total_words_sentence = len(sentence.split())

        total_correct_words += correct_words
        total_words += total_words_sentence

        results.append({
            'original_text': sentence,
            'expected_translation': expected_translation,
            'predicted_translation': model_translation,
            'correct_words': correct_words,
            'total_words': total_words_sentence
        })

    # Calculate overall statistics
    if total_words > 0:
        overall_accuracy = (total_correct_words / total_words) * 100
    else:
        overall_accuracy = 0

    print("    " + "=" * 60)
    print(colored(f"    📊 RESULTS: {json_file} with {model_name}", "yellow", attrs=["bold", "underline"]))
    print("    " + "=" * 60)

    # Color code the final percentage
    if overall_accuracy >= 80:
        final_color = "green"
    elif overall_accuracy >= 60:
        final_color = "yellow"
    elif overall_accuracy >= 40:
        final_color = "magenta"
    else:
        final_color = "red"

    print(colored(f"    ✅ Total correct words: {total_correct_words} out of {total_words}", "cyan", attrs=["bold"]))
    print(colored(f"    🎯 Overall accuracy: {overall_accuracy:.1f}%", final_color, attrs=["bold", "underline"]))

    return {
        'model_name': model_name,
        'json_file': json_file,
        'total_correct_words': total_correct_words,
        'total_words': total_words,
        'overall_accuracy': overall_accuracy,
        'sentence_results': results
    }

async def main():
    """Main function to run translation accuracy tests across multiple models and JSON files"""

    print(colored("🚀 MULTI-MODEL TRANSLATION ACCURACY TESTER", "yellow", attrs=["bold", "underline"]))
    print(colored("=" * 80, "yellow"))

    # Check if API key is set
    if not os.getenv("OPENROUTER_API_KEY"):
        print(colored("❌ ERROR: Please set your OPENROUTER_API_KEY environment variable", "red", attrs=["bold"]))
        print(colored("Example: export OPENROUTER_API_KEY='your-api-key-here'", "cyan"))
        return

    # Load dictionary once
    dictionary = load_dictionary()
    if not dictionary:
        print(colored("❌ ERROR: Could not load dictionary", "red", attrs=["bold"]))
        return

    print(colored(f"📚 Loaded dictionary with {len(dictionary)} words", "green"))

    # Results storage
    all_results = []
    model_summaries = {}

    # Iterate through models
    for model_idx, model_name in enumerate(MODEL_NAMES, 1):
        print(colored(f"\n🤖 MODEL {model_idx}/{len(MODEL_NAMES)}: {model_name}", "blue", attrs=["bold", "underline"]))
        print("=" * 80)

        model_results = []

        # Iterate through JSON files for this model
        for json_idx, json_file in enumerate(JSON_FILES, 1):
            print(colored(f"\n📄 Testing {json_file} ({json_idx}/{len(JSON_FILES)})", "cyan", attrs=["bold"]))

            # Run test for this model and JSON file
            result = await test_translation_accuracy(model_name, json_file)

            if result:
                model_results.append(result)
                all_results.append(result)
            else:
                print(colored(f"    ❌ Skipped {json_file} for {model_name}", "red"))

        # Calculate model summary
        if model_results:
            model_total_correct = sum(r['total_correct_words'] for r in model_results)
            model_total_words = sum(r['total_words'] for r in model_results)
            model_overall_accuracy = (model_total_correct / model_total_words * 100) if model_total_words > 0 else 0

            model_summaries[model_name] = {
                'total_correct_words': model_total_correct,
                'total_words': model_total_words,
                'overall_accuracy': model_overall_accuracy,
                'files_tested': len(model_results),
                'file_results': model_results
            }

            print(colored(f"\n📈 MODEL SUMMARY: {model_name}", "green", attrs=["bold"]))
            print(colored(f"   Files tested: {len(model_results)}", "cyan"))
            print(colored(f"   Total correct words: {model_total_correct} out of {model_total_words}", "cyan"))
            print(colored(f"   Overall accuracy: {model_overall_accuracy:.1f}%", "green", attrs=["bold"]))

    # Save comprehensive results
    if all_results:
        save_comprehensive_results(all_results, model_summaries)

    # Print final summary
    print_final_summary(model_summaries)

async def print_final_summary(model_summaries):
    """Print final summary of all models"""
    if not model_summaries:
        return

    print(colored("\n" + "=" * 80, "yellow"))
    print(colored("🏆 FINAL SUMMARY - ALL MODELS", "yellow", attrs=["bold", "underline"]))
    print(colored("=" * 80, "yellow"))

    # Sort models by accuracy
    sorted_models = sorted(model_summaries.items(), key=lambda x: x[1]['overall_accuracy'], reverse=True)

    for rank, (model_name, summary) in enumerate(sorted_models, 1):
        accuracy_color = "green" if summary['overall_accuracy'] >= 80 else "yellow" if summary['overall_accuracy'] >= 60 else "magenta" if summary['overall_accuracy'] >= 40 else "red"

        print(colored(f"{rank:2d}. {model_name}", "cyan", attrs=["bold"]))
        print(colored(f"    Files: {summary['files_tested']} | Words: {summary['total_correct_words']}/{summary['total_words']} | Accuracy: {summary['overall_accuracy']:.1f}%", accuracy_color))

if __name__ == "__main__":
    asyncio.run(main())

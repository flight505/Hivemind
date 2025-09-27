#!/usr/bin/env python3
"""
Script to create a subset dictionary from the inflated dictionary,
containing all words from specified JSON files plus random additional words.
"""

import json
import random
import re
from termcolor import colored

# IMPORTANT VARIABLES (ALL CAPS)
ORIGINAL_DICTIONARY_PATH = "inflated_dictionary.json"  # Use the inflated dictionary as source
JSON_FILE_TO_PROCESS = "text_10-words.json"  # JSON file to extract words/phrases from
OUTPUT_DICTIONARY_PATH = "subset_dictionary.json"  # Output subset dictionary
ADDITIONAL_RANDOM_WORDS = 0  # Number of extra random words to include

def load_original_dictionary():
    """Load the original fictional language dictionary."""
    try:
        with open(ORIGINAL_DICTIONARY_PATH, 'r', encoding='utf-8') as file:
            dictionary = json.load(file)
        print(colored(f"✓ Successfully loaded original dictionary with {len(dictionary)} words", "green"))
        return dictionary
    except FileNotFoundError:
        print(colored(f"✗ Error: Dictionary file {ORIGINAL_DICTIONARY_PATH} not found", "red"))
        return None
    except json.JSONDecodeError:
        print(colored(f"✗ Error: Invalid JSON format in {ORIGINAL_DICTIONARY_PATH}", "red"))
        return None

def load_json_snippets():
    """Load text snippets from the specified JSON file."""
    try:
        with open(JSON_FILE_TO_PROCESS, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Handle different JSON formats
        if 'snippets' in data:
            snippets = data['snippets']
            # Handle new format with objects containing original_text
            if snippets and isinstance(snippets[0], dict) and 'original_text' in snippets[0]:
                sentences = [snippet['original_text'] for snippet in snippets]
            else:
                sentences = snippets
        elif 'sentences' in data:
            sentences = data['sentences']
        else:
            print(colored(f"✗ Error: No 'snippets' or 'sentences' key found in {JSON_FILE_TO_PROCESS}", "red"))
            return None

        print(colored(f"✓ Successfully loaded {len(sentences)} text items from {JSON_FILE_TO_PROCESS}", "green"))
        return sentences
    except FileNotFoundError:
        print(colored(f"✗ Error: JSON file {JSON_FILE_TO_PROCESS} not found", "red"))
        return None
    except json.JSONDecodeError:
        print(colored(f"✗ Error: Invalid JSON format in {JSON_FILE_TO_PROCESS}", "red"))
        return None

def extract_words_from_sentences(sentences):
    """Extract all unique words from the sentences."""
    all_words = set()

    for sentence in sentences:
        # Handle both string sentences and objects with original_text
        if isinstance(sentence, dict):
            text = sentence.get('original_text', '')
        else:
            text = sentence

        # Split into words but keep punctuation (to match our dictionary keys)
        words = text.split()
        all_words.update(words)

    print(colored(f"✓ Extracted {len(all_words)} unique words/phrases from text", "green"))
    return all_words

def create_subset_dictionary(original_dict, required_words, additional_count):
    """Create a subset dictionary with required words plus random additional words."""
    # Start with all required words
    subset_dict = {}

    # Add all required words (from the JSON sentences)
    missing_words = []
    for word in required_words:
        if word in original_dict:
            subset_dict[word] = original_dict[word]
        else:
            missing_words.append(word)

    if missing_words:
        print(colored(f"⚠ Warning: {len(missing_words)} words from sentences not found in dictionary: {missing_words[:10]}...", "yellow"))

    print(colored(f"✓ Added {len(subset_dict)} required words from sentences", "green"))

    # Get words that aren't already in the subset
    available_words = [word for word in original_dict.keys() if word not in subset_dict]

    # Randomly select additional words
    if additional_count > 0 and len(available_words) > 0:
        # Ensure we don't try to select more words than available
        num_to_select = min(additional_count, len(available_words))
        random_words = random.sample(available_words, num_to_select)

        for word in random_words:
            subset_dict[word] = original_dict[word]

        print(colored(f"✓ Added {len(random_words)} random additional words", "green"))
    else:
        print(colored("⚠ No additional random words added (none available or count=0)", "yellow"))

    return subset_dict

def save_subset_dictionary(subset_dict):
    """Save the subset dictionary to a JSON file."""
    try:
        with open(OUTPUT_DICTIONARY_PATH, 'w', encoding='utf-8') as file:
            json.dump(subset_dict, file, indent=2, ensure_ascii=False)

        print(colored(f"✓ Subset dictionary saved to {OUTPUT_DICTIONARY_PATH}", "green"))
        print(colored(f"✓ Total words in subset dictionary: {len(subset_dict)}", "blue"))
        return True
    except Exception as e:
        print(colored(f"✗ Error saving dictionary: {e}", "red"))
        return False

def print_dictionary_stats(original_dict, subset_dict, required_words):
    """Print statistics about the dictionary creation."""
    print(colored("\n📊 DICTIONARY CREATION SUMMARY", "cyan", attrs=['bold']))
    print(colored("=" * 50, "cyan"))

    print(colored("Original dictionary:", "yellow", attrs=['bold']) +
          colored(f" {len(original_dict)} words", "white"))

    print(colored("Words from JSON snippets:", "yellow", attrs=['bold']) +
          colored(f" {len(required_words)} words/phrases", "white"))

    print(colored("Words actually found in dictionary:", "yellow", attrs=['bold']) +
          colored(f" {len(subset_dict)} words", "white"))

    print(colored("Additional random words:", "yellow", attrs=['bold']) +
          colored(f" {len(subset_dict) - len([w for w in required_words if w in original_dict])} words", "white"))

    print(colored("Coverage of required words:", "yellow", attrs=['bold']) +
          colored(f" {len([w for w in required_words if w in original_dict])}/{len(required_words)} ({len([w for w in required_words if w in original_dict])/len(required_words)*100:.1f}%)", "white"))

def main():
    """Main function to orchestrate the subset dictionary creation from inflated dictionary."""
    print(colored("🚀 Starting subset dictionary creation from inflated dictionary...", "blue", attrs=['bold']))

    # Load original dictionary
    original_dict = load_original_dictionary()
    if not original_dict:
        return False

    # Load text snippets from JSON
    snippets = load_json_snippets()
    if snippets is None:
        return False

    # Extract words from snippets
    required_words = extract_words_from_sentences(snippets)

    # Create subset dictionary
    subset_dict = create_subset_dictionary(original_dict, required_words, ADDITIONAL_RANDOM_WORDS)

    # Save the subset dictionary
    if save_subset_dictionary(subset_dict):
        # Print statistics
        print_dictionary_stats(original_dict, subset_dict, required_words)

        print(colored("\n✅ Subset dictionary creation from inflated dictionary completed successfully!", "green", attrs=['bold']))
        return True
    else:
        return False

if __name__ == "__main__":
    main()

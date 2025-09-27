import json
import re
import random

# ADJUSTABLE PARAMETERS
WORD_COUNTS = [10, 200, 500]  # Word counts for snippets
NUM_SNIPPETS_PER_FILE = 10  # Number of snippets to extract per file
ORIGINAL_DICTIONARY_FILE = "full_dictionary.json"  # Original dictionary from snippets
INFLATED_DICTIONARY_FILE = "inflated_dictionary.json"  # Inflated dictionary with additional words
TARGET_DICTIONARY_SIZE = 5000  # Target size for inflated dictionary



def load_dictionary(dictionary_file=None):
    """Load the fictional language dictionary"""
    if dictionary_file is None:
        dictionary_file = ORIGINAL_DICTIONARY_FILE

    try:
        with open(dictionary_file, 'r', encoding='utf-8') as file:
            dictionary = json.load(file)
            print(f"📚 Successfully loaded dictionary with {len(dictionary)} words from {dictionary_file}")
            return dictionary
    except FileNotFoundError:
        print(f"⚠️  Warning: {dictionary_file} not found")
        return {}
    except json.JSONDecodeError as e:
        print(f"⚠️  Warning: {dictionary_file} is not valid JSON: {e}")
        return {}

def clean_text(text):
    """Clean the text by removing extra whitespace and normalizing"""
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text.strip())
    # Remove chapter headers and numbers
    text = re.sub(r'CHAPTER \d+\.', '', text)
    text = re.sub(r'CHAPTER \d+.*?\n', '', text)
    return text

def extract_word_snippets(text, word_count, num_snippets=10):
    """Extract unique snippets of specified word count"""
    words = text.split()
    snippets = []

    # Calculate maximum possible start positions
    max_start = len(words) - word_count

    if max_start <= 0:
        return ["Text is too short for the requested word count"]

    # Generate unique random start positions with minimum spacing
    start_positions = set()
    min_distance = word_count // 2  # Ensure snippets don't overlap too much

    while len(start_positions) < num_snippets:
        new_pos = random.randint(0, max_start)
        # Check if this position is far enough from existing positions
        too_close = False
        for existing_pos in start_positions:
            if abs(new_pos - existing_pos) < min_distance:
                too_close = True
                break
        if not too_close:
            start_positions.add(new_pos)

    for start_pos in sorted(start_positions):
        end_pos = start_pos + word_count
        snippet = ' '.join(words[start_pos:end_pos])
        # Verify the snippet has exactly the right word count
        if len(snippet.split()) == word_count:
            snippets.append(snippet)

    return snippets[:num_snippets]  # Return exactly num_snippets

def clean_word(word):
    """Clean a word by removing punctuation for dictionary lookup"""
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

def verify_word_counts(filename, expected_count):
    """Verify that all snippets in a JSON file have the expected word count"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        print(f"\nVerifying {filename}:")
        print(f"Expected word count per snippet: {expected_count}")

        # Handle different key names (snippets vs sentences)
        key_name = 'snippets' if 'snippets' in data else 'sentences'
        items = data[key_name]

        all_correct = True
        for i, item in enumerate(items, 1):
            # Handle both old format (string) and new format (dict with original_text)
            if isinstance(item, dict):
                text = item.get('original_text', '')
            else:
                text = item

            word_count = len(text.split())
            status = "✓" if word_count == expected_count else "✗"
            print(f"Snippet {i}: {word_count} words {status}")
            if word_count != expected_count:
                all_correct = False

        total_snippets = len(items)
        print(f"Total snippets: {total_snippets}")
        print(f"All snippets correct: {'✓' if all_correct else '✗'}")

        return all_correct

    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return False
    except json.JSONDecodeError:
        print(f"Error: {filename} is not valid JSON")
        return False

def extract_unique_words_from_json(json_file, key_name):
    """Extract all unique words from a JSON file"""
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        words = set()

        # Handle different key names
        if key_name in data:
            items = data[key_name]
        else:
            # Try alternative keys
            for alt_key in ['snippets', 'sentences']:
                if alt_key in data:
                    items = data[alt_key]
                    break
            else:
                print(f"Warning: Could not find content in {json_file}")
                return set()

        for item in items:
            # Handle both old format (string) and new format (dict with original_text)
            if isinstance(item, dict):
                text = item.get('original_text', '')
            else:
                text = item

            # Split into words and clean punctuation for dictionary creation
            item_words = text.split()
            for word in item_words:
                cleaned_word = clean_word(word)  # Clean punctuation for consistent dictionary keys
                if cleaned_word:
                    words.add(cleaned_word)

        return words

    except FileNotFoundError:
        print(f"Warning: {json_file} not found")
        return set()
    except json.JSONDecodeError:
        print(f"Warning: {json_file} is not valid JSON")
        return set()

def is_consonant(char):
    """Check if a character is a consonant"""
    return char.lower() in 'bcdfghjklmnpqrstvwxyz'

def is_vowel(char):
    """Check if a character is a vowel"""
    return char.lower() in 'aeiou'

def create_fictional_word(word):
    """Convert a word to fictional language (punctuation already cleaned)"""
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'

    result = []
    for char in word:
        if char.isdigit():
            # Keep numbers as they are
            result.append(char)
        elif is_consonant(char.lower()):
            # Replace consonant with random consonant (case-insensitive)
            result.append(random.choice(consonants))
        elif is_vowel(char.lower()):
            # Replace vowel with random vowel (case-insensitive)
            result.append(random.choice(vowels))
        else:
            # This shouldn't happen since punctuation is cleaned, but just in case
            result.append(char)

    return ''.join(result)

def extract_words_from_text_file(text_file):
    """Extract all unique words from a text file"""
    try:
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Clean the text
        cleaned_text = clean_text(text)

        # Split into words and clean them
        words = set()
        for word in cleaned_text.split():
            cleaned_word = clean_word(word)
            if cleaned_word and not cleaned_word.isdigit():
                words.add(cleaned_word)  # Use cleaned word without punctuation

        print(f"📖 Extracted {len(words)} unique words from {text_file}")
        return words

    except FileNotFoundError:
        print(f"⚠️  Warning: {text_file} not found")
        return set()

def inflate_dictionary_to_target_size(existing_dict, target_size):
    """Inflate dictionary to target size by adding words from text.txt"""
    print(f"\n🔄 Inflating dictionary from {len(existing_dict)} to {target_size} words...")

    if len(existing_dict) >= target_size:
        print("✅ Dictionary already meets target size")
        return existing_dict

    # Extract additional words from text.txt
    text_words = extract_words_from_text_file('text.txt')

    # Get words not already in dictionary
    existing_words = set(existing_dict.keys())
    new_words = text_words - existing_words

    if not new_words:
        print("⚠️  No new words available from text.txt")
        return existing_dict

    # Sort new words for consistent ordering
    new_words_list = sorted(list(new_words))

    # Calculate how many words we need to add
    words_to_add = min(target_size - len(existing_dict), len(new_words_list))
    words_to_add_list = new_words_list[:words_to_add]

    # Add new words to dictionary
    inflated_dict = existing_dict.copy()
    for word in words_to_add_list:
        # Clean the word for dictionary key
        cleaned_word = clean_word(word)
        if cleaned_word and cleaned_word not in inflated_dict:
            fictional_word = create_fictional_word(cleaned_word)
            inflated_dict[cleaned_word] = fictional_word

    print(f"✅ Added {len(words_to_add_list)} new words to dictionary")

    # Save inflated dictionary
    with open(INFLATED_DICTIONARY_FILE, 'w', encoding='utf-8') as file:
        json.dump(inflated_dict, file, indent=2, ensure_ascii=False)

    print(f"💾 Inflated dictionary saved to {INFLATED_DICTIONARY_FILE} with {len(inflated_dict)} total words")

    # Show some examples of newly added words
    if words_to_add_list:
        print("\n📝 Examples of newly added words:")
        examples = words_to_add_list[:5]
        for word in examples:
            print(f"{word} -> {inflated_dict[word]}")

    return inflated_dict

def create_fictional_dictionary_from_files():
    """Create fictional dictionary from all the generated JSON files"""
    # List of JSON files to process with their expected key names
    json_files = []
    for word_count in WORD_COUNTS:
        json_files.append((f'text_{word_count}-words.json', 'snippets'))

    # Extract all unique words from all files
    all_words = set()

    for json_file, key_name in json_files:
        words_from_file = extract_unique_words_from_json(json_file, key_name)
        all_words.update(words_from_file)

    # Remove empty strings and pure numbers if any
    all_words = {word for word in all_words if word and not word.isdigit()}

    print(f"Found {len(all_words)} unique words across all files")

    # Create fictional dictionary with cleaned words as keys
    fictional_dictionary = {}

    for word in sorted(all_words):
        # Clean the word for dictionary key (remove punctuation)
        cleaned_word = clean_word(word)
        if cleaned_word:
            fictional_word = create_fictional_word(cleaned_word)
            fictional_dictionary[cleaned_word] = fictional_word

    # Save original dictionary (from snippets only)
    with open(ORIGINAL_DICTIONARY_FILE, 'w', encoding='utf-8') as file:
        json.dump(fictional_dictionary, file, indent=2, ensure_ascii=False)

    print(f"Created original fictional language dictionary with {len(fictional_dictionary)} word mappings")
    print(f"Saved to: {ORIGINAL_DICTIONARY_FILE}")

    # Show a few examples
    print("\nExamples of word transformations:")
    examples = list(fictional_dictionary.items())[:10]
    for original, fictional in examples:
        print(f"{original} -> {fictional}")

    # Inflate dictionary to target size
    inflated_dict = inflate_dictionary_to_target_size(fictional_dictionary, TARGET_DICTIONARY_SIZE)

    return inflated_dict

def main():
    print("🚀 COMPREHENSIVE TEXT SNIPPET GENERATOR")
    print("=" * 60)

    # Read the text file
    try:
        with open('text.txt', 'r', encoding='utf-8') as file:
            raw_text = file.read()
    except FileNotFoundError:
        print("Error: text.txt file not found")
        return

    # Clean the text
    cleaned_text = clean_text(raw_text)
    print(f"📄 Cleaned text has {len(cleaned_text.split())} words")

    # Process each word count
    for word_count in WORD_COUNTS:
        print(f"\n📝 Processing {word_count}-word snippets...")

        # Extract snippets
        snippets = extract_word_snippets(cleaned_text, word_count, NUM_SNIPPETS_PER_FILE)

        # Create JSON structure with translations
        data = {
            "snippets": []
        }

        for snippet in snippets:
            snippet_data = {
                "original_text": snippet
            }
            data["snippets"].append(snippet_data)

        # Write to JSON file
        filename = f'text_{word_count}-words.json'
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

        print(f"✅ Created {filename} with {len(snippets)} unique {word_count}-word snippets")

    print("\n📋 VERIFICATION PHASE")
    print("=" * 60)

    # Verify word counts
    verification_results = []
    for word_count in WORD_COUNTS:
        filename = f'text_{word_count}-words.json'
        print(f"\n🔍 Verifying {filename}...")
        is_correct = verify_word_counts(filename, word_count)
        verification_results.append(is_correct)

    print("\n📚 DICTIONARY CREATION PHASE")
    print("=" * 60)

    # Create fictional dictionary
    print("\n🏗️  Creating fictional language dictionary...")
    fictional_dict = create_fictional_dictionary_from_files()

    print("\n🔄 SECOND PASS - ADD TRANSLATIONS")
    print("=" * 60)

    # Now add translations to all files using the inflated dictionary
    if fictional_dict:
        print("📝 Adding translations to all JSON files using inflated dictionary...")

        for word_count in WORD_COUNTS:
            filename = f'text_{word_count}-words.json'

            # Read existing file
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Add translations to each snippet
            for snippet_data in data["snippets"]:
                original_text = snippet_data["original_text"]
                expected_translation = get_expected_translation(original_text, fictional_dict)
                snippet_data["expected_translation"] = expected_translation

            # Write back to file
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)

            # Calculate translation coverage
            total_words = sum(len(snippet["original_text"].split()) for snippet in data["snippets"])
            translated_words = 0

            for snippet in data["snippets"]:
                for word in snippet["original_text"].split():
                    clean_w = clean_word(word)
                    if clean_w in fictional_dict:
                        translated_words += 1

            coverage = (translated_words / total_words * 100) if total_words > 0 else 0
            print(f"✅ Updated {filename} - Translation coverage: {coverage:.1f}%")

    print("\n" + "="*60)
    print("🧹 PUNCTUATION CLEANUP SUMMARY:")
    print("- Dictionary keys: All punctuation removed for consistent lookups")
    print("- Word extraction: Cleaned words used for dictionary creation")
    print("- Translation lookup: Uses cleaned words for reliable matching")
    print("- Expected result: Much higher translation coverage (close to 100%)")

    print("\n🎉 ALL TASKS COMPLETED!")
    print("=" * 60)
    print("✅ Text snippet generation: COMPLETE")
    print("✅ Word count verification: COMPLETE")
    print("✅ Original dictionary creation: COMPLETE")
    print("✅ Dictionary inflation: COMPLETE")
    print("✅ Translation addition: COMPLETE")
    print("\n📊 SUMMARY:")
    print(f"- Word counts processed: {WORD_COUNTS}")
    print(f"- Snippets per file: {NUM_SNIPPETS_PER_FILE}")
    print(f"- Files created: {len(WORD_COUNTS)}")
    print(f"- Original dictionary: {ORIGINAL_DICTIONARY_FILE}")
    print(f"- Inflated dictionary: {INFLATED_DICTIONARY_FILE}")
    print(f"- Dictionary target size: {TARGET_DICTIONARY_SIZE}")
    print(f"- Dictionary final size: {len(fictional_dict) if fictional_dict else 0}")
    print(f"- Verification passed: {sum(verification_results)}/{len(verification_results)} files")

if __name__ == "__main__":
    main()
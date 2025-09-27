# LLM Translation Accuracy Benchmark

A comprehensive system for benchmarking Large Language Models on fictional language translation tasks. The system creates artificial language transformations and tests how well LLMs can learn and apply these systematic rules.

## 📁 Project Overview

This project consists of 5 Python scripts that work together to:

1. **Generate** fictional language dictionaries from English text
2. **Test** LLM translation accuracy using OpenRouter API
3. **Visualize** results with beautiful accuracy charts

## 📄 File Descriptions

### A_extract_text_snippets.py - Data Preparation
**Purpose**: Extracts text snippets and creates fictional language dictionaries

**What it does**:
- Reads `text.txt` and creates snippets of different word counts (10, 200, 500 words)
- Generates fictional language transformations using systematic rules:
  - Consonants → Random consonants (b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z)
  - Vowels → Random vowels (a,e,i,o,u)
  - Numbers stay the same
- Creates two dictionary files:
  - `full_dictionary.json` - Words from generated snippets
  - `inflated_dictionary.json` - Expanded to 5000 words from text.txt

**Key Functions**:
- `create_fictional_word()` - Applies transformation rules
- `preserve_punctuation()` - Maintains punctuation in translations
- `extract_word_snippets()` - Creates text samples of exact word counts

**Configuration**:
```python
WORD_COUNTS = [10, 200, 500]  # Snippet sizes
NUM_SNIPPETS_PER_FILE = 10     # Snippets per size
TARGET_DICTIONARY_SIZE = 5000  # Final dictionary size
```

### B_openrouter_client.py - API Client
**Purpose**: Handles OpenRouter API communication

**What it does**:
- Simple async client for OpenRouter API calls
- Configures base URL and authentication
- Handles API responses and errors

**Configuration**:
```python
# Requires environment variable:
# OPENROUTER_API_KEY=your_api_key_here
```

### C_translation_accuracy_tester.py - Main Testing Engine
**Purpose**: Tests LLM translation accuracy against the fictional language

**What it does**:
- Loads `inflated_dictionary.json` and test snippets
- Sends parallel API requests to multiple LLMs
- Compares model translations with expected results
- Calculates word-by-word accuracy scores
- Saves comprehensive results to `results/` folder

**Key Features**:
- **Parallel Processing**: Tests multiple models simultaneously
- **Retry Logic**: Handles API failures with automatic retries
- **Accurate Scoring**: Word-by-word accuracy with punctuation handling
- **Comprehensive Results**: Saves both summary and detailed results

**Configuration**:
```python
MODEL_NAMES = [
    "openai/gpt-5",
    "anthropic/claude-sonnet-4",
    # ... more models
]

JSON_FILES = ["text_500-words.json"]  # Test files to use
RETRY_DELAY_SECONDS = 5
MAX_RETRIES = 3
```

**Output Files**:
- `results/comprehensive_translation_results_*.json` - Complete results
- Includes model rankings, accuracy scores, and detailed sentence comparisons

### D_create_accuracy_chart.py - Results Visualization
**Purpose**: Creates beautiful bar charts from test results

**What it does**:
- Reads comprehensive results JSON files
- Generates professional matplotlib/seaborn bar charts
- Shows model accuracy rankings with visual styling
- Saves as high-resolution PNG files

**Configuration**:
```python
OUTPUT_IMAGE_PATH = "model_accuracy_chart.png"
FIGURE_SIZE = (18, 14)
DPI = 300
```

### E_not_used_create_subset_dictionary.py - Legacy (Unused)
**Purpose**: Creates subset dictionaries (no longer used)

**Status**: This file is legacy and not part of the active workflow. The main system uses the full inflated dictionary directly.

---

## 🔄 Complete Workflow

```
1. Data Creation Phase
   text.txt → A_extract_text_snippets.py → text_*-words.json + inflated_dictionary.json

2. Testing Phase
   inflated_dictionary.json + text_*-words.json → C_translation_accuracy_tester.py → comprehensive_results.json

3. Visualization Phase
   comprehensive_results.json → D_create_accuracy_chart.py → model_accuracy_chart.png
```

### Step-by-Step Process:

1. **Prepare Data**:
   ```bash
   python A_extract_text_snippets.py
   ```
   - Creates `text_10-words.json`, `text_200-words.json`, `text_500-words.json`
   - Creates `full_dictionary.json` and `inflated_dictionary.json`

2. **Run Accuracy Tests**:
   ```bash
   python C_translation_accuracy_tester.py
   ```
   - Requires `OPENROUTER_API_KEY` environment variable
   - Tests all configured models against all configured test files
   - Saves results to `results/` folder

3. **Create Charts** (Optional):
   ```bash
   python D_create_accuracy_chart.py
   ```
   - Update `RESULTS_JSON_PATH` in the script first
   - Generates `model_accuracy_chart.png`

---

## 📋 Dependencies

**Required Python packages**:
```bash
pip install openai termcolor matplotlib seaborn pandas
```

**Environment Variables**:
```bash
export OPENROUTER_API_KEY="your_openrouter_api_key"
```

**Required Files**:
- `text.txt` - Source text for dictionary creation
- `inflated_dictionary.json` - Created by A script
- `text_*-words.json` files - Created by A script

---

## 🎯 Key Features

### Accurate Benchmarking
- **Systematic Rules**: Fictional language follows consistent transformation patterns
- **Punctuation Preservation**: Maintains proper punctuation in translations
- **Word-by-Word Accuracy**: Precise measurement of translation quality
- **Comprehensive Testing**: Tests multiple models across multiple text lengths

### Robust Error Handling
- **API Retry Logic**: Automatically retries failed requests
- **Graceful Degradation**: Continues testing even if some models fail
- **Detailed Logging**: Clear error messages and progress tracking

### Professional Output
- **Structured Results**: JSON format with complete metadata
- **Visual Charts**: Publication-quality accuracy rankings
- **Detailed Analysis**: Sentence-level accuracy breakdowns

---

## 🚀 Quick Start

1. **Setup**:
   ```bash
   # Install dependencies
   pip install openai termcolor matplotlib seaborn pandas

   # Set API key
   export OPENROUTER_API_KEY="your_key_here"
   ```

2. **Prepare Data**:
   ```bash
   python A_extract_text_snippets.py
   ```

3. **Run Tests**:
   ```bash
   python C_translation_accuracy_tester.py
   ```

4. **View Results**:
   - Check `results/` folder for JSON results
   - Run `python D_create_accuracy_chart.py` for charts

---

## ⚙️ Configuration Options

### Model Selection (C_translation_accuracy_tester.py)
```python
MODEL_NAMES = [
    "openai/gpt-5",           # High-performance GPT model
    "anthropic/claude-sonnet-4", # Claude Sonnet
    "x-ai/grok-4",            # Grok model
    # Add more models as needed
]
```

### Test File Selection
```python
JSON_FILES = [
    "text_500-words.json",    # Large text chunks
    # "text_200-words.json",  # Medium chunks
    # "text_10-words.json",   # Small chunks
]
```

### Dictionary Size (A_extract_text_snippets.py)
```python
TARGET_DICTIONARY_SIZE = 5000  # Words in final dictionary
```

**Why Inflate the Dictionary?**

The dictionary inflation makes the benchmark more challenging by expanding from ~200-300 snippet words to 5000+ words, forcing models to learn systematic transformation rules across many examples rather than memorizing a small vocabulary. This creates meaningful differentiation between model capabilities  instead of artificial high scores (95%+). A large vocabulary better tests pattern recognition and rule generalization - key LLM capabilities. 🎯

---

## 📊 Understanding Results

### JSON Results Structure:
```json
{
  "test_timestamp": "2024-01-01 12:00:00",
  "total_models_tested": 5,
  "total_files_tested": 1,
  "model_summaries": {
    "openai/gpt-5": {
      "rank": 1,
      "overall_accuracy": 87.5,
      "total_correct_words": 1750,
      "total_words": 2000,
      "files_tested": 1
    }
  },
  "detailed_results": [
    {
      "model_name": "openai/gpt-5",
      "json_file": "text_500-words.json",
      "overall_accuracy": 87.5,
      "sentences": [...]
    }
  ]
}
```

### Accuracy Interpretation:
- **Word-by-Word**: Each word compared individually
- **Punctuation Handled**: Punctuation removed for fair comparison
- **Percentage**: Correct words / Total words × 100
- **Ranking**: Models sorted by overall accuracy

---

## 🔧 Troubleshooting

### Common Issues:

**API Errors**:
- Check `OPENROUTER_API_KEY` is set correctly
- Verify API key has sufficient credits
- Some models may be temporarily unavailable

**File Not Found**:
- Ensure `text.txt` exists in project root
- Run `A_extract_text_snippets.py` first to create required files

**Low Accuracy Scores**:
- This is expected! The fictional language rules are complex
- Models need to learn the systematic transformations
- Lower scores indicate the benchmark's difficulty (good for differentiation)

---

## 🎨 Example Output

The system generates beautiful charts showing model rankings:

```
🏆 FINAL SUMMARY - ALL MODELS
1. openai/gpt-5              - 87.5% accuracy
2. anthropic/claude-sonnet-4 - 82.3% accuracy
3. x-ai/grok-4               - 76.8% accuracy
...
```

**Chart Features**:
- Color-coded bars (red for winner, green for others)
- Rank numbers on left
- Accuracy percentages on bars
- Professional styling with high DPI

---

## 📈 Use Cases

- **Model Comparison**: Rank LLMs on systematic learning tasks
- **Benchmark Creation**: Test specific capabilities (pattern recognition, rule learning)
- **Research**: Study how different architectures handle artificial languages
- **Development**: Monitor model improvements over time

This system provides a rigorous, reproducible way to evaluate LLM performance on systematic language transformation tasks that require learning and applying artificial rules.

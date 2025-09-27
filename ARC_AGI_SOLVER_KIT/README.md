# ARC-AGI Puzzle Solver with AI

An automated system for solving ARC-AGI (Abstraction and Reasoning Corpus for Artificial General Intelligence) puzzles using large language models through OpenRouter and OpenAI APIs.

## What is ARC-AGI?

ARC-AGI is a benchmark dataset designed to test AI systems' ability to solve abstract reasoning puzzles. Each puzzle consists of:
- **Training examples**: Input-output grid pairs showing the transformation pattern
- **Test input**: A new input grid requiring the same transformation
- **Goal**: Generate the correct output grid by identifying and applying the pattern

The puzzles involve grid manipulations, pattern recognition, and logical transformations - representing a significant challenge for AI systems.

## Project Structure

```
├── solve_arc_puzzle.py          # Main parallel puzzle solver
├── API_client.py                # OpenRouter/OpenAI API client
├── puzzle_failures.py           # Tracks failed/incorrect puzzles
├── test.py                      # Grid comparison and validation
├── helper_stuff/
│   ├── __init__.py             # Package initialization
│   └── puzzle_helpers.py       # Utility functions for puzzles
├── ARC-AGI/                    # Original ARC dataset
│   └── data/
│       ├── training/           # Training puzzles (400 files)
│       └── evaluation/         # Evaluation puzzles (400 files)
└── ARC-AGI-2/                  # Extended ARC dataset
    └── data/
        ├── training/           # More training data (1000 files)
        └── evaluation/         # Evaluation puzzles (100 files)
```

## Features

- **Parallel Processing**: Solves multiple puzzles simultaneously for efficiency
- **AI-Powered Solving**: Uses advanced LLMs (OpenRouter Sonoma Sky Alpha by default)
- **Dimension Validation**: Ensures output grids match expected dimensions
- **Failure Tracking**: Automatically saves and categorizes failed puzzles
- **Flexible Puzzle Selection**: Process specific puzzles, random selection, or retry failed ones
- **Comprehensive Logging**: Colored terminal output with detailed results
- **Grid Validation**: Built-in tools to compare predicted vs expected outputs

## Setup

### Prerequisites

- Python 3.8+
- OpenRouter API key (or OpenAI API key)

### Installation

1. **Clone/Download the project**
2. **Install dependencies** (no requirements.txt needed - uses only standard libraries)
3. **Set API key**:
   ```bash
   # For OpenRouter (default)
   export OPENROUTER_API_KEY="your_openrouter_key_here"

   # Or for OpenAI
   export OPENAI_API_KEY="your_openai_key_here"
   ```

### Required Python Packages

The project uses these standard libraries (install if needed):
- `openai` - For API calls
- `termcolor` - For colored terminal output

## Usage

### Basic Puzzle Solving

Run the main solver with default settings:

```bash
python solve_arc_puzzle.py
```

This will:
- Use the ARC-AGI-2 training dataset
- Process 10 randomly selected puzzles
- Use OpenRouter Sonoma Sky Alpha model
- Display results with colored output

### Command Line Options

The script uses global variables at the top of `solve_arc_puzzle.py`. Modify these to customize behavior:

```python
# IMPORTANT VARIABLES (ALL CAPS AS REQUESTED)
PUZZLE_FOLDER = "ARC-AGI-2/data/training"  # Dataset folder
MODEL_NAME = "openrouter/sonoma-sky-alpha" # AI model to use
PROVIDER = "openrouter"                    # API provider
NUM_PUZZLES = 10                          # Number of puzzles to solve
PUZZLES = []                              # Specific puzzle files (leave empty for random)
```

### Processing Specific Puzzles

To solve specific puzzles, set the `PUZZLES` variable:

```python
PUZZLES = [
    "ARC-AGI-2/data/evaluation/c4d067a0.json",
    "ARC-AGI-2/data/evaluation/16de56c4.json"
]
```

### Retrying Failed Puzzles

The system automatically generates `puzzle_failures.py` with lists of failed puzzles. To retry them:

1. Copy the desired list from `puzzle_failures.py`
2. Paste it into `solve_arc_puzzle.py`:

```python
# Retry all problematic puzzles
PUZZLES = ALL_FAILED_PUZZLE_FILES.copy()

# Or retry only API failures
PUZZLES = API_FAILED_PUZZLE_FILES.copy()

# Or retry only incorrect answers
PUZZLES = INCORRECT_PUZZLE_FILES.copy()
```

## How It Works

### 1. Puzzle Loading
- Reads JSON puzzle files from ARC dataset
- Extracts training examples and test input
- Validates file structure

### 2. AI Prompt Formatting
Each puzzle is formatted into a detailed prompt including:
- Training examples with input/output pairs
- Clear instructions on pattern recognition
- Dimension requirements
- Output format specifications
- Validation checklist

### 3. Parallel API Calls
- Makes concurrent requests to AI models
- Uses async/await for efficient processing
- Handles API errors gracefully

### 4. Response Processing
- Extracts JSON arrays from AI responses
- Validates grid dimensions match expected output
- Compares predicted vs expected grids
- Categorizes results: correct, incorrect, or API failure

### 5. Results Analysis
- Calculates accuracy statistics
- Tracks dimension correctness separately
- Saves failed puzzles for later retry
- Provides detailed per-puzzle feedback

## Output and Results

### Terminal Output
The solver provides colored, detailed output:

```
🚀 Starting Parallel ARC-AGI Puzzle Solver
📂 Folder: ARC-AGI-2/data/training
🔢 Number of puzzles: 10
🤖 Model: openrouter/sonoma-sky-alpha

📡 Sending parallel requests to OpenRouter API...

🧩 Puzzle 1: 1a2e2828.json
   Status: ✅ CORRECT
   Dimensions: ✅ DIMENSIONS OK
   Expected: 10x10
   Actual:   10x10

🏆 FINAL RESULTS
   Correct Solutions: 7/10 (70.0%)
   Correct Dimensions: 8/10 (80.0%)
   API Failed: 0 | Incorrect: 3 (saved to puzzle_failures.py)
```

### Failure Analysis
Failed puzzles are automatically saved to `puzzle_failures.py` with:
- API failures (network/model errors)
- Incorrect answers (wrong grid output)
- Usage instructions for retrying

### Grid Validation
Use `test.py` to compare predicted vs expected grids:

```python
Predicted = [[0, 0, 0], [1, 1, 1]]  # AI output
expected = [[0, 0, 0], [1, 1, 1]]   # Correct answer

# Run: python test.py
# Output: ✅ All values match! or detailed mismatch report
```

## Configuration Options

### AI Models
Change the model in `solve_arc_puzzle.py`:

```python
# OpenRouter models
MODEL_NAME = "openrouter/sonoma-sky-alpha"  # Default
MODEL_NAME = "openrouter/gpt-4o"           # GPT-4 Optimized
MODEL_NAME = "openrouter/claude-3.5-sonnet" # Claude 3.5

# OpenAI models (change PROVIDER = "openai")
MODEL_NAME = "gpt-4"                       # GPT-4
MODEL_NAME = "gpt-3.5-turbo"               # GPT-3.5 Turbo
```

### Dataset Selection
Choose different datasets:

```python
PUZZLE_FOLDER = "ARC-AGI/data/training"      # Original ARC training
PUZZLE_FOLDER = "ARC-AGI/data/evaluation"    # Original ARC evaluation
PUZZLE_FOLDER = "ARC-AGI-2/data/training"    # Extended training (default)
PUZZLE_FOLDER = "ARC-AGI-2/data/evaluation"  # Extended evaluation
```

## Troubleshooting

### Common Issues

1. **"OPENROUTER_API_KEY environment variable not set"**
   - Set your API key: `export OPENROUTER_API_KEY="your_key"`

2. **"Puzzle file not found"**
   - Check PUZZLE_FOLDER path
   - Verify puzzle files exist

3. **"No JSON files found"**
   - Ensure you're using the correct dataset folder
   - Check file permissions

4. **API Rate Limits**
   - OpenRouter has rate limits; add delays if needed
   - Consider upgrading your plan for higher limits

5. **Dimension Mismatches**
   - AI sometimes outputs wrong grid sizes
   - Check the prompt formatting in `puzzle_helpers.py`

### Performance Tips

- **Start Small**: Begin with `NUM_PUZZLES = 5` to test
- **Monitor API Usage**: Check your OpenRouter dashboard
- **Retry Strategically**: Focus on dimension-correct but logically wrong puzzles
- **Model Selection**: Try different models for different puzzle types

## Architecture Details

### Core Components

- **`solve_arc_puzzle.py`**: Main orchestration and parallel processing
- **`API_client.py`**: Handles all AI model interactions
- **`puzzle_helpers.py`**: Data loading, formatting, and file management
- **`puzzle_failures.py`**: Failure tracking and retry lists

### AI Prompt Strategy

The system uses a comprehensive prompt that includes:
- Clear problem statement
- Multiple training examples
- Explicit dimension requirements
- Format specifications
- Validation checklist
- Emphasis on pattern consistency

### Error Handling

- API failures are caught and logged
- Invalid JSON responses are handled gracefully
- Dimension mismatches are flagged separately from logical errors
- Failed puzzles are automatically categorized for retry

## Contributing

To improve the system:
1. Experiment with different prompt formats
2. Try various AI models and parameters
3. Add more sophisticated validation
4. Implement puzzle difficulty analysis
5. Add visualization tools for grids

## License

This project uses the ARC-AGI dataset. Please refer to the original ARC license and terms of use.

---

**Note**: This system demonstrates AI's current capabilities on abstract reasoning tasks. ARC-AGI remains a challenging benchmark, with even the best AI systems achieving limited success rates.

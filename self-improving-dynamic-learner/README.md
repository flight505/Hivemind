# AI Predictor Generator

An intelligent system that uses Large Language Models (LLMs) to automatically generate, test, and improve Python predictor functions for classification tasks. The system iteratively learns from mistakes and builds increasingly accurate predictors through cross-cycle learning.

## 🎯 What This Does

This system automatically creates Python functions that can predict categorical outcomes (like 1, 2, 3, 4) based on numerical input features (A, B, C, D, E). It uses AI to:

1. **Analyze patterns** in your dataset
2. **Generate predictor functions** using simple mathematical operations
3. **Test accuracy** on your full dataset
4. **Learn from mistakes** to improve future predictions
5. **Iterate cyclically** to achieve higher accuracy over time

## 📁 Project Structure

```
├── predictor_generator.py          # Main predictor generation script
├── predictor_evaluator.py          # Evaluation and testing utilities
├── API_client.py                   # OpenRouter/OpenAI API client
├── predictor_generator_with_hard_examples.py  # Advanced version with hard examples
├── find_unsolved_problems.py       # Diagnostic tool to find consistently unsolved cases
├── complex_dataset.csv             # Your training data (example)
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install pandas openai termcolor matplotlib tqdm
```

### 2. Set API Keys

Set your API keys as environment variables:

```bash
# For OpenRouter (recommended)
export OPENROUTER_API_KEY="your_openrouter_key_here"

# OR for OpenAI
export OPENAI_API_KEY="your_openai_key_here"
```

### 3. Prepare Your Data

Your CSV file should have columns: `A`, `B`, `C`, `D`, `E` (inputs) and `Output` (target categories 1-4).

Example data format:
```csv
A,B,C,D,E,Output
1.2,3.4,2.1,4.5,1.8,2
2.3,1.9,3.7,2.8,4.1,1
...
```

### 4. Run the Generator

```bash
python predictor_generator.py
```

## 🔧 How It Works

### Core Algorithm

The system uses a **cyclic learning approach**:

1. **Sample Data**: Takes a small sample of your data to learn patterns
2. **Generate Function**: Uses AI to create a predictor function based on mathematical relationships
3. **Full Evaluation**: Tests the function on your ENTIRE dataset
4. **Learn from Mistakes**: Analyzes prediction errors and wrong cases
5. **Improve**: Creates better functions using insights from previous attempts
6. **Repeat**: Cycles through this process to achieve higher accuracy

### Key Features

#### 🎨 **Intelligent Pattern Recognition**
- Analyzes mathematical relationships between inputs (A, B, C, D, E)
- Discovers patterns like sums, differences, ratios, and conditional logic
- Uses simple arithmetic operations (no complex ML algorithms)

#### 🔄 **Cross-Cycle Learning**
- Remembers successful patterns from previous cycles
- Learns from common mistake types
- Builds upon the best-performing functions

#### 📊 **Comprehensive Evaluation**
- Tests on 100% of your dataset (not just training samples)
- Tracks accuracy progression over time
- Generates detailed error analysis

#### 🎯 **Adaptive Improvement**
- Detects stagnation and tries creative new approaches
- Focuses on difficult cases that remain unsolved
- Balances exploration with exploitation of known good patterns

## 📋 Configuration Options

### Main Script (`predictor_generator.py`)

```python
# IMPORTANT VARIABLES
PROVIDER = "OPENROUTER"          # "OPENROUTER" or "OPENAI"
CSV_FILE = "complex_dataset.csv" # Your data file
SAMPLE_SIZE = 10                 # Rows to show AI for pattern learning
MODEL_NAME = "openrouter/sonoma-sky-alpha"  # AI model to use

# Cycle Settings
ITERATIONS_PER_CYCLE = 10        # Generations per cycle
TOP_PERFORMERS_TO_KEEP = 3       # Best functions to remember
REFLECTIONS_TO_KEEP = 3          # Strategic insights to retain

# Output Settings
PREDICTORS_FOLDER = "predictors-SKY"  # Where to save functions
PLOT_FILENAME = "accuracy_progress-SKY.png"  # Progress chart
```

### API Client (`API_client.py`)

```python
# API Configuration
MAX_API_RETRIES = 10             # Retry failed requests
API_RETRY_DELAY = 2              # Base delay between retries (seconds)
RATE_LIMIT_DELAY = 0.1           # Delay between API calls
```

### Hard Examples Version (`predictor_generator_with_hard_examples.py`)

Additional features for challenging datasets:

```python
# Hard Examples Configuration
HARD_EXAMPLES_JSON = "unsolved_rows.json"  # Track unsolved cases
MAX_HARD_EXAMPLES_TO_SHOW = 5   # Cases to focus on per generation
```

### Find Unsolved Problems (`find_unsolved_problems.py`)

Configuration for the diagnostic tool:

```python
# Analysis Settings
FOLDER_TO_TEST = "predictors-SKY"  # Folder containing predictor files
CSV_FILE = "complex_dataset.csv"   # Dataset to test against
PRINT_INTERVAL = 10                 # Print progress every N predictors

# Performance Settings
NUM_PROCESSES = 10                  # Number of parallel processes
TEMP_MODULE_NAME = "temp_predictor" # Temporary import name

# Output Settings
OUTPUT_JSON = "unsolved_rows.json"  # Results file
```

## 📊 Output and Results

### Generated Files

The system creates several types of output:

#### 📁 Predictor Functions
```
predictors-SKY/
├── predictor_1.py     # First attempt (e.g., 45.2% accuracy)
├── predictor_2.py     # Improved version (52.1% accuracy)
├── predictor_3.py     # Better version (61.8% accuracy)
└── ...
```

Each predictor file contains:
- The Python function code
- Accuracy achieved
- Generation timestamp
- Performance metrics

#### 📈 Progress Visualization
- `accuracy_progress-SKY.png`: Shows accuracy improvement over time
- Line chart with cycle boundaries
- Current iteration marker

#### 📝 Strategic Reflections
```
predictors-SKY/
├── reflection_cycle_1.txt
├── reflection_cycle_2.txt
└── ...
```

AI-generated insights about:
- Patterns that work well
- Common failure modes
- Strategic directions for improvement

#### 🔍 Diagnostic Files (from find_unsolved_problems.py)
```
unsolved_rows.json                    # Indices of consistently unsolved cases
consistently_failing_rows.csv         # Actual data for unsolved cases
```

Contains:
- Row indices that ALL predictors failed to solve correctly
- Statistics about unsolved percentage
- Export of the actual unsolved data for manual analysis

### Console Output

The system provides detailed logging:

```
🚀 STARTING CYCLE 1
🔄 CYCLE 1 - ITERATION 1/10 (Global: 1)
🤖 Sending request to openrouter/sonoma-sky-alpha...
✅ Received valid function from model
📊 Evaluating predictor accuracy...
🏆 New best in cycle 1: 67.3%
📊 Cycle 1 Summary:
  • Average Accuracy: 62.1%
  • Best Accuracy: 67.3%
  • Hard examples remaining: 23
```

## 🎯 Advanced Features

### Hard Examples Mode

The `predictor_generator_with_hard_examples.py` version adds:

- **Persistent Challenge Tracking**: Remembers cases that remain unsolved
- **Focused Improvement**: Prioritizes fixing the hardest examples
- **Automatic Resolution**: Removes solved cases from the challenge list

Use this when you have:
- Particularly difficult edge cases
- Non-uniform data distributions
- Specific examples you want to ensure are handled correctly

### Find Unsolved Problems Tool

The `find_unsolved_problems.py` script is a **diagnostic tool** that analyzes all your generated predictors to identify the truly challenging cases:

**What it does:**
1. **Tests all predictors** against your full dataset in parallel
2. **Finds consensus failures** - rows that ALL predictors get wrong
3. **Creates unsolved_rows.json** - tracks indices of consistently unsolved cases
4. **Exports unsolved data** to `consistently_failing_rows.csv` for analysis
5. **Reports statistics** - percentage of dataset that remains unsolved

**When to use it:**
- After generating many predictors to identify persistent challenges
- Before using hard examples mode to seed it with the toughest cases
- To understand what patterns your predictors consistently struggle with
- To measure overall system performance on the hardest examples

**Usage:**
```bash
python find_unsolved_problems.py
```

**Output:**
```
🔍 Starting parallel predictor consistency test...
✅ Loaded dataset with 1000 rows
📂 Found 25 predictor files to test
🔄 Using 10 parallel processes
🚀 Running parallel tests...
Testing predictors: 100%|██████████| 25/25 [02:30<00:00, 6.67predictor/s]

🏁 Testing complete! Successfully tested 25 predictors.
🎯 Found 23 rows unsolved by ALL 25 predictors
  • Total dataset rows: 1000
  • Percentage unsolved: 2.3%
💾 Saved unsolved row indices to unsolved_rows.json
💾 Also saved unsolved rows data to consistently_failing_rows.csv
```

### API Flexibility

Supports both major AI providers:
- **OpenRouter**: Access to multiple models, often more cost-effective
- **OpenAI**: Direct access to GPT models with guaranteed availability

### Error Handling

Robust error management:
- **API Failures**: Automatic retries with exponential backoff
- **Syntax Errors**: Detects and reports code issues
- **Execution Errors**: Handles runtime failures gracefully
- **Rate Limiting**: Built-in delays to respect API limits

## 🔧 Usage Examples

### Basic Usage

```bash
# Simple generation
python predictor_generator.py

# With custom data
CSV_FILE="my_data.csv" python predictor_generator.py
```

### Hard Examples Mode

```bash
# Start with hard examples tracking
python predictor_generator_with_hard_examples.py

# The system will create unsolved_rows.json automatically
```

### Find Unsolved Problems

```bash
# Analyze all predictors to find consistently unsolved cases
python find_unsolved_problems.py

# This will create:
# - unsolved_rows.json (indices of unsolved cases)
# - consistently_failing_rows.csv (actual unsolved data)
```

### Custom Configuration

```python
# Modify settings at the top of the script
MODEL_NAME = "openai/gpt-4"
ITERATIONS_PER_CYCLE = 15
SAMPLE_SIZE = 20
```

## 📈 Performance Expectations

### Typical Results
- **Starting Accuracy**: 30-50% (random baseline)
- **After 10 iterations**: 60-75% (learns basic patterns)
- **After 50 iterations**: 80-90% (masters complex relationships)
- **Peak Performance**: 90-95%+ (near-optimal for mathematical approaches)

### Factors Affecting Performance
- **Data Quality**: Clean, consistent data leads to better results
- **Pattern Complexity**: Simple mathematical relationships are easiest to learn
- **Dataset Size**: More data provides better learning opportunities
- **AI Model**: More capable models achieve higher accuracy faster

## 🚨 Troubleshooting

### Common Issues

#### API Connection Problems
```bash
# Check your API key is set
echo $OPENROUTER_API_KEY

# Test API connection
python -c "import openai; print('API key found' if openai.api_key else 'No API key')"
```

#### Low Accuracy
- **Check Data Quality**: Ensure consistent data types and reasonable value ranges
- **Increase Iterations**: Try more cycles (`ITERATIONS_PER_CYCLE = 20`)
- **Use Hard Examples**: Switch to `predictor_generator_with_hard_examples.py`

#### Memory Issues
- **Reduce Sample Size**: `SAMPLE_SIZE = 5`
- **Limit Reflections**: `REFLECTIONS_TO_KEEP = 2`

### Debug Mode

Add debug prints to understand what's happening:

```python
# In predictor_generator.py, add:
print(f"DEBUG: Generated function:\n{generated_function}")
print(f"DEBUG: Evaluation results: {eval_results}")
```

## 🎉 Success Stories

This system has successfully generated predictors for:
- **Classification tasks** with 4-10 categories
- **Mathematical pattern recognition** (sums, ratios, conditionals)
- **Edge case handling** through iterative improvement
- **Complex datasets** with non-linear relationships



---

**Happy predicting!** 🎯 The system will automatically learn and improve, turning your data into accurate prediction functions through intelligent AI-driven exploration. 🚀

# Parallel Tree Search Predictor Generator

A sophisticated system that uses **Parallel Monte Carlo Tree Search (MCTS)** to automatically generate and optimize Python predictor functions through iterative improvement and machine learning model interactions.

## 🎯 What This System Does

This system creates Python functions that can predict categorical outputs (1, 2, 3, 4) based on 5 numerical inputs (A, B, C, D, E). It uses a **tree search algorithm** where each "node" represents a different predictor function, and the system intelligently explores the space of possible functions to find the most accurate one.

## 🚀 Key Features

### 🔄 Intelligent Learning Loop
- **Tree Search**: Explores predictor function space using Monte Carlo Tree Search
- **Parallel Processing**: Simultaneously explores 5 different branches for faster discovery
- **Hybridization**: Every 50 nodes, combines the best performing functions to create hybrids
- **Stagnation Detection**: Detects when accuracy gets stuck and forces creative variation
- **Periodic Reflection**: Every 3 nodes, analyzes progress and adjusts strategy

### 📚 Advanced Learning Techniques
- **Cross-Cycle Learning**: Learns from top performers across different search phases
- **Example-Based Improvement**: Uses specific failure cases to guide future generations
- **Mistake Categorization**: Distinguishes between syntax errors, execution errors, and prediction errors
- **Progressive Feedback**: Provides increasingly detailed feedback as the search progresses

### 🎨 Smart Exploration
- **PUCT Algorithm**: Balances exploration of new paths vs exploitation of known good paths
- **Dynamic Prompting**: Creates context-aware prompts that include best practices and avoid past mistakes
- **Category Balance**: Ensures functions can predict all 4 categories (1, 2, 3, 4) equally well
- **Mathematical Innovation**: Focuses on simple but effective arithmetic relationships

## 🏗️ System Architecture

### Core Components

1. **`predictor_generator_parallel_ts.py`** - Main orchestrator implementing the tree search
2. **`API_client.py`** - Flexible client for OpenRouter/OpenAI API calls
3. **`predictor_evaluator.py`** - Evaluates generated functions against the full dataset

### Data Flow

```
Dataset → Tree Search → API Model → Generated Function → Evaluator → Feedback Loop
```

## 🌳 Understanding the Tree Search

### What is Tree Search?

Imagine you're trying to find the best recipe for chocolate chip cookies. Instead of trying random combinations, you could:

1. Start with a basic recipe (root node)
2. Try slight variations (child nodes)
3. Keep the best variations and build upon them
4. Occasionally combine the best recipes you've found (hybridization)

That's essentially what tree search does here!

### Key Tree Search Parameters

```python
# Total exploration budget
TOTAL_NODES = 1000  # How many different functions to try

# Parallel exploration
PARALLEL_BRANCHES = 5  # Try 5 different approaches simultaneously

# Exploration vs Exploitation balance
C_PUCT = 1.0  # How much to explore vs exploit known good paths

# Branching factor
TREE_CHILDREN_PER_EXPANSION = 4  # Generate 4 variations per node
```

### Tree Search Algorithm (PUCT)

The system uses **Predictive Upper Confidence Bound (PUCT)** to decide which path to explore next:

```
PUCT Score = Q-value + Exploration Bonus
```

- **Q-value**: How good this path has been so far (based on accuracy)
- **Exploration Bonus**: Encourages trying new, unexplored paths

## 🚀 Key Features

### 1. Parallel Processing
- Explores **5 branches simultaneously** instead of one at a time
- Each branch generates and evaluates multiple predictor variations
- Dramatically speeds up the search process

### 2. Hybridization 🔗
Every 50 nodes, the system tries to **combine the best performing functions**:

```python
HYBRIDIZATION_FREQUENCY = 50
```

**How it works:**
1. Identifies the top 2 performing functions in the current tree
2. Creates a prompt asking the AI to combine their strengths
3. Generates a "hybrid" function that learns from both approaches
4. Evaluates the hybrid and adds it to the tree

**Example Hybridization Prompt:**
```
TOP PERFORMER 1 (Accuracy: 87.5%):
def predict_output(A, B, C, D, E):
    return 1 if A + B > C else 2 if A - B < D else 3

TOP PERFORMER 2 (Accuracy: 89.2%):
def predict_output(A, B, C, D, E):
    return 2 if B * C > A + D else 4 if E > A else 1

HYBRID FUNCTION REQUEST:
Create a new predictor that combines the best aspects of both...
```

### 3. Stagnation Detection 🛑
Every 10 nodes, checks if accuracy is stuck at the same level:

```python
STAGNATION_CHECK_FREQUENCY = 10
```

**Detection Logic:**
- If the same accuracy appears 3 times in a row
- Triggers "stagnation feedback" to encourage creative variation
- Forces the system to try radically different approaches

### 4. Periodic Reflection 🧠
Every 3 nodes, the system pauses for strategic analysis:

```python
REFLECTION_FREQUENCY = 3
```

**Reflection Process:**
1. Analyzes current progress and patterns
2. Identifies what's working and what's not
3. Suggests new strategies for remaining exploration
4. Saves reflection to file for later analysis

### 5. Example-Based Learning 📚

The system learns from mistakes using **failure examples** from top performers:

#### Cross-Cycle Learning
- Collects failure examples from the best functions
- Shows these examples to future generations
- Helps new functions avoid common mistakes

#### Within-Cycle Improvement
- When a function makes mistakes, the system:
  1. Shows the specific wrong predictions
  2. Explains what the correct answer should be
  3. Asks for a corrected version

## 📊 How the Evaluation Works

### Predictor Evaluation Process

1. **Load Dataset**: Reads all rows from `complex_dataset.csv`
2. **Import Function**: Dynamically loads the generated predictor
3. **Test Each Row**: Calls `predict_output(A, B, C, D, E)` for every data point
4. **Calculate Accuracy**: Compares predictions vs actual outputs
5. **Collect Mistakes**: Stores all incorrect predictions for learning

### Mistake Categories

The system tracks different types of errors:

1. **Prediction Errors**: Function ran but gave wrong answer
2. **Execution Errors**: Function crashed (syntax/runtime errors)
3. **Syntax Errors**: Code couldn't be parsed

## 🎨 The Improvement Feedback Loop

### Creating Improved Prompts

When a function performs poorly, the system creates detailed feedback:

```python
improved_prompt = create_improved_prompt(
    base_prompt,
    mistakes,           # What went wrong
    node_id,           # Which attempt this is
    eval_results,      # Performance metrics
    failure_examples,  # Examples from top performers
    cycle_number       # Current search phase
)
```

### Feedback Components

1. **Specific Error Details**: Shows exact inputs that failed
2. **Expected vs Actual**: Explains what should happen
3. **Top Performer Examples**: Shows successful patterns
4. **Creative Guidance**: Suggests mathematical approaches
5. **Priority Order**: Fixes syntax first, then execution, then accuracy

## 🔧 Configuration Parameters

### Important Variables (Top of Script)

```python
# API Configuration
PROVIDER = "OPENROUTER"  # or "OPENAI"
MODEL_NAME = "openrouter/sonoma-sky-alpha"

# Dataset
CSV_FILE = "complex_dataset.csv"
SAMPLE_SIZE = 10  # Rows shown to model for training

# Tree Search Parameters
TOTAL_NODES = 1000
PARALLEL_BRANCHES = 5
C_PUCT = 1.0

# Special Features
HYBRIDIZATION_FREQUENCY = 50
STAGNATION_CHECK_FREQUENCY = 10
REFLECTION_FREQUENCY = 3

# Learning Parameters
TOP_PERFORMERS_TO_KEEP = 3
EXAMPLES_PER_PERFORMER = 10
REFLECTIONS_TO_KEEP = 3
```

## 📁 Output Files

### Generated Files

1. **`predictors-SKY-PARALLEL-TS/predictor_*.py`** - Saved predictor functions with accuracy info
2. **`accuracy_progress-SKY-PARALLEL-TS.png`** - Progress visualization
3. **`tree_visualization.html`** - Interactive tree browser
4. **`reflection_node_*.txt`** - Strategic analysis files

### File Organization

```
project/
├── predictor_generator_parallel_ts.py  # Main script
├── API_client.py                       # API communication
├── predictor_evaluator.py              # Function testing
├── complex_dataset.csv                 # Training data
├── predictors-SKY-PARALLEL-TS/         # Generated functions
│   ├── predictor_1.py
│   ├── predictor_34.py (best so far)
│   └── reflection_node_150.txt
├── accuracy_progress-SKY-PARALLEL-TS.png
└── tree_visualization.html
```

## 🚀 Running the System

### Prerequisites

1. **Python Dependencies:**
```bash
pip install pandas openai termcolor matplotlib
```

2. **API Keys:**
```bash
# For OpenRouter
export OPENROUTER_API_KEY="your_key_here"

# For OpenAI
export OPENAI_API_KEY="your_key_here"
```

### Execution

```bash
python predictor_generator_parallel_ts.py
```

### What Happens During Execution

1. **Initialization**: Loads dataset, sets up tree structure
2. **Parallel Exploration**: Processes 5 branches simultaneously
3. **API Calls**: Each branch makes requests to generate functions
4. **Evaluation**: Tests each generated function
5. **Learning**: Incorporates mistakes into next iteration
6. **Special Events**: Hybridization, reflection, stagnation checks
7. **Visualization**: Updates progress charts and tree browser

## 📈 Understanding the Progress

### Accuracy Plot
- **X-axis**: Node number (attempt number)
- **Y-axis**: Prediction accuracy percentage
- **Lines**: Shows improvement over time
- **Vertical Lines**: Mark cycle boundaries

### Tree Visualization
- **🟢**: ≥90% accuracy (excellent)
- **🟡**: ≥70% accuracy (good)
- **🟠**: >0% accuracy (needs improvement)
- **⚪**: 0% accuracy (failed)
- **🔍**: Currently exploring this path

## 🎯 Success Metrics

The system aims to achieve:
- **≥95% accuracy** on the full dataset
- **Balance across all 4 categories** (1, 2, 3, 4)
- **Robust error handling** (no crashes)
- **Simple, interpretable logic**

## 🔄 The Learning Cycle

1. **Generate**: Create new predictor function
2. **Test**: Evaluate on full dataset
3. **Analyze**: Identify mistakes and patterns
4. **Learn**: Incorporate feedback into next generation
5. **Adapt**: Use hybridization and reflection for strategy shifts
6. **Repeat**: Continue until target accuracy reached

## 🧪 Example Generated Function

```python
def predict_output(A, B, C, D, E):
    """
    Generated by Parallel Tree Search
    Accuracy: 94.2%
    """
    # Simple but effective mathematical relationships
    if A + B > C and D < E:
        return 1
    elif B * 2 > A + C:
        return 2
    elif C - A > D + E:
        return 3
    else:
        return 4
```

This system demonstrates how **machine learning can be used to generate human-interpretable code** through intelligent exploration and iterative improvement!

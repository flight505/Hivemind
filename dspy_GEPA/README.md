# DSPy-GEPA: Evolutionary Prompt Optimization

This repository demonstrates **DSPy** with **GEPA** (Generative Evolutionary Prompt Optimization) for automatically evolving and optimizing AI prompts through reflection and evolutionary algorithms.

## 🎯 What This Does

GEPA uses **reflection** (GPT-5 analyzing failures) and **evolutionary optimization** to automatically improve prompts from basic instructions to expert-level prompts. Instead of manual prompt engineering, GEPA learns from examples and evolves better prompts iteratively.

## 📁 Project Structure

```
├── dspy_openrouter_unoptimized.py    # Baseline math solver (no optimization)
├── dspy_openrouter_with_GEPA.py      # Math problem solver with GEPA optimization
├── travel_itinerary_planner.py       # Travel planning with GEPA optimization
├── optimized_prompt.txt             # Evolved math solver prompt
├── optimized_travel_prompt.txt      # Evolved travel planner prompt
├── train_set.json                   # Math training data
├── travel_train_set.json            # Travel training data
└── README.md                        # This file
```

## 🚀 Quick Start

### Prerequisites
```bash
pip install dspy-ai gepa  # GEPA requires separate installation
```

### Environment Variables
```bash
export OPENROUTER_API_KEY="your-openrouter-api-key-here"
```

### Run Math Problem Solver
```bash
python dspy_openrouter_with_GEPA.py
```

### Run Travel Itinerary Planner
```bash
python travel_itinerary_planner.py
```

## 🔧 How GEPA Works

### Core Algorithm

1. **Initialization**: Start with basic prompt
2. **Evaluation**: Test current prompt on examples
3. **Reflection**: Use GPT-5 to analyze failures and generate feedback
4. **Evolution**: Generate new prompt variations based on feedback
5. **Selection**: Use Pareto optimization to select best prompts
6. **Iteration**: Repeat until convergence or budget exhausted

### Key Innovation: Reflection-Based Evolution

Unlike traditional prompt optimization, GEPA uses **reflection** to understand WHY prompts fail:

```
Bad Prompt: "Solve this math problem."
↓
Reflection: "The model didn't show intermediate steps..."
↓
New Prompt: "Solve step-by-step, showing all work clearly..."
```

## 📊 Example Results

### Math Problem Solver
**Before GEPA:**
```
"Solve the problem and provide the answer in the correct format."
```

**After GEPA:**
```
Evolved prompt with detailed mathematical reasoning instructions,
format requirements, and error-checking protocols...
```

### Travel Itinerary Planner
**Before GEPA:**
```
"Create a detailed day-by-day travel itinerary with budget breakdown."
```

**After GEPA:**
```
Sophisticated prompt understanding travel styles, budget allocation,
cultural considerations, and optimal activity sequencing...
```

## 🛠️ Important Parameters Explained

### Budget Control

```python
optimizer = GEPA(
    # Option 1: Auto presets (recommended)
    auto="light",      # ~400 calls, 6 candidates - quick experimentation
    auto="medium",     # ~800 calls, 12 candidates - balanced
    auto="heavy",      # ~1200 calls, 18 candidates - thorough

    # Option 2: Direct control
    max_metric_calls=1000,     # Exact total budget
    max_full_evals=50,         # Number of complete evaluations

    # Option 3: Evaluation-based
    max_full_evals=25,         # 25 complete dataset evaluations
)
```

### Dataset Configuration

```python
# Exploration vs Evaluation Trade-off
train_set = train_set[:4]  # More training = more learning opportunities
val_set = val_set[:1]      # Smaller validation = more exploration budget

# Large validation = conservative, general solutions
# Small validation = diverse, specialized solutions
```

### Reflection Settings

```python
reflection_lm=dspy.LM(
    model="openai/x-ai/grok-4-fast:free",  # Strong model for reflection
    temperature=1.0,                      # High creativity for new ideas
    max_tokens=32000,                     # Allow detailed analysis
    api_key=os.getenv("OPENROUTER_API_KEY"),
    api_base="https://openrouter.ai/api/v1"
)

reflection_minibatch_size=3,  # Examples to analyze per reflection
```

### Evaluation Settings

```python
num_threads=32,        # Parallel evaluation (limited by dataset size)
failure_score=0.0,     # Score for failed examples
perfect_score=1.0,     # Maximum possible score
```

## 🔧 Error Fixes Applied

### 1. DSPy Evaluate Bug Fix

**Problem:** `UnboundLocalError: cannot access local variable 'results'`

**Root Cause:** DSPy's `evaluate.py` was missing the line `results = executor.execute(process_item, devset)`

**Fix Applied:**
```python
# In evaluate.py around line 162, added:
results = executor.execute(process_item, devset)
```

**Impact:** Enables proper parallel evaluation of programs during optimization.

### 2. Import Order Fix

**Problem:** `from dspy import GEPA` was placed after GEPA instantiation

**Fix:** Moved import to top of file with other imports.

### 3. Metric Function Robustness

**Problem:** Integer parsing could fail on malformed LLM responses

**Fix:** Added comprehensive error handling in metric functions:
```python
try:
    llm_answer = int(prediction.answer)
except ValueError as e:
    # Return detailed feedback about format requirements
    return dspy.Prediction(score=0, feedback=format_feedback)
```

## 📈 Understanding GEPA Logs

### Budget Messages
```
Running GEPA for approx 400 metric calls of the program.
This amounts to 40.00 full evals on the train+val set.
```
- Total optimization budget and evaluation breakdown

### Optimization Progress
```
Average Metric: 2.0 / 2 (100.0%)
```
- Current best program performance on validation set

### Convergence Signals
```
All subsample scores perfect. Skipping.
Reflective mutation did not propose a new candidate
```
- Optimization has found optimal solution, no further improvements needed

### Pareto Optimization
```
Using 15 examples for tracking Pareto scores.
You can consider using a smaller sample of the valset to allow GEPA to explore more diverse solutions within the same budget.
```
- Large validation sets → Conservative, general solutions
- Small validation sets → Diverse, specialized solutions

## 🎯 Use Cases & Applications

### When to Use GEPA

✅ **Complex reasoning tasks** (math, coding, analysis)
✅ **Structured output requirements** (itineraries, reports, plans)
✅ **Domain-specific expertise** (travel, legal, medical)
✅ **Quality-sensitive applications** (education, professional services)

### GEPA Advantages

- **Automatic optimization** - No manual prompt engineering
- **Reflection-based** - Learns WHY prompts fail, not just that they fail
- **Multi-objective** - Optimizes across entire validation sets
- **Resume capability** - Can continue optimization with `log_dir`

## 🔍 Deep Dive: Metric Functions

Metrics provide **both scoring AND feedback** for GEPA's reflection:

### Math Problem Metric
```python
def metric_with_feedback(example, prediction, trace=None, pred_name=None, pred_trace=None):
    # 1. Parse answer with error handling
    # 2. Calculate correctness score
    # 3. Generate detailed feedback for reflection
    # 4. Include solution context for learning
```

### Travel Planning Metric
```python
def metric_with_feedback(example, prediction, trace=None, pred_name=None, pred_trace=None):
    # 1. Check itinerary structure (day-by-day breakdown)
    # 2. Verify budget inclusion
    # 3. Ensure destination focus
    # 4. Provide specific improvement guidance
```

## 🚀 Advanced Configuration

### Custom Budget Calculation
```python
# GEPA automatically calculates budget based on:
# - Number of predictors in your program
# - Number of candidates to try
# - Validation set size
# - Minibatch size for reflection
```

### Checkpointing & Resumption
```python
optimizer = GEPA(
    log_dir="./gepa_checkpoints",  # Save progress
    # Can resume interrupted runs
    ...
)
```

### Multi-Objective Tracking
```python
# GEPA tracks Pareto frontiers across:
# - Accuracy on different example types
# - Output quality metrics
# - Computational efficiency
# - Format compliance
```

## 📊 Performance Monitoring

### Track Statistics
```python
optimizer = GEPA(
    track_stats=True,  # Enable detailed result tracking
    ...
)

# Access optimization history
optimized_program.detailed_results.candidates          # All tried prompts
optimized_program.detailed_results.val_aggregate_scores # Performance scores
optimized_program.detailed_results.discovery_eval_counts # When each was found
```

## 🎓 Learning Resources

- **DSPy Documentation**: https://dspy.ai
- **GEPA Paper**: [GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning](https://arxiv.org/abs/2507.19457)
- **OpenRouter**: https://openrouter.ai (for model access)

## 🤝 Contributing

Found bugs or improvements? The DSPy ecosystem is actively developed. Check the repositories for contribution guidelines.

---

**Happy optimizing!** 🎯 GEPA can transform basic prompts into expert-level instructions automatically.

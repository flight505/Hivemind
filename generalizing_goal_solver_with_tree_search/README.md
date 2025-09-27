# Goal Solver: Advanced Parallel Tree Search with 2-Stage Evaluation

A cutting-edge AI-powered system that uses parallel Monte Carlo Tree Search with PUCT scoring and a sophisticated **2-stage evaluation system** to generate, rigorously evaluate, and iteratively improve solutions to complex goals using large language models.

## 🎯 Overview

This system implements an advanced parallel MCTS approach enhanced with PUCT scoring and a ** 2-stage evaluation pipeline**. It generates solution candidates through parallel exploration, evaluates them using extremely strict AI-driven rubrics  and uses multiple iterative improvement techniques to achieve exceptional quality.

**Key Innovation**: Only solutions passing Stage 1 evaluation (≥60/70 points) proceed to Stage 2 and get saved, ensuring only high-quality solutions are retained.

## 🚀 Key Features

- **Parallel Tree Search**: Processes multiple solution branches simultaneously for efficient exploration
- **2-Stage Evaluation System**: Rigorous filtering with Stage 1 (70pts/7 rubrics) + Stage 2 (configurable increments)
- **Ultra-Efficient API Usage**: Only 2 API calls total for generating all evaluation rubrics
- **Harsh AI Evaluation**: Extremely strict rubrics with merciless LLM-based assessment
- **Real-Time Visualization**: Generates live progress plots showing quality scores, distributions, and metrics
- **Smart Filtering**: Only saves solutions that pass Stage 1 (≥60 points), dramatically improving quality
- **Iterative Improvement**: Cross-cycle learning, stagnation detection, hybridization, and creative prompting
- **Thread-Safe Operations**: Supports concurrent processing with proper synchronization
- **Comprehensive Logging**: Colored terminal output with detailed progress tracking
- **Automatic Documentation**: Saves all solutions, evaluations, and reflections to organized files

## 🔧 How It Works

### 1. **Initialization Phase**
- **Generates evaluation rubrics with only 2 API calls**: Stage 1 (7 rubrics in 1 call) + Stage 2 (N rubrics in 1 call)
- Sets up the tree search infrastructure with configurable parameters
- Initializes conversation histories and quality tracking

### 2. **Parallel Tree Search Algorithm**
The system uses an advanced MCTS approach with these key components:

#### **Selection Phase**
- Selects promising nodes using PUCT scoring
- Balances exploitation (high-quality solutions) vs exploration (untried paths)
- Ensures unique exploration paths across parallel branches

#### **Expansion Phase**
- Generates new solution candidates from selected nodes
- Creates variations to explore different approaches
- Applies stagnation feedback and hybridization when appropriate

#### **2-Stage Evaluation Phase**
- **Stage 1**: Evaluates with 7 parallel rubrics (70 points total)
  - Each solution must score ≥60 points to pass Stage 1
  - Failed solutions are discarded and not saved
- **Stage 2**: Only successful Stage 1 solutions evaluated with complementary rubrics (30 points total)
  - Uses configurable increments (e.g., STAGE_2_INCREMENTS=1 → 30×1pt rubrics)
  - Provides fresh evaluation perspectives
- **Final Score**: Sum of Stage 1 + Stage 2 scores (0-100 scale)

#### **Backpropagation Phase**
- Updates tree statistics with evaluation results
- Propagates quality scores up through the tree
- Updates best solution tracking
- **Only Stage 1-passing solutions contribute to tree learning**

### 3. **Advanced Features**

#### **Stagnation Detection**
- Monitors quality scores for repetitive patterns
- Triggers creative variation prompts when stuck
- Prevents convergence on suboptimal solutions

#### **Hybridization**
- Periodically combines elements from top-performing solutions
- Creates new hybrid approaches that leverage multiple successful strategies
- Occurs every `HYBRIDIZATION_FREQUENCY` nodes

#### **Cross-Cycle Learning**
- Collects success examples from previous cycles
- Provides learning context for future generations
- Enables cumulative improvement over iterations

#### **Periodic Reflection**
- Generates strategic insights about progress patterns
- Identifies emerging successful approaches
- Saves reflection documents for analysis

## ⚙️ Configuration

All important variables are defined as ALL_CAPS constants at the top of the script:

### **Goal Definition**
```python
GOAL = "list of 5 totally unique and useful suggestions for a new simple saas using LLMs"
```

### **API Configuration**
```python
PROVIDER = "OPENROUTER"                    # API provider
MODEL_NAME = "openrouter/sonoma-sky-alpha" # Model identifier
MAX_API_RETRIES = 10                       # Retry attempts for failed calls
API_RETRY_DELAY = 2                        # Delay between retries (seconds)
RATE_LIMIT_DELAY = 0.1                      # Rate limiting delay
```

### **Tree Search Configuration**
```python
TOTAL_NODES = 100                           # Total exploration budget
PARALLEL_BRANCHES = 5                       # Concurrent branches per iteration
TREE_CHILDREN_PER_EXPANSION = 4             # Variations per expansion
C_PUCT = 1.0                                # Exploration vs exploitation balance
HYBRIDIZATION_FREQUENCY = 20                # Nodes between hybridizations
STAGNATION_CHECK_FREQUENCY = 10             # Nodes between stagnation checks
REFLECTION_FREQUENCY = 5                    # Nodes between reflections
```

### **Quality Configuration**
```python
TARGET_QUALITY_THRESHOLD = 90.0             # Stop when solution reaches this score
MINIMUM_QUALITY_THRESHOLD = 0.0             # Minimum score to consider evaluated
MAXIMUM_QUALITY_SCORE = 100.0               # Maximum possible score
TOP_PERFORMERS_TO_KEEP = 3                  # Top solutions for cross-learning
EXAMPLES_PER_PERFORMER = 5                  # Examples stored per top performer
REFLECTIONS_TO_KEEP = 3                     # Recent reflections to maintain
```

### **2-Stage Evaluation Configuration**
```python
# Stage 1: 7 rubrics × 10 points each = 70 total points
STAGE_1_SETTINGS = {
    "TOTAL_POINTS": 70,                      # Total points for Stage 1
    "CHUNKS": 7,                            # Number of rubrics for Stage 1
    "MINIMUM_SCORE_TO_PASS_STAGE_1": 60     # Must score ≥60 to pass Stage 1
}

# Stage 2: Configurable increments for remaining 30 points
STAGE_2_INCREMENTS = 1                      # Point allocation per rubric (1 = 30×1pt rubrics)
```

### **Plotting Configuration**
```python
PLOT_FILE = f"{SOLUTIONS_FOLDER}/progress_plot.png"   # Real-time progress plot file
ENABLE_PLOTTING = True                      # Set to False to disable plotting
```

## 📊 Output Structure

The system creates a `solutions/` folder with organized outputs:

```
solutions/
├── best_solution.txt              # Final best solution with full details
├── solution_0_85.5.txt            # Individual solution files (with quality scores)
├── solution_1_72.3.txt
├── ...
├── progress_plot.png             # Real-time progress visualization
├── reflections/                   # Strategic insights and progress analysis
│   ├── reflection_node_5.txt
│   ├── reflection_node_10.txt
│   └── ...
└── rubrics/                      # Evaluation rubrics and criteria
    ├── stage1_rubrics.txt        # Stage 1 evaluation rubrics (7 rubrics, 70pts total)
    └── stage2_rubrics.txt        # Stage 2 evaluation rubrics (30pts total)
```

### **Solution File Format**
Each solution file contains:
- Generation timestamp and goal
- Quality score and detailed feedback
- Complete solution content
- Evaluation breakdown (dimensions, strengths, improvements)

## 🚀 Usage

### **Prerequisites**
- Python 3.7+
- Required packages (install via `pip install -r requirements.txt`):
  - `termcolor` - Colored terminal output
  - API client dependencies (via `API_client.py`)

### **Quick Start**
1. **Configure your goal** at the top of the script
2. **Adjust parameters** as needed for your use case
3. **Run the script**:
   ```bash
   python goal_solver_parallel_ts.py
   ```

### **Customization Examples**

#### **For Complex Goals (Increase exploration)**
```python
TOTAL_NODES = 200
PARALLEL_BRANCHES = 8
TREE_CHILDREN_PER_EXPANSION = 6
TARGET_QUALITY_THRESHOLD = 95.0
```

#### **For Speed (Reduce computation)**
```python
TOTAL_NODES = 50
PARALLEL_BRANCHES = 3
TREE_CHILDREN_PER_EXPANSION = 2
REFLECTION_FREQUENCY = 10  # Less frequent reflections
```

#### **For Creative Tasks (Increase variation)**
```python
HYBRIDIZATION_FREQUENCY = 10  # More frequent hybridization
STAGNATION_CHECK_FREQUENCY = 5  # More responsive to stagnation
```

## 🔍 Technical Details

### **PUCT Scoring Algorithm**
The system uses a modified PUCT formula for node selection:

```
score = Q_value + exploration_term
Q_value = 0.7 * (node_value / max_visits) / 100 + 0.3 * rank_score
exploration = c_puct * sqrt(log(total_visits) / (node_visits + 1))
```

Where:
- `Q_value`: Quality estimate (70% raw score + 30% relative ranking)
- `exploration_term`: Encourages exploration of less-visited nodes
- `c_puct`: Controls exploration vs exploitation balance

### **Thread Safety**
- Uses `threading.RLock()` for conversation history access
- Atomic operations for global counters
- Node-specific locks for tree modifications

### **2-Stage Evaluation System**
The system uses a sophisticated 2-stage evaluation pipeline:

**Stage 1 (70 points)**: 7 parallel rubrics generated in 1 API call
- Each rubric evaluates a specific aspect with extremely strict standards
- Solutions must score ≥60 points to pass Stage 1
- Failed solutions are discarded and not saved

**Stage 2 (30 points)**: Configurable number of complementary rubrics in 1 API call
- STAGE_2_INCREMENTS determines rubric size (e.g., 1 = 30×1pt rubrics, 2 = 15×2pt rubrics)
- Evaluates from different perspectives than Stage 1
- Only applied to Stage 1-passing solutions

**API Efficiency**: Only 2 API calls total for all rubric generation (vs. 30+ individual calls previously)

### **Harsh Evaluation Standards**
The system uses extremely strict evaluation criteria:
- Most solutions score 40-65 points total
- 80+ scores are rare and represent truly exceptional quality
- 90+ scores are extremely rare and indicate groundbreaking solutions
- Generic or obvious solutions automatically score below 60

### **Memory Management**
- Limits stored reflections to prevent unbounded growth
- Maintains only recent top performers for cross-learning
- Efficient tree pruning of low-quality branches

## 🎨 Advanced Features Explained

### **Stagnation Detection**
Detects when the same quality score appears 3+ times consecutively and triggers:
- Creative variation prompts
- Encouragement to explore alternative approaches
- Pattern-breaking instructions

### **Hybridization Process**
Every N nodes, the system:
1. Identifies top 2 performing solutions
2. Creates prompts that combine their successful elements
3. Generates new hybrid solutions that leverage multiple approaches

### **Cross-Cycle Learning**
Builds knowledge progressively:
- Collects success patterns from previous cycles
- Provides context about what worked before
- Enables cumulative improvement strategies

### **Quality-Guided Search**
- Prioritizes exploration of high-potential branches
- Uses quality scores to guide tree expansion
- Automatically stops when target quality is achieved

## 📈 Performance Optimization

### **Scalability Considerations**
- **Memory**: Tree size grows with `TOTAL_NODES` - monitor for large explorations
- **API Costs**: Each node requires multiple API calls (generation + evaluation + variations)
- **Time**: Parallel processing reduces wall-clock time but increases peak resource usage

### **Parameter Tuning Guidelines**
- **High-complexity goals**: Increase `TOTAL_NODES` and `PARALLEL_BRANCHES`
- **Creative tasks**: Lower `C_PUCT` to encourage more exploration
- **Convergent tasks**: Increase `TARGET_QUALITY_THRESHOLD`
- **API-limited**: Reduce `TREE_CHILDREN_PER_EXPANSION` and `PARALLEL_BRANCHES`

## 🐛 Troubleshooting

### **Common Issues**
1. **API Failures**: Check `API_client.py` configuration and network connectivity
2. **Too Few Solutions Saved**: Stage 1 is too strict - reduce `STAGE_1_SETTINGS["MINIMUM_SCORE_TO_PASS_STAGE_1"]`
3. **Too Many Low Scores**: Evaluation is working as intended - the system uses harsh standards to ensure quality
4. **Stagnation**: Reduce `STAGNATION_CHECK_FREQUENCY` or adjust creative prompts
5. **Memory Issues**: Reduce `TOTAL_NODES` or implement tree pruning

### **Debugging Tips**
- Monitor the colored terminal output for progress and errors - look for "✅ PASSED STAGE 1" vs "❌ FAILED STAGE 1"
- Check `solutions/rubrics/stage1_rubrics.txt` and `solutions/rubrics/stage2_rubrics.txt` for evaluation criteria
- Review individual solution files for detailed 2-stage feedback with scores
- Examine reflection files for strategic insights about the search process
- If no solutions are being saved, the Stage 1 threshold may be too high for your goal complexity

## 🤝 Contributing

To extend this system:
- Modify the evaluation rubric generation for domain-specific tasks
- Add new stagnation detection patterns
- Implement different tree search algorithms
- Add support for multi-modal evaluation (images, code execution, etc.)

## 📄 License

This project is provided as-is for educational and research purposes. Please cite appropriately if used in academic work.

---

**Happy goal solving with 2-stage evaluation!** 🎯✨

This advanced system uses cutting-edge parallel tree search with a revolutionary 2-stage evaluation pipeline to ensure only the highest-quality solutions are retained. With ultra-efficient API usage (only 2 calls for rubric generation) and merciless quality standards, you'll get exceptional results that truly meet your goals.

**Key Benefits:**
- **Quality Assurance**: Only Stage 1-passing solutions (≥60/70 points) get saved
- **API Efficiency**: 90%+ reduction in rubric generation API calls
- **Comprehensive Evaluation**: Multi-dimensional assessment from multiple perspectives
- **Real-Time Insights**: Live plotting and detailed logging throughout the process

**Pro Tip**: Start with `STAGE_1_SETTINGS["MINIMUM_SCORE_TO_PASS_STAGE_1"] = 50` for easier initial testing, then increase to 60+ for production-quality results.

The system will rigorously evaluate thousands of potential solutions, ensuring only the most exceptional ones make it through both evaluation stages! 🚀💎

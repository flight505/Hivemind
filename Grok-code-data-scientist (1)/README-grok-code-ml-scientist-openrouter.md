# Grok Code ML Scientist (OpenRouter)

An advanced ML scientist script that uses Grok via OpenRouter to generate, test, and iteratively improve machine learning solutions.

## Overview

This script leverages Grok's coding capabilities through OpenRouter to automatically:
- Generate complete, runnable Python ML scripts
- Execute them with timeout protection
- Automatically fix errors and optimize for performance
- Iteratively improve solutions based on previous results
- Save all outputs with detailed progress tracking

## Features

- **Iterative Improvement**: Runs 25 iterations, learning from previous attempts
- **Error Handling**: Automatically detects and fixes code errors
- **Performance Optimization**: Optimizes slow solutions for better runtime
- **Leakage Prevention**: Ensures proper cross-validation practices
- **GPU Support**: Detects and utilizes GPU acceleration when available
- **Comprehensive Logging**: Saves all execution outputs and progress reports

## Prerequisites

- Python 3.7+
- OpenRouter account and API key
- Required data files: `train.csv`, `test.csv`, `sample_submission.csv`, `additional_info.txt`

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install openai pandas termcolor
   ```

2. **Set up OpenRouter API key:**
   ```bash
   export OPENROUTER_API_KEY="your-openrouter-api-key-here"
   ```

## Usage

1. **Prepare your data:**
   - Place `train.csv` and `test.csv` in the same directory as the script
   - Ensure `sample_submission.csv` is present for the correct submission format
   - Add any additional challenge information to `additional_info.txt`

2. **Run the script:**
   ```bash
   python grok-code-ml-scientist-openrouter.py
   ```

## Configuration

The script includes several configurable constants at the top:

```python
ITERATIONS = 25              # Number of improvement iterations
ERROR_HISTORY_SIZE = 3       # Keep track of last 3 errors
SOLUTION_HISTORY_SIZE = 3    # Keep track of last 3 solutions
MAX_RUNTIME_MINUTES = 30     # Maximum runtime per iteration
IMPROVEMENT_EFFORT = "high"  # Reasoning effort level
```

## Output Structure

All outputs are saved to `runs/grok_ml_scientist/YYYYMMDD-HHMMSS/`:

```
runs/grok_ml_scientist/
└── 20231201-143022/           # Timestamped run directory
    ├── solution.py            # Current best solution
    ├── progress_report.json   # Performance metrics and metadata
    ├── submission.csv         # Competition submission file
    ├── execution_outputs.txt  # All execution logs
    └── older_solutions/       # Previous iterations
        ├── solution_1.py
        ├── progress_report_1.json
        ├── submission_1.csv
        └── ...
```

## Progress Report Format

Each `progress_report.json` contains:

```json
{
  "best_model": "LightGBM",
  "cv_scores": [0.85, 0.83, 0.86, 0.84, 0.85],
  "mean_cv": 0.846,
  "std_cv": 0.011,
  "validation_scheme": "5-fold StratifiedKFold",
  "features_used": 25,
  "feature_importances": {
    "feature1": 0.15,
    "feature2": 0.12,
    ...
  },
  "training_time_seconds": 180.5,
  "oof_score": 0.844,
  "notes": "Used GPU acceleration, early stopping at 150 rounds"
}
```

## How It Works

1. **Initialization**: Sets up OpenRouter client and creates timestamped run directory
2. **Data Loading**: Reads sample data and challenge information
3. **Iterative Generation**:
   - Generates ML solution using Grok
   - Executes with timeout protection
   - Handles errors by requesting fixes from Grok
   - Optimizes slow solutions for better performance
   - Learns from previous iterations
4. **Output**: Saves best solution, progress report, and submission file

## Model Capabilities

The script leverages Grok's understanding of:
- Machine learning best practices
- Python programming
- Data preprocessing and feature engineering
- Model selection and hyperparameter tuning
- Cross-validation techniques
- GPU acceleration
- Memory optimization

## Error Handling

- **Timeout Protection**: Automatically kills processes exceeding time limits
- **Error Detection**: Identifies actual errors vs warnings
- **Automatic Fixes**: Requests corrected code from Grok when errors occur
- **Performance Optimization**: Requests optimized code when runtime is too slow

## Safety Features

- **Leakage Prevention**: Ensures proper data splitting and transformation fitting
- **Resource Limits**: Respects memory and time constraints
- **Graceful Degradation**: Falls back to CPU if GPU unavailable

## Monitoring Progress

The script provides colored terminal output:
- 🔵 Cyan: Phase updates
- 🟡 Yellow: Iteration progress and optimization attempts
- 🔴 Red: Errors and timeouts
- 🟢 Green: Successful operations and file saves

## Tips for Best Results

1. **Data Quality**: Ensure your `additional_info.txt` clearly describes the problem
2. **API Key**: Use a stable OpenRouter connection
3. **System Resources**: Ensure adequate RAM (30GB+) and VRAM (8GB+) for complex models
4. **Time Budget**: First runs may take several hours due to 25 iterations
5. **Interrupt Handling**: You can safely interrupt and restart - progress is saved

## Troubleshooting

**"OpenRouter API key not found"**
- Ensure `OPENROUTER_API_KEY` environment variable is set
- Check your OpenRouter account has sufficient credits

**"Execution timed out"**
- Increase `MAX_RUNTIME_MINUTES` for complex problems
- The script will automatically attempt optimization

**"No properly formatted code blocks"**
- This indicates Grok's response format issue
- The script will retry on the next iteration

## License

This script is provided as-is for educational and research purposes.

# Spaceship Titanic AI Prediction Engines

This repository contains four different AI-powered prediction engines for the Spaceship Titanic dataset. Each script uses different approaches to predict passenger transportation outcomes using various AI models through the OpenRouter API.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Common Configuration](#common-configuration)
- [Script 1: BULK Prediction Engine](#script-1-bulk-prediction-engine)
- [Script 2: Progressive BATCH Prediction Engine](#script-2-progressive-batch-prediction-engine)
- [Script 3: Progressive BATCH Alternative](#script-3-progressive-batch-alternative)
- [Script 4: Progressive SINGLE Prediction Engine](#script-4-progressive-single-prediction-engine)
- [Comparison of Approaches](#comparison-of-approaches)
- [Output Files](#output-files)
- [Usage Instructions](#usage-instructions)

## Overview

All scripts analyze the Spaceship Titanic dataset to predict whether passengers were transported to another dimension. They use AI models to:

1. **Analyze patterns** in the training data
2. **Generate predictive rules** and metrics
3. **Make predictions** on unseen data
4. **Calculate accuracy** against actual outcomes
5. **Adapt and improve** predictions over time (progressive scripts)

## Prerequisites

- Python 3.7+
- Required packages: `openai`, `pandas`, `termcolor`, `matplotlib`, `numpy`
- OpenRouter API key (set as environment variable `OPENROUTER_API_KEY`)
- Spaceship Titanic dataset (`train.csv`)

## Common Configuration

All scripts share these configuration variables:

```python
# API Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # Required
MODEL_NAME = "x-ai/grok-4"  # or other OpenRouter models
REASONING_EFFORT = "high"  # For OpenRouter models

# Data Configuration
CSV_FILE_PATH = "train.csv"  # Dataset location
FIRST_ROWS_TO_ANALYZE = 500  # Rows used for initial analysis
```

## Script 1: BULK Prediction Engine

**File:** `ai_prediction_engine_BULK.py`

### Overview
This script performs a one-time bulk analysis and prediction on the dataset. It analyzes the first N rows to understand patterns, then predicts the next M rows in a single batch.

### How It Works

1. **Data Loading & Preparation**
   - Loads the complete dataset from `train.csv`
   - Splits data into analysis rows (first 500) and prediction rows (next 50)
   - Removes the `Transported` column from prediction data

2. **Pattern Analysis**
   - Sends first 500 rows to the AI model
   - Requests detailed analysis of transportation patterns
   - Identifies correlations between features and transport outcomes

3. **Bulk Prediction**
   - Uses the analysis to predict transport status for rows 501-550
   - Requests predictions in JSON format with passenger IDs
   - Parses and validates the prediction results

4. **Accuracy Calculation**
   - Compares predictions against actual values from the dataset
   - Calculates overall accuracy percentage
   - Generates detailed accuracy report

5. **Reporting**
   - Saves accuracy report as JSON file with timestamp
   - Displays colored console output with progress indicators

### Key Features
- **Single-shot analysis**: One comprehensive analysis, then bulk prediction
- **Detailed reporting**: Complete accuracy breakdown and JSON export
- **Colored output**: User-friendly terminal display with status indicators
- **Error handling**: Graceful handling of API failures and data issues

### Output Files
- `accuracy_report_[model]_[timestamp].json`: Detailed accuracy metrics

---

## Script 2: Progressive BATCH Prediction Engine

**File:** `ai_prediction_engine_progressive_BATCH.py`

### Overview
This script implements an adaptive learning system that processes predictions in batches and continuously improves its predictive metrics based on errors.

### How It Works

1. **Initial Setup**
   - Analyzes first 10 rows to generate initial predictive metrics
   - Creates a dedicated output folder for the experiment
   - Sets up rolling accuracy tracking (20 predictions window)

2. **Iterative Batch Processing**
   - Processes predictions in configurable batch sizes (default: 1 row per batch)
   - For each batch:
     - Makes predictions using current metrics
     - Validates against actual outcomes
     - Tracks errors within the batch

3. **Adaptive Learning**
   - **Error Detection**: Identifies incorrect predictions within each batch
   - **Metrics Adjustment**: When errors occur, sends error details to AI for metrics refinement
   - **Comprehensive Learning**: Uses all batch errors for context when adjusting metrics
   - **Metrics Persistence**: Saves each iteration of metrics to timestamped files

4. **Accuracy Tracking**
   - **Cumulative Accuracy**: Overall accuracy across all predictions
   - **Rolling Accuracy**: Accuracy of last 20 predictions
   - **Real-time Plotting**: Updates accuracy progress chart after each batch

5. **Advanced Features**
   - **Unified API Interface**: Supports both OpenAI and OpenRouter
   - **Batch Error Context**: Considers all errors in a batch for learning
   - **Visual Progress**: Matplotlib charts showing accuracy trends

### Key Features
- **Batch processing**: Configurable batch sizes for predictions
- **Adaptive metrics**: Continuous improvement based on prediction errors
- **Comprehensive error analysis**: Uses multiple errors for learning context
- **Dual accuracy tracking**: Both cumulative and rolling accuracy metrics
- **Visual analytics**: Real-time plotting of prediction performance

### Output Files
- `prediction_metrics_[config]/`: Folder containing all outputs
- `metrics_iteration_[n]_[timestamp].txt`: Predictive metrics for each iteration
- `accuracy_progress.png`: Real-time accuracy visualization
- Console output with detailed progress and accuracy metrics

---

## Script 3: Progressive BATCH Alternative

**File:** `ai_prediction_engine_progressive_BATCH_alternative.py`

### Overview
This is an enhanced version of the progressive batch engine with additional features and optimizations for better experiment tracking and metrics management.

### Key Differences from Script 2

1. **Enhanced Metrics Format**
   - Uses more concise, structured predictive rules
   - Focuses on actionable prediction patterns
   - Simplified format for easier parsing and application

2. **Advanced Experiment Tracking**
   - **Experiment Configuration**: Saves complete setup parameters to JSON
   - **Accuracy History**: Maintains detailed JSON history of all accuracy metrics
   - **Enhanced Metadata**: Tracks model, batch size, iterations, and timestamps

3. **Improved Metrics Adjustment**
   - **Focused Error Correction**: Targets specific error cases more precisely
   - **Concise Updates**: Generates more focused metrics adjustments
   - **Better Context**: Includes batch error summaries for comprehensive learning

4. **Comprehensive Reporting**
   - **Experiment Config File**: Complete setup documentation
   - **Accuracy History JSON**: Time-series accuracy data
   - **Final Summary**: Enhanced completion statistics

### How It Works

The core algorithm is similar to Script 2 but with these enhancements:

1. **Experiment Initialization**
   - Saves complete experiment configuration to JSON
   - More detailed initial metrics generation

2. **Enhanced Batch Processing**
   - Improved error tracking and context gathering
   - More precise metrics adjustment prompts

3. **Advanced Analytics**
   - **JSON Accuracy History**: Complete accuracy tracking over time
   - **Experiment Metadata**: Full configuration and results tracking
   - **Enhanced Final Reporting**: More comprehensive completion statistics

### Key Features
- **Experiment reproducibility**: Complete configuration tracking
- **Concise metrics**: Streamlined predictive rules format
- **Comprehensive analytics**: Detailed accuracy history and metadata
- **Enhanced error handling**: More precise error correction
- **Better organization**: Improved file structure and naming

### Output Files
- `prediction_metrics_[config]/`: Main experiment folder
- `experiment_config_[timestamp].json`: Complete experiment setup
- `accuracy_history.json`: Time-series accuracy data
- `metrics_iteration_[n]_[timestamp].txt`: Predictive metrics
- `accuracy_progress.png`: Visual progress tracking

---

## Script 4: Progressive SINGLE Prediction Engine

**File:** `ai_prediction_engine_progressive_SINGLE.py`

### Overview
This script processes predictions one at a time, adjusting metrics after each individual prediction error. It's the simplest of the progressive engines but provides immediate feedback and adaptation.

### How It Works

1. **Initial Analysis**
   - Analyzes first 10 rows to create initial predictive metrics
   - Uses concise, rule-based metrics format

2. **Single Prediction Loop**
   - Processes one passenger prediction at a time
   - For each prediction:
     - Applies current predictive metrics
     - Makes prediction using AI model
     - Compares with actual outcome

3. **Immediate Adaptation**
   - **Error Detection**: Identifies incorrect predictions immediately
   - **Instant Adjustment**: Adjusts metrics after each error
   - **Metrics Saving**: Saves updated metrics after each adjustment

4. **Accuracy Tracking**
   - **Cumulative Accuracy**: Running total accuracy
   - **Rolling Accuracy**: Last 20 predictions performance
   - **Real-time Feedback**: Immediate accuracy updates

### Key Features
- **Immediate feedback**: Adjusts after each prediction
- **Simple architecture**: One prediction at a time
- **Fast iteration**: Quick cycles of prediction and learning
- **Focused learning**: Targets individual error cases precisely

### Key Differences from Batch Versions
- **No batch processing**: Single predictions only
- **Immediate adaptation**: Adjusts after every error (not batch)
- **Simpler error handling**: Focuses on individual cases
- **Faster iterations**: More frequent but smaller adjustments

### Output Files
- `prediction_metrics_[config]/`: Experiment outputs
- `metrics_iteration_[n]_[timestamp].txt`: Metrics after each adjustment
- Console output with real-time accuracy tracking

---

## Comparison of Approaches

| Feature | BULK | Progressive BATCH | BATCH Alternative | SINGLE |
|---------|------|-------------------|-------------------|--------|
| **Prediction Style** | One bulk prediction | Configurable batches | Configurable batches | Single predictions |
| **Learning Approach** | Static analysis | Batch error learning | Enhanced batch learning | Immediate error learning |
| **Metrics Format** | Detailed analysis | Comprehensive rules | Concise rules | Concise rules |
| **Experiment Tracking** | Basic JSON report | Files + plotting | Full JSON history | Files only |
| **Adaptation Speed** | None | After each batch | After each batch | After each error |
| **Complexity** | Simple | High | Very High | Medium |
| **Use Case** | Quick analysis | Research/production | Advanced research | Rapid prototyping |

### When to Use Each Script

- **BULK**: Quick analysis, baseline accuracy, simple predictions
- **Progressive BATCH**: Production systems, batch processing, comprehensive learning
- **BATCH Alternative**: Advanced research, detailed experiment tracking, reproducibility
- **SINGLE**: Rapid prototyping, immediate feedback, simple adaptive learning

---

## Output Files

### Common Files
- **Metrics Files**: `metrics_iteration_[n]_[timestamp].txt` - Predictive rules and patterns
- **Accuracy Plots**: `accuracy_progress.png` - Visual accuracy progression
- **Console Output**: Colored terminal output with real-time status

### Script-Specific Files
- **BULK**: `accuracy_report_[model]_[timestamp].json`
- **BATCH Alternative**: `experiment_config_[timestamp].json`, `accuracy_history.json`

### Folder Structure
```
prediction_metrics_[config]/
├── metrics_iteration_0_[timestamp].txt          # Initial metrics
├── metrics_iteration_1_[timestamp].txt          # After first adjustment
├── metrics_iteration_2_[timestamp].txt          # After second adjustment
├── ...
├── accuracy_progress.png                        # Progress visualization
├── experiment_config_[timestamp].json          # (Alternative only)
├── accuracy_history.json                       # (Alternative only)
└── accuracy_report_[model]_[timestamp].json    # (BULK only)
```

---

## Usage Instructions

### 1. Setup Environment
```bash
# Install dependencies
pip install openai pandas termcolor matplotlib numpy

# Set API key
export OPENROUTER_API_KEY="your_api_key_here"
```

### 2. Prepare Data
Ensure `train.csv` is in the same directory as the scripts.

### 3. Configure Script Parameters
Edit the configuration variables at the top of each script:
```python
MODEL_NAME = "x-ai/grok-4"  # or other OpenRouter models
FIRST_ROWS_TO_ANALYZE = 500  # Analysis rows
ITERATIONS = 100  # For progressive scripts
```

### 4. Run Scripts
```bash
# BULK prediction
python ai_prediction_engine_BULK.py

# Progressive BATCH
python ai_prediction_engine_progressive_BATCH.py

# Progressive BATCH Alternative
python ai_prediction_engine_progressive_BATCH_alternative.py

# Progressive SINGLE
python ai_prediction_engine_progressive_SINGLE.py
```

### 5. Monitor Progress
- Watch colored console output for real-time status
- Check generated folders for metrics and plots
- Review accuracy reports and visualizations

### 6. Analyze Results
- Compare accuracy metrics across different approaches
- Review saved metrics files for learned patterns
- Use accuracy plots to understand learning progression
- Analyze experiment configs for reproducibility

---

## Troubleshooting

### Common Issues
1. **API Key Not Set**: Ensure `OPENROUTER_API_KEY` environment variable is configured
2. **Missing Dependencies**: Install all required packages
3. **Data Format**: Ensure `train.csv` has the expected Spaceship Titanic format
4. **Rate Limits**: OpenRouter may have rate limits for intensive usage

### Error Handling
- All scripts include comprehensive error handling
- Failed predictions are logged and handled gracefully
- Metrics adjustment failures fall back to previous metrics
- File operations include error checking and recovery

---


Experiment with different models to find optimal performance for your use case.

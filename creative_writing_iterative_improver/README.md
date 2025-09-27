# 🎨 Iterative Creative Text Improvement System

A sophisticated AI-powered system that uses conflicting evaluator personas to iteratively improve creative text through parallel evaluation, contextual feedback, and controlled rewriting.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Files & Components](#files--components)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Output Files](#output-files)
- [System Flow](#system-flow)
- [Key Features](#key-features)

## 🎯 Overview

This system implements an **iterative creative improvement pipeline** that:

1. **Generates diverse AI personas** with conflicting evaluation approaches
2. **Evaluates text in parallel** using multiple expert perspectives
3. **Aggregates feedback** while maintaining evaluator context
4. **Rewrites text creatively** while preserving original meaning
5. **Tracks progress** and saves the best performing versions

The system is designed to improve creative text through **conflicting viewpoints** rather than consensus, leading to more nuanced and well-rounded improvements.

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Original Text │───▶│  Parallel Eval  │───▶│  Contextual     │
│                 │    │  5 AI Personas  │    │  Feedback Agg   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                         │
┌─────────────────┐    ┌─────────────────┐               │
│   Controlled    │◀───│   Creative      │◀──────────────┘
│   Rewriting     │    │   Rewriting     │
│   (Length Safe) │    │   (Meaning Safe)│
└─────────────────┘    └─────────────────┘
         │                       │
         └───────────────────────┘
                 ▼
        ┌─────────────────┐
        │   Best Version  │
        │   Always Saved  │
        └─────────────────┘
```

## 📁 Files & Components

### Core Scripts

#### `iterative_improvement.py` - Main System
The heart of the iterative improvement system featuring:
- **Persona generation** with conflicting viewpoints
- **Parallel evaluation** using 5 diverse AI experts
- **Contextual feedback aggregation** with scorer information
- **Length-controlled rewriting** with retry mechanisms
- **Progress visualization** and comprehensive logging
- **Best version preservation** regardless of final outcome

#### `creative_grading.py` - Standalone Grading
A focused script for one-time text evaluation:
- Generates or loads evaluation personas
- Performs parallel grading with 5 experts
- Outputs structured evaluation results
- Useful for quick assessments without iteration

### Supporting Files

#### `API_client.py` - API Interface
Handles all OpenRouter API communications:
- Async API calls with error handling
- Client caching for efficiency
- Support for multiple providers (OpenRouter, OpenAI)

#### `requirements.txt` - Dependencies
```txt
openai          # API client
termcolor       # Colored terminal output
matplotlib      # Progress visualization
numpy          # Numerical operations
```

## 🚀 Installation

1. **Clone or download** the project files
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set environment variables**:
   ```bash
   # For OpenRouter
   export OPENROUTER_API_KEY="your_openrouter_api_key_here"
   ```

## ⚙️ Configuration

### Core Parameters (`iterative_improvement.py`)

```python
# System Limits
MAX_ITERATIONS = 50                    # Maximum improvement cycles
MAX_AVERAGE_SCORE = 9                  # Target score to achieve (1-10)
LENGTH_TOLERANCE_PERCENT = 10          # Allowed length deviation (±10%)

# Quality Controls
MAX_REWRITE_RETRIES = 3                # Retries if length exceeded
MAX_HISTORY_LENGTH = 3                 # Message history limit (pairs)
TOP_SCORING_EXAMPLES = 3               # Best versions to show as examples

# API Settings
MODEL = "openrouter/sonoma-sky-alpha"  # AI model to use
PROVIDER = "openrouter"                # API provider
```

### Input Text

Modify the `TEXT` variable in `iterative_improvement.py`:

```python
TEXT = """
Your creative text content here.
This will be iteratively improved by the system.
"""
```

## 🎮 Usage

### Method 1: Full Iterative Improvement

```bash
python iterative_improvement.py
```

**What happens:**
- Automatically generates conflicting evaluation personas
- Runs up to 50 iterations of evaluate → rewrite → evaluate
- Stops when target score (9.0/10) reached OR max iterations hit
- Saves best version regardless of final outcome

### Method 2: One-Time Grading

```bash
python creative_grading.py
```

**What happens:**
- Generates evaluation personas (if needed)
- Performs single parallel evaluation
- Outputs structured grading results
- No iterative improvement

## 📊 Output Files

### Results Directory Structure
```
results/
├── iteration_1.json          # Complete iteration data
├── iteration_2.json          # Complete iteration data
├── text_iteration_1_score_7.2.txt    # Text with metadata
├── text_iteration_2_score_8.1.txt    # Text with metadata
├── best_version_score_8.7.txt        # Best performing version
├── final_summary.json                # Overall statistics
├── progress_plot.png                 # Visual progress chart
└── personas.json                     # Generated evaluators
```

### File Contents

#### `iteration_X.json` - Complete Iteration Data
```json
{
  "iteration": 5,
  "average_score": 8.73,
  "individual_grades": [
    {
      "person": "1",
      "expertise": "Surrealist Poetry and Imagery",
      "total_score": 9.0,
      "rubrics": [
        {"name": "Creativity", "score": 9},
        {"name": "Technical Skill", "score": 8},
        {"name": "Emotional Impact", "score": 10}
      ],
      "suggestions": ["Enhance metaphors", "Strengthen imagery"]
    }
  ],
  "combined_suggestions": [...],
  "text": "The actual text content..."
}
```

#### `text_iteration_X_score_Y.Z.txt` - Readable Text
```
Iteration 5
Average Score: 8.73/10
Word Count: 42

Text Content:
--------------------------------------------------

[Actual improved text content]
```

#### `best_version_score_X.X.txt` - Best Performance
```
Best Iteration Results
======================
Best Score: 8.73/10
Best Iteration: 5
Word Count: 42

Best Text Content:
--------------------------------------------------

[The highest scoring version]
```

#### `final_summary.json` - System Statistics
```json
{
  "total_iterations": 12,
  "final_average_score": 7.8,
  "best_average_score": 8.7,
  "best_iteration_number": 5,
  "target_achieved": false,
  "improvement_achieved": true
}
```

## 🔄 System Flow

### 1. Initialization
- Load/create 5 conflicting evaluation personas
- Set up progress tracking and visualization
- Initialize conversation history for rewriter

### 2. Evaluation Phase
- **Parallel Processing**: All 5 personas evaluate simultaneously
- **Structured Grading**: Each provides 3 rubric scores + 2-3 suggestions
- **Context Preservation**: Persona expertise and scores included with feedback

### 3. Feedback Aggregation
- Combine suggestions from all evaluators
- Include top-scoring examples from previous iterations
- Maintain persona attribution for credibility weighting

### 4. Creative Rewriting
- **Length Control**: Must stay within ±10% of original word count
- **Content Integrity**: Preserve exact original meaning, no additions/modifications
- **Creative Freedom**: Rewrite in improved style while staying faithful
- **Retry Mechanism**: Up to 3 attempts if length exceeded

### 5. Quality Assurance
- **Progress Plot**: Real-time visualization of improvement trajectory
- **Best Version Tracking**: Always preserve highest-scoring iteration
- **Comprehensive Logging**: Every iteration saved for analysis

### 6. Termination
- **Success**: Target score (9.0/10) achieved
- **Completion**: Maximum iterations (50) reached
- **Best Result**: Always saved regardless of outcome

## 🌟 Key Features

### 🤖 Conflicting AI Personas
- **5 Diverse Evaluators**: Technical, creative, emotional, structural perspectives
- **Natural Tension**: Designed to conflict rather than agree
- **Expert Attribution**: Each suggestion tagged with evaluator and score

### 📏 Quality Safeguards
- **Length Control**: Automatic retry if word count exceeded
- **Content Integrity**: Zero tolerance for meaning alteration
- **Creative Balance**: Improve style without changing substance

### 📊 Comprehensive Tracking
- **Real-time Visualization**: Progress plot updates each iteration
- **Complete Audit Trail**: Every version saved with full metadata
- **Best Version Guarantee**: Highest scoring result always preserved

### 🔄 Intelligent Iteration
- **Contextual Memory**: Rewriter sees conversation history
- **Progressive Learning**: Uses top examples as improvement guides
- **Adaptive Constraints**: Length bounds adjust per iteration

### 🎨 Creative Enhancement
- **Evaluator Synthesis**: Balances conflicting feedback perspectives
- **Style Improvement**: Enhances clarity, flow, and impact
- **Meaning Preservation**: Original intent completely maintained

## 🎯 Best Practices

1. **Text Length**: Start with 50-200 words for optimal iteration
2. **Clear Intent**: Ensure original text has clear purpose/message
3. **Patient Runs**: Let system run multiple iterations for best results
4. **Review Outputs**: Check best_version file for final assessment
5. **Adjust Targets**: Modify MAX_AVERAGE_SCORE based on text type

## 🔧 Troubleshooting

### Common Issues

**"Text too long" errors:**
- Reduce LENGTH_TOLERANCE_PERCENT (default 10%)
- Check that original text length is reasonable
- Model may need clearer length instructions

**Low improvement scores:**
- Try different MODEL setting
- Adjust persona generation prompt for domain expertise
- Ensure original text is clear and well-structured

**API rate limits:**
- Add delays between iterations if needed
- Reduce MAX_ITERATIONS for testing
- Check API key quotas

### Performance Tuning

- **Faster runs**: Reduce MAX_ITERATIONS to 10-20
- **Higher quality**: Increase TOP_SCORING_EXAMPLES to 5
- **Stricter control**: Reduce LENGTH_TOLERANCE_PERCENT to 5%
- **More retries**: Increase MAX_REWRITE_RETRIES to 5

---

**🎨 Created with ❤️ for creative AI-assisted writing improvement**

*This system demonstrates how conflicting AI perspectives can collaboratively enhance creative work while maintaining complete content integrity.*

# Hivemind

A comprehensive collection of AI research projects, experiments, and tools exploring various aspects of artificial intelligence, machine learning, and computational problem-solving. This repository showcases cutting-edge AI techniques, from advanced reasoning systems to creative applications.

## 🧠 Projects Overview

This repository contains multiple experimental projects and research initiatives:

### 🤖 ARC AGI Solver Kit
- **Location**: `ARC_AGI_SOLVER_KIT/`
- **Description**: Automated system for solving ARC (Abstraction and Reasoning Corpus) puzzles using large language models through OpenRouter and OpenAI APIs
- **Features**: 
  - Parallel processing for efficient puzzle solving
  - AI-powered solving with advanced LLMs (OpenRouter Sonoma Sky Alpha)
  - Dimension validation and failure tracking
  - Comprehensive logging with colored terminal output
  - Grid validation tools
- **Datasets**: ARC-AGI (800 puzzles) and ARC-AGI-2 (1122 puzzles)
- **Performance**: Achieves significant success rates on abstract reasoning tasks

### 🎨 Art with Math
- **Location**: `art_with_math/`
- **Description**: Mathematical art generation and visualization using p5.js, demonstrating how simple mathematical concepts create beautiful organic animations
- **Features**:
  - Interactive HTML-based animations with trigonometric functions
  - Real-time rotation demos and loop shape generation
  - Educational progression from basic concepts to complex patterns
  - Visual dartboard representation and convergence analysis
- **Learning Path**: Basic sin/cos → π estimation → statistics → complex animations

### 🌐 Language Learning Experiments
- **Location**: `can_an_llm_learn_a_new_language/`
- **Description**: Comprehensive system for benchmarking Large Language Models on fictional language translation tasks
- **Features**:
  - Creates artificial language transformations with systematic rules
  - Tests LLM translation accuracy using OpenRouter API
  - Generates beautiful accuracy charts and model rankings
  - Word-by-word accuracy measurement with punctuation handling
- **Workflow**: Data creation → Testing → Visualization with 5 Python scripts

### 🔧 Context Engineering
- **Location**: `context_engineer_v3/`
- **Description**: Advanced context engineering system with chat integration and streaming AI responses for comprehensive research
- **Features**:
  - Generates purpose-focused research questions with custom taxonomy
  - Parallel processing for concurrent question answering
  - Interactive chat mode with existing research context
  - Real-time streaming responses with "thinking..." animation
  - Web search integration and cost tracking
- **Modes**: Research generation and interactive chat with seamless navigation

### 📝 Creative Writing AI
- **Location**: `creative_writing_iterative_improver/`
- **Description**: Sophisticated AI-powered system using conflicting evaluator personas to iteratively improve creative text
- **Features**:
  - Parallel evaluation using 5 diverse AI experts with conflicting viewpoints
  - Length-controlled rewriting with retry mechanisms
  - Progress visualization and comprehensive logging
  - Best version preservation regardless of final outcome
- **Innovation**: Uses conflicting perspectives rather than consensus for more nuanced improvements

### 🧮 DSPy GEPA Optimization
- **Location**: `dspy_GEPA/`
- **Description**: DSPy framework experiments with GEPA (Generative Evolutionary Prompt Optimization) for automatically evolving AI prompts
- **Features**:
  - Reflection-based evolution using GPT-5 to analyze failures
  - Automatic prompt optimization from basic to expert-level instructions
  - Math problem solving and travel itinerary planning applications
  - Pareto optimization for multi-objective prompt selection
- **Innovation**: Learns WHY prompts fail, not just that they fail

### 🌳 Dynamic In-Context Learning
- **Location**: `dynamic_in_context_learning/` & `dynamic in context learning v2/`
- **Description**: Advanced in-context learning techniques with dynamic adaptation and tree search integration
- **Features**:
  - Adaptive learning strategies that evolve based on performance
  - Tree search algorithms for optimal context selection
  - Performance optimization through iterative improvement
  - Large-scale experimentation with multiple learning paradigms

### 🎯 Goal Solver with Tree Search
- **Location**: `generalizing_goal_solver_with_tree_search/`
- **Description**: Cutting-edge AI-powered system using parallel Monte Carlo Tree Search with PUCT scoring and 2-stage evaluation
- **Features**:
  - Parallel tree search with 5 concurrent branches
  - 2-stage evaluation system (Stage 1: 70pts, Stage 2: 30pts)
  - Ultra-efficient API usage (only 2 calls for all rubric generation)
  - Harsh AI evaluation with merciless LLM-based assessment
  - Real-time visualization and comprehensive progress tracking
- **Innovation**: Only solutions passing Stage 1 (≥60/70 points) proceed to Stage 2

### 🚀 GPT-5 Experiments
- **Location**: `gpt-5-tool-streaming-examples/` & `GPT-5_verbosity/`
- **Description**: Experiments with GPT-5 capabilities including tool streaming, reasoning, and verbosity analysis
- **Features**:
  - Code interpreter integration with streaming responses
  - Web search capabilities and reasoning streaming
  - Combined tools demonstration
  - Verbosity and reasoning effort parameter testing
- **Analysis**: Parallel requests testing different verbosity levels and reasoning effort values

### 📊 Data Science Projects
- **Location**: `Grok-code-data-scientist/` & `Grok-code-data-scientist (1)/`
- **Description**: Advanced ML scientist script using Grok via OpenRouter to generate, test, and iteratively improve machine learning solutions
- **Features**:
  - 25-iteration improvement cycles with learning from previous attempts
  - Automatic error detection and code fixing
  - Performance optimization and leakage prevention
  - GPU support detection and utilization
  - Comprehensive logging and progress tracking

### 💡 Ideas Generation
- **Location**: `ideas_lists_generator/`
- **Description**: Versatile Python script leveraging LLMs to generate creative and innovative ideas in batches
- **Features**:
  - Batch processing to avoid token limits and API constraints
  - Duplicate prevention and diversity tracking
  - Flexible configuration for different idea types
  - Progress tracking with colored terminal output
  - Error handling with retry mechanisms
- **Applications**: App ideas, business concepts, content ideas, product innovations

### 🔍 In-Context Learning Research
- **Location**: `in-context_learning/` & `in context learning with Tree Search/`
- **Description**: Advanced research into in-context learning methodologies with tree search integration
- **Features**:
  - Tree search algorithms for optimal context selection
  - Adaptive learning strategies and performance optimization
  - Large-scale experimentation with multiple learning paradigms
  - Comprehensive analysis of learning effectiveness

### 🧮 Monte Carlo Simulations
- **Location**: `monte_carlo_simulations/`
- **Description**: Comprehensive, hands-on introduction to Monte Carlo simulations using Python with interactive learning progression
- **Features**:
  - 4 progressive learning files (A-D) from basics to financial applications
  - Interactive demonstrations with real-time updates
  - Visual dartboard representation and ASCII stock charts
  - Geometric probability and statistical foundations
- **Applications**: π estimation, financial modeling, risk analysis, option pricing

### 🤖 Self-Improving Dynamic Learner
- **Location**: `self-improving-dynamic-learner/`
- **Description**: Intelligent system that uses LLMs to automatically generate, test, and improve Python predictor functions through cross-cycle learning
- **Features**:
  - Iterative learning from mistakes with pattern recognition
  - Cross-cycle learning and adaptive improvement
  - Comprehensive evaluation on full datasets
  - Hard examples mode for challenging edge cases
  - Progress visualization and diagnostic tools

### 🔗 Conversations API
- **Location**: `conversations_api/`
- **Description**: OpenAI Conversations API integration with comprehensive documentation and streaming event support
- **Features**:
  - Full CRUD operations for conversations and items
  - Streaming events for real-time responses
  - Metadata support and pagination
  - Tool call integration (code interpreter, web search, MCP)
- **Documentation**: Complete API reference with examples and event schemas

### 🧮 Mathematical Problem Solvers
- **Location**: `LLM_polynomial_solver/` & `graph_throry_solver/`
- **Description**: Specialized AI systems for solving mathematical problems
- **Features**:
  - **Polynomial Solver**: GPT-5-mini factorizes 14th degree polynomials 100% of the time
  - **Graph Theory**: Shortest path finder with GPT-5-mini performing perfectly on 40-node graphs
  - No shortcut methods - pure algorithmic problem solving
  - Performance benchmarking across different models

### 🎛️ Script Commands Master
- **Location**: `script-commands-master/`
- **Description**: Extensive collection of Raycast script commands for productivity automation
- **Features**:
  - 591 shell scripts, 290 PNG images, 172 AppleScript files
  - Productivity automation and workflow optimization
  - Community-driven script collection with documentation
  - Template system for creating custom commands

## 🛠️ Getting Started

### Prerequisites
- Python 3.8+
- Node.js (for web-based projects)
- Git (with submodule support)

### Setup
1. Clone the repository with submodules:
   ```bash
   git clone --recursive https://github.com/yourusername/hivemind.git
   cd hivemind
   ```

2. Initialize and update submodules:
   ```bash
   git submodule update --init --recursive
   ```

3. Install dependencies for specific projects:
   ```bash
   # Example for a Python project
   cd project_name
   pip install -r requirements.txt
   
   # Example for Node.js project
   npm install
   ```

## 📁 Project Structure

Each project directory contains:
- **README.md**: Project-specific documentation
- **requirements.txt**: Python dependencies (where applicable)
- **Source code**: Implementation files
- **Results/Outputs**: Generated results and analysis

## 🔬 Research Areas

This repository explores cutting-edge AI research across multiple domains:

- **🧩 Abstraction and Reasoning**: ARC puzzle solving with advanced tree search algorithms
- **🌐 Language Learning**: LLM language acquisition and translation accuracy benchmarking
- **🔧 Context Engineering**: Advanced context optimization with streaming AI responses
- **🎨 Creative AI**: Iterative writing improvement and idea generation systems
- **⚡ Optimization**: Prompt evolution (GEPA) and model performance optimization
- **🔄 Dynamic Learning**: Self-improving AI systems with cross-cycle learning
- **📊 Mathematical Visualization**: Interactive art generation and Monte Carlo simulations
- **🎯 Problem Solving**: Tree search algorithms and mathematical problem solvers
- **🤖 Model Capabilities**: GPT-5 experiments and reasoning analysis
- **📈 Data Science**: Automated ML pipeline generation and optimization
- **🔗 API Integration**: Advanced API usage patterns and streaming implementations

## 🤝 Contributing

This is a research repository. If you'd like to contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add appropriate documentation
5. Submit a pull request

## 📄 License

This project contains multiple components with different licenses. Please check individual project directories for specific licensing information.

## 🔗 Related Resources

### Core Technologies
- [ARC Challenge](https://github.com/fchollet/ARC) - Abstraction and Reasoning Corpus
- [DSPy Framework](https://github.com/stanfordnlp/dspy) - Declarative self-improving AI systems
- [OpenRouter API](https://openrouter.ai/) - Unified API for multiple LLM providers
- [OpenAI API](https://platform.openai.com/) - GPT models and tools integration
- [p5.js](https://p5js.org/) - Creative coding and mathematical visualization

### Research Papers & References
- [GEPA: Reflective Prompt Evolution](https://arxiv.org/abs/2507.19457) - Evolutionary prompt optimization
- [Monte Carlo Tree Search](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search) - Tree search algorithms
- [In-Context Learning](https://arxiv.org/abs/2001.07676) - Few-shot learning methodologies

### Tools & Frameworks
- [Raycast](https://raycast.com/) - Productivity automation platform
- [Matplotlib/Seaborn](https://matplotlib.org/) - Data visualization
- [TermColor](https://pypi.org/project/termcolor/) - Colored terminal output

### Community & Support
- [DSPy Community](https://github.com/stanfordnlp/dspy) - Framework discussions
- [OpenRouter Discord](https://openrouter.ai/) - API support and model discussions
- [Raycast Community](https://www.raycast.com/community) - Script commands and extensions

---

*This repository represents cutting-edge research and experimentation in artificial intelligence. The projects showcase advanced techniques in reasoning, learning, optimization, and creative applications. Results and findings are shared for educational and research purposes, demonstrating the current state-of-the-art in AI research and development.*

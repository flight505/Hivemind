## Context Engineer

### Purpose
Generate comprehensive, purpose‑focused research questions and, after confirmation, answer them in parallel with up‑to‑date web search. **NEW**: Chat with existing research context using streaming AI responses and seamless navigation between chat and research generation modes.

### What it does
- **Research Generation**: Prompts for a topic, purpose, and optional timeframe
- **Question Design**: Creates custom, non‑overlapping section taxonomy with objective, subject‑matter questions
- **Web Search**: Uses web search during both question generation and answering phases
- **Parallel Processing**: Answers all questions concurrently (async) with concurrency controls
- **File Organization**: Saves outputs in structured folders under `outputs/` directory
- **Chat Mode**: **NEW** - Interactive chat with existing research context, web search is disabled by default
- **Streaming Responses**: **NEW** - Real-time streaming with "thinking..." animation
- **Seamless Navigation**: **NEW** - Switch between chat and research generation modes
- **Cost Tracking**: Logs token usage, web search calls, and flex‑tier cost estimates (GPT‑5 family)
- **Cost Summary**: Prints a bold, banner‑style ALL‑IN TOTAL COST at the end

### Files
- `context_engineer.py` — the main script with chat and streaming capabilities
- `requirements.txt` — dependencies (no version pins)
- `outputs/` — main output directory
- `outputs/<run-folder>/questions.json` — generated questions (saved under the per‑run folder)
- `outputs/<run-folder>/` — per‑section answers and a combined answers file (created after confirmation)
- `outputs/<run-folder>/combined_answers.md` — **NEW** - complete research context for chat mode

### Requirements
- Python 3.9+
- OpenAI API key with access to GPT-5 and web search tools

Install dependencies:
```bash
pip install -r requirements.txt
```

### Configuration
All important variables are defined in ALL CAPS at the top of `context_engineer.py`.

- Questions generation
  - `OPENAI_API_KEY`: read from the environment (required)
  - `MODEL`: e.g., `gpt-5`
  - `REASONING_EFFORT`: `low` | `medium` | `high`
  - `ENABLE_WEB_SEARCH`: enable web search tool during generation
  - `SERVICE_TIER`: usually `flex`
  - `OUTPUT_JSON_PATH`: base filename for questions JSON (the file is saved under the per‑run folder)
  - `TOTAL_QUESTIONS`: `None` for unlimited, or an integer for exact total across sections

- Answering (async)
  - `ANSWER_MODEL`: e.g., `gpt-5`
  - `ANSWER_ENABLE_WEB_SEARCH`: enable web search tool during answering (**default: False for chat mode**)
  - `ANSWER_REASONING_EFFORT`: `low` | `medium` | `high`
  - `ANSWER_SERVICE_TIER`: usually `flex`
  - `ANSWER_OUTPUT_FORMAT`: `markdown` (default) or `text`
  - `OUTPUT_DIR`: default base, but is overridden per run using `topic`‑`purpose`‑`timeframe`
  - `ANSWER_MAX_CONCURRENCY`: max concurrent answer calls
  - `ANSWER_REMOVE_CITATIONS`: remove citations/URLs from answers and combined file (default `True`)
  - `ANSWER_MAX_WEB_SEARCHES`: soft/hard guidance limit in the prompt for tool calls per answer

Set your API key (Windows):
```bat
setx OPENAI_API_KEY YOUR_KEY_HERE
```
Open a new terminal after setting it so the variable is available.

### New Features Overview

#### Chat Mode with Existing Research
- **Interactive Chat**: Chat with any previously generated research context
- **Streaming Responses**: Real-time streaming with "AI: Thinking..." animation
- **Options Menu**: Type `-options` during chat for navigation menu:
  1. Continue chatting
  2. Back to research selection
  3. Generate new research
  4. Exit
- **No Web Search**: Chat mode uses only existing research context (no additional API calls)
- **Seamless Transitions**: Switch between chat and research generation modes

#### Enhanced User Experience
- **Thinking Animation**: Visual feedback during AI processing
- **Organized Outputs**: All research saved under `outputs/` directory
- **Auto-Chat Offer**: After generating new research, automatically offers to chat with it

### Run
```bash
python context_engineer.py
```

#### Two Main Modes:

**Mode 1: Chat with Existing Research**
- Shows available research outputs at startup
- Choose to chat with existing context or generate new research
- Interactive chat with streaming responses
- Use `-options` for navigation between modes

**Mode 2: Generate New Research**
Follow the prompts:
1) Enter the topic
2) Enter the purpose of the research
3) Optionally enter a timeframe

After questions are generated, the script will ask if you want to generate answers in parallel. If you confirm:
- A per‑run directory will be created: `outputs/<sanitized-topic>-<sanitized-purpose>-<sanitized-timeframe>`
- `questions.json` will be written inside that folder
- Each section will have its own subfolder (sanitized name)
- Each question will be saved as a separate file (sanitized first 50 characters)
- A combined file will be written: `combined_answers.md` (or `.txt`)
- **NEW**: Automatically offers to chat with the newly generated research

On success, the script will:
- save the generated JSON to `questions.json`
- print a tally like: `Tally: 9 sections, 147 total questions`
- **NEW**: offer to start chatting with the research immediately

### Output format
Questions JSON (strict schema requested; script falls back if needed):
```json
{
  "topic": "...",
  "purpose": "...",
  "sections": [
    { "name": "...", "questions": ["...", "..."] }
  ]
}
```
If the model returns plain text, the script will fallback to a minimal JSON with a single `Questions` section to avoid losing content.

Answers layout:
- `<run-folder>/<section>/` — one folder per section (sanitized name)
- `<run-folder>/<section>/<question>.md|.txt` — one file per question (first 50 chars, sanitized)
- `<run-folder>/combined_answers.md|.txt` — merged result in chosen format

### Chat Mode Usage

#### Starting Chat
- At startup, the script shows available research outputs
- Choose to chat with existing context or generate new research
- Select a research output by number to start chatting

#### Chat Commands
- **Normal chat**: Type any question to ask the AI about the research
- **`-options`**: Show navigation menu with numbered choices
- **`back` or `b`**: Return to research selection
- **`quit`, `exit`, `bye`**: End current chat session

#### Chat Options Menu
When you type `-options` during chat, you get:
1. **Continue chatting** - Return to current chat
2. **Back to research selection** - Choose different research
3. **Generate new research** - Start new research generation
4. **Exit** - Quit the application

#### Chat Features
- **Streaming Responses**: Real-time text streaming with "AI: Thinking..." animation
- **Full Context Access**: Uses entire `combined_answers.md` for comprehensive answers
- **No Web Search by Default**: `ANSWER_ENABLE_WEB_SEARCH = False` in chat mode - relies solely on existing research context
- **Citation Removal**: Automatically cleans citations from responses

### Behavior and design notes
- **Question Design**: Questions target the subject matter (no "Do you understand…", "How familiar are you…")
- **Dynamic Sections**: Sections are created dynamically; the model is encouraged to be creative yet non‑redundant
- **Web Search**: Can be enabled during research generation and answering phases
- **Parallel Processing**: Answering uses AsyncOpenAI to run calls in parallel with concurrency limit
- **Streaming Chat**: **NEW** - Chat responses stream in real-time with thinking animation
- **Organized Outputs**: **NEW** - All research saved under structured `outputs/` directory
- **Seamless Navigation**: **NEW** - Switch between chat and research generation modes
- **Console Output**: Uses `termcolor` for colorful status updates:
  - `INFO` (general info), `OK` (success), `WARN` (warnings), `ERROR` (errors)
  - `USAGE` (tokens), `SEARCH` (web search calls), `COST` (pricing)
  - Final banner showing ALL‑IN TOTAL COST
- **Cost Tracking**: Computed for GPT‑5 family on `flex` tier only; includes model tokens and web search per‑call pricing
- **Citation Handling**: Citations/URLs are removed by default without breaking Markdown structure (can be disabled)

### Controlling the number of questions
Set `TOTAL_QUESTIONS` in `context_engineer.py`:
```python
TOTAL_QUESTIONS = 120  # or None
```
When set, the prompt asks the model to “produce exactly N total questions across sections.” When `None`, the model is free to generate as many as needed.

### Web search behavior and limits
- The answering prompt instructs the model to use at most `ANSWER_MAX_WEB_SEARCHES` targeted tool calls (default 3). This is a hard limit guidance embedded in the prompt.
- **Chat Mode**: Web search is **disabled by default** (`ANSWER_ENABLE_WEB_SEARCH = False`) - relies entirely on existing research context for responses.
- **To enable web search in chat**: Change `ANSWER_ENABLE_WEB_SEARCH = True` in the script configuration.

### Streaming Events Support
**NEW**: Chat mode supports real-time streaming using OpenAI streaming events:
- **ResponseOutputTextDelta**: Streams text chunks as they arrive
- **ResponseTextDone**: Handles completion of text streaming
- **Automatic Fallback**: If streaming fails, automatically falls back to non-streaming mode
- **Thinking Animation**: Shows "AI: Thinking..." until first token arrives, then transitions to streaming

### Troubleshooting

#### General Issues
- **Missing API key**: ensure `OPENAI_API_KEY` is set in your environment
- **Empty output**: re-run; optionally increase `REASONING_EFFORT`, or set `TOTAL_QUESTIONS`
- **Answering rate limits**: reduce `ANSWER_MAX_CONCURRENCY`
- **Output file names**: they are sanitized and truncated to 50 characters
- **Network/API errors**: transient; try again after a short delay

#### Chat Mode Issues
- **No research outputs available**: Generate some research first, or check if `outputs/` directory exists
- **Streaming not working**: Falls back to non-streaming mode automatically
- **Chat context not loading**: Ensure `combined_answers.md` exists in the research folder
- **Options menu not appearing**: Type `-options` (with the dash) during chat

#### New Feature Notes
- **Thinking animation**: May appear briefly even with fast responses due to network latency
- **Chat context**: Uses the complete research file for comprehensive answers
- **Navigation**: You can always return to previous menus using `back` or `-options`
- **File organization**: All new research is saved under `outputs/` directory automatically

### Privacy
Inputs are not persisted by the script. Generated files are written only to the per‑run folder under `outputs/`:
- `outputs/<run-folder>/questions.json`
- `outputs/<run-folder>/<section>/<question>.md|.txt`
- `outputs/<run-folder>/combined_answers.md|.txt` — also used for chat mode context

**NEW**: Chat mode uses existing `combined_answers.md` files and does not make additional API calls or persist chat history.

### Recent Improvements

#### Version 2.0 - Enhanced Interactive Experience
- **🆕 Chat Mode**: Interactive chat with existing research context
- **⚡ Streaming Responses**: Real-time text streaming with "thinking..." animation
- **🧭 Options Menu**: Type `-options` during chat for navigation menu
- **🔄 Seamless Navigation**: Switch between chat and research generation modes
- **📁 Organized Outputs**: All research saved under structured `outputs/` directory
- **🎯 Full Context Access**: Chat uses complete `combined_answers.md` files
- **🚫 No Web Search in Chat**: Chat mode relies solely on existing research
- **🎨 Enhanced UX**: Visual feedback and improved user experience
- **🔧 Robust Error Handling**: Automatic fallbacks for streaming failures
- **📊 Auto-Chat Offer**: Automatically offers to chat with newly generated research

#### Previous Features
- Parallel question answering with AsyncOpenAI
- Custom section taxonomy generation
- Web search integration for research and answering
- Cost tracking and usage metrics
- Citation removal and content cleaning
- Structured file organization and sanitization


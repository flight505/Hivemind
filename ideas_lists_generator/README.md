# Idea Generator & List Maker

A versatile Python script that leverages Large Language Models (LLMs) to generate creative and innovative ideas of any type in batches. This tool helps creators, entrepreneurs, developers, and content makers discover new concepts, projects, or ideas across various domains and use cases.

## Features

- **Batch Processing**: Generates ideas in configurable batches to avoid token limits and API constraints
- **Duplicate Prevention**: Tracks previously generated ideas to ensure diversity and uniqueness
- **Flexible Configuration**: Easily customize the number of ideas, model parameters, and output format
- **Progress Tracking**: Real-time progress updates with colored terminal output
- **File Output**: Automatically saves all generated ideas to a text file
- **Error Handling**: Robust error handling with retry mechanisms and detailed logging

## Requirements

The following Python packages are required (install via pip):

```bash
pip install fastapi uvicorn jinja2 python-multipart termcolor openai
```

**Note**: Package versions are not specified in requirements.txt to allow for flexibility and automatic version resolution.

## Environment Setup

### API Keys

You need to set up API keys for your chosen LLM provider:

#### OpenRouter (Default)
Set the environment variable:
```bash
export OPENROUTER_API_KEY=your_openrouter_api_key_here
```

#### OpenAI
Set the environment variable:
```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

## Configuration

The script uses several important variables defined at the top of the file. You can customize these based on your needs:

| Variable | Description | Default Value |
|----------|-------------|---------------|
| `MODEL_NAME` | The LLM model to use for generation | `"openrouter/sonoma-sky-alpha"` |
| `PROVIDER` | API provider ("openrouter" or "openai") | `"openrouter"` |
| `OUTPUT_FILE` | Output file name for generated ideas | `"generated_ideas.txt"` |
| `N_IDEAS` | Total number of ideas to generate | `10000` |
| `IDEAS_PER_CALL` | Number of ideas to generate per API call | `100` |
| `USER_INPUT_TYPE` | The type/category of ideas to generate | `"app ideas that leverage Large Language Models (LLMs)"` |

## Usage

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**:
   Configure your API keys as described in the Environment Setup section.

3. **Run the Script**:
   ```bash
   python generate_app_ideas.py
   ```

The script will automatically:
- Generate ideas in batches
- Track progress with colored output
- Save results to the specified output file
- Handle errors and retries gracefully

## Output Format

Generated ideas are saved to the specified output file with the following format:

```
1. AI-powered personal finance advisor that analyzes spending patterns and provides real-time budgeting suggestions
2. Virtual reality language learning platform with immersive cultural experiences
3. Blockchain-based supply chain tracker for ethical sourcing verification
...
```

Each idea includes:
- Sequential numbering
- Clear, concise description (typically 10-20 words)
- Focus on the core concept and value proposition

**The script can generate ideas for any domain by changing the `USER_INPUT_TYPE` variable:**
- Business ideas
- Product concepts
- Content ideas (blogs, videos, podcasts)
- Service innovations
- Creative projects
- Research topics
- And much more...

## Customization Examples

### Generate Business Ideas
Modify the `USER_INPUT_TYPE` variable:
```python
USER_INPUT_TYPE = "business ideas that improve productivity and efficiency"
```

### Generate Content Ideas
For blog posts or videos:
```python
USER_INPUT_TYPE = "blog post ideas about technology and innovation"
```

### Generate Product Ideas
For physical or digital products:
```python
USER_INPUT_TYPE = "innovative product concepts for sustainable living"
```

### Use Different Model
Change the model and provider:
```python
MODEL_NAME = "openai/gpt-4"
PROVIDER = "openai"
```

### Generate Fewer Ideas
Reduce the total count:
```python
N_IDEAS = 100  # Generate 100 ideas instead of 10,000
```

## Progress Monitoring

The script provides real-time feedback through colored terminal output:

- 🔄 **Yellow**: Batch processing status
- 📊 **Blue**: Progress statistics and API call information
- 🤖 **Blue**: Model information
- ✅ **Green**: Successful operations
- 💾 **Cyan**: File save confirmations
- ❌ **Red**: Errors and failures

## Troubleshooting

### Common Issues

1. **API Key Not Set**:
   ```
   ValueError: OPENROUTER_API_KEY environment variable is required
   ```
   **Solution**: Set your API key as an environment variable before running the script.

2. **Rate Limiting**:
   If you encounter rate limits, reduce `IDEAS_PER_CALL`:
   ```python
   IDEAS_PER_CALL = 50  # Reduce batch size
   ```

3. **Empty Responses**:
   The script includes safeguards to skip invalid responses and continue processing.

4. **Network Issues**:
   The script will retry failed API calls automatically and provide error details.

### Getting Help

If you encounter issues:
1. Check that your API key is correctly set
2. Verify your internet connection
3. Review the colored output for specific error messages
4. Consider reducing batch sizes if you're hitting rate limits

## Example Output

```
🚀 Starting app ideas generation...
📋 Target: 10000 ideas, 100 per call

🔄 Call 1: Generating 100 ideas...
📊 Progress: 0/10000 ideas accumulated
🤖 Calling model: openrouter/sonoma-sky-alpha
✅ Successfully generated batch!
💾 Saved 100 new ideas to file
📊 Total accumulated: 100/10000

✅ Generation complete!
📁 All ideas saved to generated_ideas.txt
📊 Final count: 10000 ideas
📊 Total API calls: 100
```

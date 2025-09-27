import openai
import os
import asyncio

# OpenRouter configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize OpenAI async client with OpenRouter base URL
client = openai.AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

async def make_openrouter_call(model_name, messages, reasoning_effort):
    try:
        response = await client.chat.completions.create(
            model=model_name,
            messages=messages,
            reasoning_effort=reasoning_effort
        )
        return response
    except Exception as e:
        print(f"Error making API call: {e}")
        return None


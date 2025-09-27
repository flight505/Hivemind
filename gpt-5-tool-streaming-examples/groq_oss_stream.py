#!/usr/bin/env python
import os
import sys
from typing import List, Dict, Any

from termcolor import colored
from groq import Groq


MODEL_ID = "openai/gpt-oss-120b"


def require_groq_key() -> None:
    api_key = os.environ.get("GROQ_API_KEY")
    if api_key:
        return
    print(colored("Missing GROQ_API_KEY environment variable.", "red", attrs=["bold"]))
    print(
        colored(
            "On Windows, set it like this (then open a new terminal):\n"
            "  setx GROQ_API_KEY YOUR_KEY_HERE",
            "yellow",
        )
    )
    sys.exit(1)


def print_banner() -> None:
    title = colored("Groq Streaming Chat (GPT-OSS 120B)", "cyan", attrs=["bold"])
    model = colored(f"Model: {MODEL_ID}", "magenta")
    hint = colored("Type /help for commands. Type /exit to quit.", "yellow")
    print(title)
    print(model)
    print(hint)
    print()


def print_help() -> None:
    print(colored("Commands:", "cyan", attrs=["bold"]))
    print(colored("  /help", "green"), "- Show this help message")
    print(colored("  /clear", "green"), "- Clear conversation history")
    print(colored("  /exit", "green"), "- Quit the chat")
    print()


def main() -> None:
    require_groq_key()
    client = Groq()
    print_banner()

    # OpenAI-compatible chat history
    messages: List[Dict[str, Any]] = []

    while True:
        try:
            user_input = input(colored("You > ", "green"))
        except (EOFError, KeyboardInterrupt):
            print()
            break

        user_input = user_input.strip()
        if not user_input:
            continue
        if user_input.lower() in {"/exit", "/quit"}:
            break
        if user_input.lower() == "/help":
            print_help()
            continue
        if user_input.lower() == "/clear":
            messages.clear()
            print(colored("Conversation cleared.", "yellow"))
            continue

        messages.append({"role": "user", "content": user_input})

        reasoning_printed_header = False
        answer_printed_header = False
        reasoning_parts: List[str] = []
        answer_parts: List[str] = []

        try:
            stream = client.chat.completions.create(
                model=MODEL_ID,
                messages=messages,
                stream=True,
                temperature=0.6,
                # GPT-OSS supports reasoning_effort; "high" produces more reasoning tokens
                reasoning_effort="high",
                # For GPT-OSS, reasoning_format is fixed to parsed; reasoning appears in message.reasoning
            )

            for chunk in stream:
                try:
                    choice = chunk.choices[0]
                    delta = getattr(choice, "delta", None)
                    if not delta:
                        continue

                    # Stream reasoning increments if provided in delta
                    # For GPT-OSS, reasoning is parsed and placed in message.reasoning.
                    # During streaming, SDK may expose partials under delta.reasoning.
                    delta_reasoning = getattr(delta, "reasoning", None)
                    if not delta_reasoning:
                        # Fallback to dict access if available
                        try:
                            delta_dict = delta.model_dump()  # pydantic v2
                        except Exception:
                            delta_dict = getattr(delta, "__dict__", {})
                        if isinstance(delta_dict, dict):
                            delta_reasoning = delta_dict.get("reasoning")

                    if delta_reasoning:
                        if not reasoning_printed_header:
                            print(colored("Reasoning >", "yellow", attrs=["bold"]))
                            reasoning_printed_header = True
                        reasoning_parts.append(delta_reasoning)
                        print(colored(delta_reasoning, "yellow"), end="", flush=True)

                    # Stream normal assistant content
                    delta_content = getattr(delta, "content", None)
                    if delta_content:
                        if not answer_printed_header:
                            print() if reasoning_printed_header else None
                            print(colored("Assistant >", "cyan", attrs=["bold"]))
                            answer_printed_header = True
                        answer_parts.append(delta_content)
                        print(colored(delta_content, "white"), end="", flush=True)
                except Exception:
                    # Ignore malformed chunks safely
                    continue
        except Exception as e:
            print(colored(f"\n[Groq stream error] {e}", "red"))
            # Do not append assistant on failure
            continue

        print()  # newline after streaming

        final_answer = ("".join(answer_parts)).strip()
        if final_answer:
            messages.append({"role": "assistant", "content": final_answer})

    print(colored("Goodbye!", "magenta"))


if __name__ == "__main__":
    main()


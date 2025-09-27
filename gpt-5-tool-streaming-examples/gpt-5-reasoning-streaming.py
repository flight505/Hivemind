#!/usr/bin/env python
import os
import sys
from termcolor import colored
from openai import OpenAI


MODEL_NAME = "gpt-5"


def require_api_key() -> None:
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        return
    print(colored("Missing OPENAI_API_KEY environment variable.", "red", attrs=["bold"]))
    print(
        colored(
            "On Windows, set it like this (then open a new terminal):\n"
            "  setx OPENAI_API_KEY YOUR_KEY_HERE",
            "yellow",
        )
    )
    sys.exit(1)


def print_banner() -> None:
    title = colored("OpenAI Terminal Chatbot (Responses API)", "cyan", attrs=["bold"])
    model = colored(f"Model: {MODEL_NAME}", "magenta")
    help_hint = colored("Type /help for commands. Type /exit to quit.", "yellow")
    print(title)
    print(model)
    print(help_hint)
    print()


def print_help() -> None:
    print(colored("Commands:", "cyan", attrs=["bold"]))
    print(colored("  /help", "green"), "- Show this help message")
    print(colored("  /clear", "green"), "- Clear conversation history")
    print(colored("  /exit", "green"), "- Quit the chatbot")
    print()


def build_conversation_transcript(history: list[tuple[str, str]], user_message: str) -> str:
    lines: list[str] = []
    # Provide a brief system instruction to keep answers useful and concise
    lines.append(
        "System: You are a helpful, concise assistant. Answer clearly and helpfully."
    )
    for role, content in history:
        prefix = "User" if role == "user" else "Assistant"
        lines.append(f"{prefix}: {content}")
    lines.append(f"User: {user_message}")
    lines.append("Assistant:")
    return "\n".join(lines)


def main() -> None:
    require_api_key()
    client = OpenAI()
    print_banner()

    conversation_history: list[tuple[str, str]] = []

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
            conversation_history.clear()
            print(colored("Conversation cleared.", "yellow"))
            continue

        conversation_text = build_conversation_transcript(conversation_history, user_input)

        assistant_text_parts: list[str] = []
        reasoning_summary_parts: list[str] = []
        printed_reasoning_header = False
        printed_answer_header = False

        # Stream the response tokens as they arrive
        try:
            with client.responses.stream(
                model=MODEL_NAME,
                input=conversation_text,
                reasoning={"effort": "low", "summary": "auto"},
            ) as stream:
                for event in stream:
                    # Stream reasoning summaries (text form)
                    if getattr(event, "type", None) == "response.reasoning_summary_text.delta":
                        delta_text = getattr(event, "delta", "")
                        if delta_text:
                            if not printed_reasoning_header:
                                print(colored("Reasoning >", "yellow", attrs=["bold"]))
                                printed_reasoning_header = True
                            reasoning_summary_parts.append(delta_text)
                            print(colored(delta_text, "yellow"), end="", flush=True)
                        continue

                    # Stream reasoning summaries (structured form)
                    if getattr(event, "type", None) == "response.reasoning_summary.delta":
                        delta_obj = getattr(event, "delta", None)
                        summary_text = None
                        # Try best-effort extraction
                        if hasattr(delta_obj, "text"):
                            summary_text = getattr(delta_obj, "text")
                        elif isinstance(delta_obj, dict):
                            summary_text = delta_obj.get("text")
                        if summary_text:
                            if not printed_reasoning_header:
                                print(colored("Reasoning >", "yellow", attrs=["bold"]))
                                printed_reasoning_header = True
                            reasoning_summary_parts.append(summary_text)
                            print(colored(summary_text, "yellow"), end="", flush=True)
                        continue

                    if getattr(event, "type", None) == "response.output_text.delta":
                        delta_text = getattr(event, "delta", "")
                        if delta_text:
                            if not printed_answer_header:
                                print() if printed_reasoning_header else None
                                print(colored("Assistant >", "cyan", attrs=["bold"]))
                                printed_answer_header = True
                            assistant_text_parts.append(delta_text)
                            # Print token deltas live
                            print(colored(delta_text, "white"), end="", flush=True)
                    elif getattr(event, "type", None) == "response.error":
                        err = getattr(event, "error", None)
                        print(colored(f"\n[Stream error] {err}", "red"))
                # Ensure we have the final aggregated response object (optional)
                _ = stream.get_final_response()
        except Exception as api_error:
            print(colored(f"[Streaming failed] {api_error}", "red"))
            assistant_text_parts.append("")

        print()  # newline after streaming output

        assistant_text = "".join(assistant_text_parts).strip() or "(No text output returned)"

        # Save to local history for multi-turn context
        conversation_history.append(("user", user_input))
        conversation_history.append(("assistant", assistant_text))

    print(colored("Goodbye!", "magenta"))


if __name__ == "__main__":
    main()


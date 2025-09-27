#!/usr/bin/env python
import os, sys, warnings
from termcolor import colored
from openai import OpenAI

# IMPORTANT CONFIG (ALL CAPS)
MODEL_NAME = "gpt-5"
REASONING_EFFORT = "medium"  # low | medium | high
SYSTEM_INSTRUCTIONS = "You are a helpful, concise assistant. Use web_search when current info is needed."
TOOLS = [{"type": "web_search"}]
USER_INPUT = ""
DEBUG_EVENTS = False

# Suppress noisy SDK serializer warnings (harmless but verbose)
warnings.filterwarnings("ignore", category=UserWarning, module=r"pydantic\.main", message=r"Pydantic serializer warnings:")


def require_api_key() -> None:
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        return
    print(colored("Missing OPENAI_API_KEY environment variable.", "red", attrs=["bold"]))
    print(colored("On Windows: setx OPENAI_API_KEY YOUR_KEY_HERE (open a new terminal)", "yellow"))
    sys.exit(1)


def print_banner() -> None:
    print(colored("OpenAI GPT-5 Terminal Chat (Web Search + Reasoning)", "cyan", attrs=["bold"]))
    print(colored(f"Model: {MODEL_NAME} | Reasoning: {REASONING_EFFORT}", "magenta"))
    print(colored("Type /help for commands. Type /exit to quit.", "yellow"), "\n")


def print_help() -> None:
    print(colored("Commands:", "cyan", attrs=["bold"]))
    for cmd, desc in [("/help", "Show this help message"), ("/clear", "Clear conversation history"), ("/exit", "Quit the chat")]:
        print(colored(f"  {cmd}", "green"), f"- {desc}")
    print()


def build_conversation_transcript(history, user_message) -> str:
    return "\n".join([
        f"System: {SYSTEM_INSTRUCTIONS}",
        *[f"{'User' if r=='user' else 'Assistant'}: {c}" for r, c in history],
        f"User: {user_message}",
        "Assistant:",
    ])


def _as_dict(obj) -> dict:
    if obj is None or isinstance(obj, dict):
        return obj or {}
    try:
        return obj.model_dump()  # type: ignore[attr-defined]
    except Exception:
        return {k: getattr(obj, k) for k in ("type","delta","error","query","url","results","text","code") if hasattr(obj, k)}


def main() -> None:
    global USER_INPUT
    require_api_key()
    client = OpenAI()
    print_banner()
    history = []

    while True:
        try:
            USER_INPUT = input(colored("You > ", "green"))
        except (EOFError, KeyboardInterrupt):
            print()
            break

        USER_INPUT = USER_INPUT.strip()
        if not USER_INPUT:
            continue

        if USER_INPUT.lower() in {"/exit", "/quit"}:
            break
        if USER_INPUT.lower() == "/help":
            print_help()
            continue
        if USER_INPUT.lower() == "/clear":
            history.clear()
            print(colored("Conversation cleared.", "yellow"))
            continue

        convo_text = build_conversation_transcript(history, USER_INPUT)

        answer_parts, printed = [], {"reasoning": False, "assistant": False, "web": False}

        try:
            with client.responses.stream(
                model=MODEL_NAME,
                input=convo_text,
                tools=TOOLS,
                reasoning={"effort": REASONING_EFFORT, "summary": "auto"},
            ) as stream:
                for event in stream:
                    etype = getattr(event, "type", "") or ""
                    if DEBUG_EVENTS and etype:
                        print(colored(f"[event] {etype}", "grey"))

                    # Reasoning summaries (text or structured)
                    if etype in {"response.reasoning_summary_text.delta", "response.reasoning_summary.delta"}:
                        text = getattr(event, "delta", None)
                        if isinstance(text, str) and text:
                            pass
                        else:
                            dd = _as_dict(getattr(event, "delta", None))
                            text = dd.get("text") if isinstance(dd, dict) else None
                        if text:
                            if not printed["reasoning"]:
                                print(colored("Reasoning >", "yellow", attrs=["bold"]))
                                printed["reasoning"] = True
                            print(colored(text, "yellow"), end="", flush=True)
                        continue

                    # Web Search events (best-effort across SDK versions)
                    ed = _as_dict(event)
                    tool_name = ed.get("name") or ed.get("tool_name")
                    is_search_event = (isinstance(tool_name, str) and tool_name == "web_search") or ("web_search" in etype) or ("search" in etype)
                    if is_search_event:
                        if not printed["web"]:
                            print() if printed["reasoning"] else None
                            print(colored("Web Search >", "magenta", attrs=["bold"]))
                            printed["web"] = True
                        # Status lifecycle
                        if etype.endswith("in_progress"):
                            print(colored("[in progress]", "magenta"))
                        elif etype.endswith("completed") or etype.endswith("done"):
                            print(colored("[completed]", "magenta"))
                        # Query, URL, deltas, or result snippets
                        q = ed.get("query") or ed.get("input")
                        if isinstance(q, str) and q:
                            print(colored(f"query: {q}", "white"))
                        u = ed.get("url")
                        if isinstance(u, str) and u:
                            print(colored(f"url: {u}", "white"))
                        d = ed.get("delta")
                        if isinstance(d, str) and d:
                            print(colored(d, "white"), end="", flush=True)
                        t = ed.get("text")
                        if isinstance(t, str) and t:
                            print(colored(t, "white"), end="", flush=True)
                        # Summarize results length if present
                        results = ed.get("results")
                        if isinstance(results, list) and results:
                            print(colored(f"results: {len(results)}", "white"))
                        continue

                    # Assistant output
                    if etype == "response.output_text.delta":
                        delta = getattr(event, "delta", "")
                        if delta:
                            if not printed["assistant"]:
                                print() if (printed["reasoning"] or printed["web"]) else None
                                print(colored("Assistant >", "cyan", attrs=["bold"]))
                                printed["assistant"] = True
                            answer_parts.append(delta)
                            print(colored(delta, "white"), end="", flush=True)
                        continue

                    if etype == "response.error":
                        err = getattr(event, "error", None)
                        print(colored(f"\n[Stream error] {err}", "red"))

                # Ensure we drain the final aggregate response (not printed here)
                _ = stream.get_final_response()
        except Exception as e:
            print(colored(f"[Streaming failed] {e}", "red"))
            answer_parts.append("")

        print()
        final_answer = ("".join(answer_parts).strip()) or "(No text output returned)"
        history.append(("user", USER_INPUT))
        history.append(("assistant", final_answer))

    print(colored("Goodbye!", "magenta"))


if __name__ == "__main__":
    main()



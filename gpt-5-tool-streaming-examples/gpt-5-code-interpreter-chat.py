#!/usr/bin/env python
import os, sys
from typing import Any, Dict, List, Tuple, Optional
from termcolor import colored
from openai import OpenAI

# CONFIG (important values in ALL CAPS)
MODEL_NAME: str = "gpt-5"
REASONING_EFFORT: str = "medium"
SYSTEM_INSTRUCTIONS: str = (
    "You are a helpful assistant. Be concise. When calculations, data analysis, "
    "plotting, or code execution would help, use the Code Interpreter tool. when you generate images or CSVs and other files, make sure to return them to the user."
)
TOOLS: List[Dict[str, Any]] = [{"type": "code_interpreter", "container": {"type": "auto"}}]
USER_INPUT: str = ""
OUTPUT_DIR: str = "ci_outputs"
SAVE_DOWNLOADED_FILES: bool = True


def require_api_key() -> None:
    if os.environ.get("OPENAI_API_KEY"): return
    print(colored("Missing OPENAI_API_KEY environment variable.", "red", attrs=["bold"]))
    print(colored("On Windows: setx OPENAI_API_KEY YOUR_KEY_HERE (open a new terminal)", "yellow"))
    sys.exit(1)


def print_banner() -> None:
    print(colored("OpenAI GPT-5 Terminal Chat (Code Interpreter + Reasoning)", "cyan", attrs=["bold"]))
    print(colored(f"Model: {MODEL_NAME}", "magenta"))
    print(colored("Type /help for commands. Type /exit to quit.", "yellow"))
    print()


def print_help() -> None:
    print(colored("Commands:", "cyan", attrs=["bold"]))
    print(colored("  /help", "green"), "- Show this help message")
    print(colored("  /clear", "green"), "- Clear conversation history")
    print(colored("  /exit", "green"), "- Quit the chat"), print()


def build_conversation_transcript(history: List[Tuple[str, str]], user_message: str) -> str:
    lines = [f"System: {SYSTEM_INSTRUCTIONS}"]
    lines += [f"{'User' if r=='user' else 'Assistant'}: {c}" for r, c in history]
    lines += [f"User: {user_message}", "Assistant:"]
    return "\n".join(lines)


def _as_dict(obj: Any) -> Dict[str, Any]:
    if obj is None or isinstance(obj, dict): return obj or {}
    try: return obj.model_dump()  # type: ignore[attr-defined]
    except Exception: return {}


def _get_nested(d: Dict[str, Any], *keys: str, default: Any = None) -> Any:
    cur: Any = d
    for k in keys:
        if isinstance(cur, dict) and k in cur: cur = cur[k]
        else: return default
    return cur


def _ensure_output_dir() -> None:
    if SAVE_DOWNLOADED_FILES:
        try: os.makedirs(OUTPUT_DIR, exist_ok=True)
        except Exception: pass


def _extract_file(obj: Dict[str, Any]) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    if isinstance(obj.get("file_id"), str):
        return obj.get("file_id"), obj.get("filename"), obj.get("container_id") or _get_nested(obj, "container", "id")
    for k in ("file", "image", "image_file"):
        nested = obj.get(k)
        if isinstance(nested, dict):
            fid = nested.get("file_id") or nested.get("id")
            if isinstance(fid, str):
                cid = nested.get("container_id") or _get_nested(nested, "container", "id")
                return fid, nested.get("filename"), cid
    if isinstance(obj.get("id"), str) and obj.get("id").startswith("file-"): return obj.get("id"), obj.get("filename"), None
    return None, None, None


def _download(client: OpenAI, fid: str, fname: Optional[str], cid: Optional[str]) -> Optional[str]:
    if not SAVE_DOWNLOADED_FILES: return None
    _ensure_output_dir()
    try:
        if isinstance(fid, str) and fid.startswith("file-"):
            resp = client.files.content(fid)
        elif isinstance(fid, str) and fid.startswith("cfile_") and isinstance(cid, str):
            cont = getattr(getattr(client, "containers", None), "files", None)
            if cont is None: return None
            getc = getattr(getattr(cont, "content", cont), "retrieve", None)
            if callable(getc): resp = getc(container_id=cid, file_id=fid)
            else: return None
        else: return None
        base = fname or fid
        if "." not in os.path.basename(base): base += ".bin"
        path = os.path.join(OUTPUT_DIR, base)
        with open(path, "wb") as f:
            data = getattr(resp, "read", None)
            if callable(data): f.write(resp.read())
            else:
                blob = getattr(resp, "content", None) or getattr(resp, "body", None) or getattr(resp, "data", None) or getattr(resp, "text", b"")
                if isinstance(blob, str): blob = blob.encode("utf-8", errors="ignore")
                f.write(blob)
        return path
    except Exception as e:
        print(colored(f"[Download failed for {fid}] {e}", "red")); return None


def _harvest_and_download_files(client: OpenAI, obj: Any, seen: set[str]) -> List[str]:
    out: List[str] = []
    try:
        if isinstance(obj, dict):
            fid, fname, cid = _extract_file(obj)
            if fid and fid not in seen:
                p = _download(client, fid, fname, cid)
                if p: seen.add(fid); out.append(p)
            for v in obj.values(): out += _harvest_and_download_files(client, v, seen)
        elif isinstance(obj, list):
            for it in obj: out += _harvest_and_download_files(client, it, seen)
    except Exception: pass
    return out


def main() -> None:
    global USER_INPUT
    require_api_key(); client = OpenAI(); print_banner()
    history: List[Tuple[str, str]] = []

    while True:
        try: USER_INPUT = input(colored("You > ", "green"))
        except (EOFError, KeyboardInterrupt): print(); break
        USER_INPUT = USER_INPUT.strip()
        if not USER_INPUT: continue
        if USER_INPUT.lower() in {"/exit", "/quit"}: break
        if USER_INPUT.lower() == "/help": print_help(); continue
        if USER_INPUT.lower() == "/clear": history.clear(); print(colored("Conversation cleared.", "yellow")); continue

        convo = build_conversation_transcript(history, USER_INPUT)
        answer_parts: List[str] = []
        printed_reasoning = printed_answer = printed_tool = False

        try:
            with client.responses.stream(
                model=MODEL_NAME,
                input=convo,
                tools=TOOLS,
                reasoning={"effort": REASONING_EFFORT, "summary": "auto"},
            ) as stream:
                for event in stream:
                    et = getattr(event, "type", "") or ""

                    # reasoning summaries
                    if et == "response.reasoning_summary_text.delta":
                        t = getattr(event, "delta", "")
                        if t:
                            if not printed_reasoning: print(colored("Reasoning >", "yellow", attrs=["bold"])); printed_reasoning = True
                            print(colored(t, "yellow"), end="", flush=True)
                        continue
                    if et == "response.reasoning_summary.delta":
                        d = getattr(event, "delta", None)
                        txt = getattr(d, "text", None) if d is not None else None
                        if not txt: txt = _as_dict(d).get("text")
                        if txt:
                            if not printed_reasoning: print(colored("Reasoning >", "yellow", attrs=["bold"])); printed_reasoning = True
                            print(colored(txt, "yellow"), end="", flush=True)
                        continue

                    # code interpreter lifecycle + code
                    if et in {
                        "response.code_interpreter_call.in_progress",
                        "response.code_interpreter_call.interpreting",
                        "response.code_interpreter_call.completed",
                        "response.code_interpreter_call_code.delta",
                        "response.code_interpreter_call_code.done",
                    }:
                        if not printed_tool: print() if printed_reasoning else None; print(colored("Code Interpreter >", "blue", attrs=["bold"])); printed_tool = True
                        if et.endswith("in_progress"): print(colored("[in progress]", "blue"))
                        elif et.endswith("interpreting"): print(colored("[interpreting]", "blue"))
                        elif et.endswith("completed"): print(colored("[completed]", "blue"))
                        elif et.endswith("code.delta"):
                            dc = getattr(event, "delta", "")
                            if isinstance(dc, str) and dc: print(colored(dc, "white"), end="", flush=True)
                        elif et.endswith("code.done"):
                            fc = getattr(event, "code", "")
                            if isinstance(fc, str) and fc: print(); print(colored("[final code]", "blue")); print(colored(fc, "white"))
                        continue

                    # assistant output
                    if et == "response.output_text.delta":
                        t = getattr(event, "delta", "")
                        if t:
                            if not printed_answer:
                                if printed_reasoning or printed_tool: print()
                                print(colored("Assistant >", "cyan", attrs=["bold"]))
                                printed_answer = True
                            answer_parts.append(t)
                            print(colored(t, "white"), end="", flush=True)
                        continue

                    if et == "response.error": print(colored(f"\n[Stream error] {getattr(event, 'error', None)}", "red"))

                # final response + harvest files
                saved = _harvest_and_download_files(client, _as_dict(stream.get_final_response()), set())
                for p in saved: print(colored(f"Saved to: {p}", "blue"))
        except Exception as e:
            print(colored(f"[Streaming failed] {e}", "red"))

        print()
        final_answer = ("".join(answer_parts).strip()) or "(No text output returned)"
        history.append(("user", USER_INPUT)); history.append(("assistant", final_answer))

    print(colored("Goodbye!", "magenta"))


if __name__ == "__main__":
    main()



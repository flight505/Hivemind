import asyncio
import time
from typing import Dict, Any

from openai import AsyncOpenAI
from termcolor import colored


# =====================
# CONFIGURATION (ALL-CAPS)
# =====================
MODEL = "gpt-5"
REASONING_EFFORTS = ["low", "medium", "high"]
PROMPT = (
    "Write a very long, structured blog post about Large Language Models (LLMs). "
    "Cover: an introduction, historical context, core architectures, training data, "
    "tokenization, attention mechanisms, scaling laws, inference, prompting, safety, "
    "evaluation, real-world applications, limitations, open challenges, and a forward-looking conclusion. "
    "Use clear headings and readable paragraphs that are friendly to non-experts."
)
VERBOSITIES = ["low", "medium", "high"]
OUTPUT_FILENAME_PATTERN = "blog_verbosity-{verbosity}_reasoning-{effort}.txt"


async def extract_text_from_response(response: Any) -> str:
    """Best-effort extraction of text content from a Responses API result."""
    # Prefer the helper if present
    text = getattr(response, "output_text", None)
    if isinstance(text, str) and text.strip():
        return text

    # Fallback: walk structured content
    try:
        parts = []
        for item in getattr(response, "output", []) or []:
            for content in getattr(item, "content", []) or []:
                value = getattr(content, "text", None)
                if isinstance(value, str):
                    parts.append(value)
                elif isinstance(value, dict) and "value" in value:
                    parts.append(str(value["value"]))
        if parts:
            return "\n".join(parts)
    except Exception:
        pass

    # Final fallback: stringify the whole object
    return str(response)


async def generate_blog_with_verbosity_and_effort(
    client: AsyncOpenAI, verbosity: str, reasoning_effort: str
) -> Dict[str, Any]:
    start = time.perf_counter()
    print(colored(f"Starting generation (verbosity={verbosity}, effort={reasoning_effort})...", "cyan"))

    response = await client.responses.create(
        model=MODEL,
        input=PROMPT,
        reasoning={"effort": reasoning_effort},
        text={"verbosity": verbosity},
    )

    content_text = await extract_text_from_response(response)
    words = content_text.split()
    word_count = len(words)

    filename = OUTPUT_FILENAME_PATTERN.format(verbosity=verbosity, effort=reasoning_effort)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content_text)

    duration = time.perf_counter() - start
    print(colored(f"Finished (verbosity={verbosity}, effort={reasoning_effort}) in {duration:.2f}s, words={word_count}", "green"))

    return {
        "verbosity": verbosity,
        "effort": reasoning_effort,
        "duration_seconds": duration,
        "word_count": word_count,
        "file": filename,
    }


async def main() -> None:
    print(colored("Initializing async client and launching parallel generations...", "yellow"))
    client = AsyncOpenAI()

    tasks = [
        generate_blog_with_verbosity_and_effort(client, v, e)
        for v in VERBOSITIES
        for e in REASONING_EFFORTS
    ]
    results = await asyncio.gather(*tasks)

    # Report (pretty table)
    ordered_levels = ["low", "medium", "high"]
    results_sorted = sorted(
        results,
        key=lambda r: (ordered_levels.index(r["verbosity"]), ordered_levels.index(r["effort"]))
    )

    headers = ["Verbosity", "Reasoning", "Time (s)", "Words", "File"]
    rows = [
        [
            r["verbosity"],
            r["effort"],
            f"{r['duration_seconds']:.2f}",
            str(r["word_count"]),
            r["file"],
        ]
        for r in results_sorted
    ]

    col_widths = [
        max(len(headers[i]), max((len(row[i]) for row in rows), default=0))
        for i in range(len(headers))
    ]

    def fmt_row(cols, color=None, bold=False):
        pieces = []
        for i, col in enumerate(cols):
            text = col.ljust(col_widths[i])
            if color:
                text = colored(text, color, attrs=["bold"] if bold else None)
            pieces.append(text)
        return "  ".join(pieces)

    print(colored("\nGeneration Report (by verbosity x reasoning effort):", "magenta", attrs=["bold"]))
    print(fmt_row(headers, color="yellow", bold=True))
    print(colored("-" * (sum(col_widths) + 2 * (len(col_widths) - 1)), "blue"))

    for row in rows:
        # Color-code by verbosity
        color_map = {"low": "white", "medium": "cyan", "high": "green"}
        print(fmt_row(row, color=color_map.get(row[0], "white")))


if __name__ == "__main__":
    asyncio.run(main())
import os
import asyncio
import re

try:
	from termcolor import colored
except Exception:
	def colored(text, color=None, attrs=None):
		return text


# -----------------------------
# CONFIG (ALL CAPS)
# -----------------------------
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-5"
REASONING_EFFORT = "medium"
ENABLE_WEB_SEARCH = True
OUTPUT_JSON_PATH = "questions.json"
TOTAL_QUESTIONS = 3 # if None, the model will generate as many questions as necessary
SERVICE_TIER = "flex" # options include flex, dlfault, priority

# -----------------------------
# Pricing (Flex, USD)
# -----------------------------
GPT5_FLEX_INPUT_PRICE_PER_M_TOKENS_USD = 0.625
GPT5_FLEX_OUTPUT_PRICE_PER_M_TOKENS_USD = 5.00
GPT5_MINI_FLEX_INPUT_PRICE_PER_M_TOKENS_USD = 0.125
GPT5_MINI_FLEX_OUTPUT_PRICE_PER_M_TOKENS_USD = 1.00
# Web search (gpt-5, o-series): $10.00 / 1k calls
WEB_SEARCH_PRICE_PER_CALL_USD = 0.01


# -----------------------------
# ANSWERING CONFIG (ALL CAPS)
# -----------------------------
ANSWER_MODEL = "gpt-5"
ANSWER_ENABLE_WEB_SEARCH = True
ANSWER_REASONING_EFFORT = "medium"
ANSWER_SERVICE_TIER = "flex"
# markdown | text
ANSWER_OUTPUT_FORMAT = "markdown"
OUTPUT_DIR = "output"  # Will be overridden per run using topic/purpose/timeframe
ANSWER_MAX_CONCURRENCY = 100
ANSWER_REMOVE_CITATIONS = True
ANSWER_MAX_WEB_SEARCHES = 3


# Will be set from user input in main()
USER_TOPIC = None
USER_PURPOSE = None
USER_TIMEFRAME = None


# -----------------------------
# RUNTIME METRICS (GLOBAL TOTALS)
# -----------------------------
GEN_INPUT_TOKENS = 0
GEN_OUTPUT_TOKENS = 0
GEN_WEB_SEARCH_CALLS = 0
GEN_MODEL_COST_USD = 0.0
GEN_WEB_COST_USD = 0.0


# -----------------------------
# Logging helpers
# -----------------------------
def _log(prefix, message, color):
	print(colored(f"[{prefix}] {message}", color))


def info(message):
	_log("INFO", message, "cyan")


def success(message):
	_log("OK", message, "green")


def warn(message):
	_log("WARN", message, "yellow")


def error(message):
	_log("ERROR", message, "red")


def usage_log(message):
	_log("USAGE", message, "magenta")


def cost_log(message):
	_log("COST", message, "blue")


def search_log(message):
	_log("SEARCH", message, "white")


def final_total_log(total_message: str):
	"""Print a very prominent, distinct total summary banner."""
	line = "=" * 72
	print(colored(line, "green"))
	print(colored(total_message, "green", attrs=["bold"]))
	print(colored(line, "green"))


def remove_citations_from_text(text: str) -> str:
	"""Remove inline citations and URLs from markdown/text while keeping core content.

	Rules:
	- Replace markdown links [label](https://url) with just 'label'
	- Drop parenthetical groups that contain http/https links or bracketed domains
	- Remove bracket-only domains like [reuters.com]
	- Remove bare URLs (http/https/www)

	Whitespace and newlines are preserved to avoid breaking Markdown structure.
	"""
	if not isinstance(text, str) or not text:
		return text

	clean = text
	# Replace markdown links with their label only
	clean = re.sub(r"\[([^\]]+)\]\((?:https?://|www\.)[^)]+\)", r"\1", clean)
	# Remove bracket-only domains or bracketed URLs
	clean = re.sub(r"\[(?:https?://|www\.)?[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\]\s)]*)?\]", "", clean)
	# Remove parenthetical groups containing URLs or bracketed domains
	clean = re.sub(r"\([^)]*(?:https?://|www\.)[^)]*\)", "", clean)
	clean = re.sub(r"\([^)]*\[[^\]]+\.[^\]]+\][^)]*\)", "", clean)
	# Remove bare URLs
	clean = re.sub(r"(?:https?://|www\.)\S+", "", clean)
	# Light tidy: collapse multiple spaces but preserve newlines
	clean = re.sub(r"[ \t]{2,}", " ", clean)
	clean = re.sub(r"[ \t]+\n", "\n", clean)
	return clean.strip()


def sanitize_simple(name: str) -> str:
	"""Sanitize a user-provided string for safe filesystem usage.

	- Lowercase
	- Remove characters other than letters, numbers, dash, underscore and space
	- Collapse whitespace to single hyphens
	- Trim to a reasonable length
	"""
	if not isinstance(name, str):
		return ""
	name = name.strip().lower()
	name = re.sub(r"[^a-z0-9\-_\s]", "", name)
	name = re.sub(r"\s+", "-", name)
	return name[:120]


def build_run_output_dir(topic: str, purpose: str, timeframe: str) -> str:
	parts = []
	if topic:
		parts.append(sanitize_simple(topic))
	if purpose:
		parts.append(sanitize_simple(purpose))
	if timeframe:
		parts.append(sanitize_simple(timeframe))
	dir_name = "-".join([p for p in parts if p]) or "output"
	return dir_name


# -----------------------------
# Prompt/input construction
# -----------------------------
def build_input(topic, purpose, timeframe):
	return (
		"You are a context engineer. Produce fundamental, domain-centric research questions that, when answered, yield deep insight for the stated purpose.\n"
		"- Input may be a topic OR a user question. If it is a question, treat it as the focal inquiry and generate the foundational research questions required to rigorously answer it.\n"
		"- Questions must target the SUBJECT MATTER, not the user's knowledge or preferences.\n"
		"- Avoid second-person wording entirely (no 'you', 'your'). Exclude forms like 'Do you understand...?', 'How familiar are you...?'\n"
		"- Prefer objective WHAT/HOW/WHY/WHO/WHEN/WHERE formulations.\n"
		"- Create AS MANY questions as necessary to remove all ambiguity, with concrete and verifiable angles (definitions, mechanisms, data, actors, timelines, causality, constraints, risks, trade-offs, and recent developments).\n"
		# "- Use up-to-date information; rely on web search where recency matters"
		" almost always perform as many web searches as necessary to better inform yourself about the questions needed to be asked"
		"- Do NOT answer the questions; output questions only.\n"
		"- Design a custom set of sections that best fits the topic and purpose; be creative and robust.\n"
		"- Sections should be non-overlapping, meaningful, and cover the space comprehensively without redundancy.\n"
		"- You MAY freely create, rename, merge, or split sections to reflect how the domain is actually structured.\n"
		"- Consider multi-angle coverage (concepts, mechanisms, data, actors, timelines, constraints, risks, trade-offs, implementation, evaluation, and recency).\n"
		"- Use only sections that add real value; omit boilerplate or empty sections.\n"
		"- Optional palette to draw inspiration from (choose only what's needed): Purpose Alignment, Foundations, Key Concepts, Actors/Stakeholders, History/Timeline, Data & Evidence, Technical Details, Economics/Business, Policy/Regulation, Risks/Limitations, Controversies/Open Problems, Recent Developments, Practical How-To, Next Steps.\n"
		"- These are examples only; select any section taxonomy that is most appropriate for the topic and purpose.\n"
		"- Include clarifying follow-ups where the answer depends on context.\n"
		"- Timeframe handling: If a timeframe is provided, every question MUST be truthful to that timeframe (e.g., 'last 6 months', '2022', 'from 1870 to 1975', 'during the Great Depression'). If no timeframe is provided, conduct general research with no date constraint.\n"
		"- Return STRICT JSON only, with this schema: {\n"
		"  \"topic\": string, \n"
		"  \"purpose\": string, \n"
		"  \"sections\": [ { \"name\": string, \"questions\": [string, ...] }, ... ]\n"
		"}. No commentary. No markdown.\n\n"
		f"topic_or_question: {topic}\n"
		f"purpose: {purpose}\n"
		+ (f"timeframe: {timeframe}\n" if timeframe else "")
	)


# -----------------------------
# OpenAI call
# -----------------------------
def extract_text(response):
	try:
		return response.output_text
	except Exception:
		pass

	try:
		response_data = response.model_dump()
	except Exception:
		try:
			response_data = response.to_dict()
		except Exception:
			response_data = None

	def find_text(node):
		if isinstance(node, dict):
			# SDK frequently nests content blocks with {text: {value: "..."}}
			text_block = node.get("text")
			if isinstance(text_block, dict) and "value" in text_block:
				return text_block.get("value")
			content = node.get("content")
			if isinstance(content, list):
				for item in content:
					found = find_text(item)
					if found:
						return found
			for value in node.values():
				found = find_text(value)
				if found:
					return found
		elif isinstance(node, list):
			for item in node:
				found = find_text(item)
				if found:
					return found
		elif isinstance(node, str):
			return node
		return None

	if response_data is not None:
		found_text = find_text(response_data)
		if found_text:
			return found_text

	return ""


def generate_questions(topic, purpose):
	if not OPENAI_API_KEY:
		error("OPENAI_API_KEY is not set in the environment.")
		raise SystemExit(1)

	from openai import OpenAI
	client = OpenAI(api_key=OPENAI_API_KEY)

	info(f"Asking GPT-5 with {REASONING_EFFORT} reasoning and web search to enumerate purpose-focused questions...")
	user_input = build_input(
		topic,
		purpose,
		USER_TIMEFRAME if USER_TIMEFRAME else None,
	)
	if TOTAL_QUESTIONS is not None:
		user_input += f"Aim to produce exactly {TOTAL_QUESTIONS} total questions across sections; keep balance and avoid redundancy.\n"

	kwargs = {
		"model": MODEL,
		"input": user_input,
		"reasoning": {"effort": REASONING_EFFORT},
		"service_tier": SERVICE_TIER,
	}
	if ENABLE_WEB_SEARCH:
		kwargs["tools"] = [{"type": "web_search_preview"}]

	try:
		response = client.responses.create(**kwargs)
		# Minimal telemetry: print token usage if available, then count web search calls by scanning output
		try:
			usage = getattr(response, "usage", None)
			input_tokens = output_tokens = total_tokens = None
			if isinstance(usage, dict):
				input_tokens = usage.get("input_tokens")
				output_tokens = usage.get("output_tokens")
				total_tokens = usage.get("total_tokens")
			elif usage is not None:
				input_tokens = getattr(usage, "input_tokens", None)
				output_tokens = getattr(usage, "output_tokens", None)
				total_tokens = getattr(usage, "total_tokens", None)
			if any(v is not None for v in (input_tokens, output_tokens, total_tokens)):
				usage_log(f"Tokens - input: {input_tokens}, output: {output_tokens}, total: {total_tokens}")
				# Accumulate generation totals
				global GEN_INPUT_TOKENS, GEN_OUTPUT_TOKENS
				GEN_INPUT_TOKENS += input_tokens or 0
				GEN_OUTPUT_TOKENS += output_tokens or 0

			# Simple web search call count: look for items with type == 'web_search_call'
			response_data = None
			try:
				response_data = response.model_dump()
			except Exception:
				try:
					response_data = response.to_dict()
				except Exception:
					pass
			output_items = None
			if isinstance(response_data, dict):
				output_items = response_data.get("output")
			if output_items is None:
				output_items = getattr(response, "output", None)
			if isinstance(output_items, list):
				web_search_call_count = sum(1 for item in output_items if isinstance(item, dict) and item.get("type") == "web_search_call")
				search_log(f"Web search tool calls: {web_search_call_count}")
				global GEN_WEB_SEARCH_CALLS
				GEN_WEB_SEARCH_CALLS += web_search_call_count

			# If model is GPT-5 or GPT-5 Mini on flex tier, estimate cost
			if SERVICE_TIER == "flex" and isinstance(MODEL, str) and (MODEL.startswith("gpt-5-mini") or MODEL == "gpt-5"):
				usd_per_m_input = GPT5_MINI_FLEX_INPUT_PRICE_PER_M_TOKENS_USD if MODEL.startswith("gpt-5-mini") else GPT5_FLEX_INPUT_PRICE_PER_M_TOKENS_USD
				usd_per_m_output = GPT5_MINI_FLEX_OUTPUT_PRICE_PER_M_TOKENS_USD if MODEL.startswith("gpt-5-mini") else GPT5_FLEX_OUTPUT_PRICE_PER_M_TOKENS_USD
				input_cost_usd = (input_tokens or 0) / 1_000_000 * usd_per_m_input
				output_cost_usd = (output_tokens or 0) / 1_000_000 * usd_per_m_output
				web_search_cost_usd = (web_search_call_count if isinstance(web_search_call_count, int) else 0) * WEB_SEARCH_PRICE_PER_CALL_USD
				total_cost_usd = input_cost_usd + output_cost_usd + web_search_cost_usd
				cost_log(f"Estimated cost (flex): model=${total_cost_usd:.6f} (input=${input_cost_usd:.6f}, output=${output_cost_usd:.6f}), web=${web_search_cost_usd:.6f}")
				# Accumulate generation costs
				global GEN_MODEL_COST_USD, GEN_WEB_COST_USD
				GEN_MODEL_COST_USD += input_cost_usd + output_cost_usd
				GEN_WEB_COST_USD += web_search_cost_usd
		except Exception:
			pass
		text = extract_text(response).strip()
		if ANSWER_REMOVE_CITATIONS:
			text = remove_citations_from_text(text)
		return text
	except Exception as exc:
		error(f"OpenAI request failed: {exc}")
		return ""


async def async_generate_answers(topic, purpose, timeframe, sections_obj):
	"""Generate answers for each question in parallel using AsyncOpenAI.

	Saves per-section and per-question outputs under OUTPUT_DIR, and
	returns a combined markdown string of all answers.
	"""
	from openai import AsyncOpenAI

	client = AsyncOpenAI(api_key=OPENAI_API_KEY)

	# Totals for end-of-run reporting
	total_input_tokens = 0
	total_output_tokens = 0
	total_model_cost_usd = 0.0
	total_web_cost_usd = 0.0
	total_web_search_calls = 0

	# Build and ensure per-run output directory
	global OUTPUT_DIR
	OUTPUT_DIR = build_run_output_dir(topic, purpose, timeframe)
	os.makedirs(OUTPUT_DIR, exist_ok=True)

	def sanitize_filename(name: str) -> str:
		name = name.strip().lower()
		name = re.sub(r"[^a-z0-9\-_\s]", "", name)
		name = re.sub(r"\s+", "-", name)
		return name[:50] if len(name) > 50 else name

	def sanitize_dirname(name: str) -> str:
		return sanitize_filename(name)

	def build_answer_prompt(section_name: str, question: str) -> str:
		format_note = (
			"Provide the answer in Markdown with headings, bullet points, code blocks where useful."
			if ANSWER_OUTPUT_FORMAT == "markdown"
			else "Provide a concise plain text answer."
		)
		return (
			f"You are a rigorous research assistant. Answer the question comprehensively and accurately.\n"
			f"- Use recent and trustworthy sources when applicable, and prefer primary data.\n"
			f"- Use web search when needed; aim to use at most {ANSWER_MAX_WEB_SEARCHES} tool calls. these will be targeted searches to inform the answer. You are not allowed to use more than {ANSWER_MAX_WEB_SEARCHES} tool calls.\n"
			f"- You must never use any more than {ANSWER_MAX_WEB_SEARCHES} tool calls. THIS IS A HARD LIMIT.\n"
			f"- Explain assumptions, uncertainties, and limitations.\n"
			f"- Structure the answer for skimmability with clear sections.\n"
			f"- Ensure the final output is as detailed as possible, covering all necessary information to fully fulfill the question, especially important and essential information from web searches if performed.\n"
			f"- Tailor the depth to the stated purpose: {purpose or 'general understanding'}.\n"
			f"- Timeframe: {timeframe or 'no specific timeframe'}. Ensure accuracy to the timeframe if provided.\n"
			f"- {format_note}\n\n"
			f"Section: {section_name}\n"
			f"Question: {question}\n"
		)

	async def answer_one(section_name: str, question: str):
		nonlocal total_input_tokens, total_output_tokens, total_model_cost_usd, total_web_cost_usd, total_web_search_calls
		user_input = build_answer_prompt(section_name, question)
		kwargs = {
			"model": ANSWER_MODEL,
			"input": user_input,
			"reasoning": {"effort": ANSWER_REASONING_EFFORT},
			"service_tier": ANSWER_SERVICE_TIER,
		}
		if ANSWER_ENABLE_WEB_SEARCH:
			kwargs["tools"] = [{"type": "web_search_preview"}]

		info(f"Answering: [{section_name}] {question[:60]}...")
		response = await client.responses.create(**kwargs)
		text = extract_text(response).strip()

		# Count tokens and web search calls for this answer
		usage = getattr(response, "usage", None)
		input_tokens = output_tokens = total_tokens = None
		if isinstance(usage, dict):
			input_tokens = usage.get("input_tokens")
			output_tokens = usage.get("output_tokens")
			total_tokens = usage.get("total_tokens")
		elif usage is not None:
			input_tokens = getattr(usage, "input_tokens", None)
			output_tokens = getattr(usage, "output_tokens", None)
			total_tokens = getattr(usage, "total_tokens", None)

		response_data = None
		try:
			response_data = response.model_dump()
		except Exception:
			try:
				response_data = response.to_dict()
			except Exception:
				pass
		output_items = None
		if isinstance(response_data, dict):
			output_items = response_data.get("output")
		if output_items is None:
			output_items = getattr(response, "output", None)
		web_search_call_count = 0
		if isinstance(output_items, list):
			web_search_call_count = sum(1 for item in output_items if isinstance(item, dict) and item.get("type") == "web_search_call")

		# Report web search calls for this answer
		search_log(f"Web search tool calls: {web_search_call_count}")

		# Cost estimation only for GPT-5 family on flex
		if ANSWER_SERVICE_TIER == "flex" and isinstance(ANSWER_MODEL, str) and (ANSWER_MODEL.startswith("gpt-5-mini") or ANSWER_MODEL == "gpt-5"):
			usd_per_m_input = GPT5_MINI_FLEX_INPUT_PRICE_PER_M_TOKENS_USD if ANSWER_MODEL.startswith("gpt-5-mini") else GPT5_FLEX_INPUT_PRICE_PER_M_TOKENS_USD
			usd_per_m_output = GPT5_MINI_FLEX_OUTPUT_PRICE_PER_M_TOKENS_USD if ANSWER_MODEL.startswith("gpt-5-mini") else GPT5_FLEX_OUTPUT_PRICE_PER_M_TOKENS_USD
			input_cost_usd = (input_tokens or 0) / 1_000_000 * usd_per_m_input
			output_cost_usd = (output_tokens or 0) / 1_000_000 * usd_per_m_output
			web_search_cost_usd = web_search_call_count * WEB_SEARCH_PRICE_PER_CALL_USD
			total_cost_usd = input_cost_usd + output_cost_usd + web_search_cost_usd
			# Per-call usage and cost
			usage_log(f"Tokens: input={input_tokens}, output={output_tokens}, total={total_tokens}")
			cost_log(f"Cost: model=${total_cost_usd:.6f} (input=${input_cost_usd:.6f}, output=${output_cost_usd:.6f}), web=${web_search_cost_usd:.6f}")
			# Accumulate totals
			total_input_tokens += input_tokens or 0
			total_output_tokens += output_tokens or 0
			total_model_cost_usd += input_cost_usd + output_cost_usd
			total_web_cost_usd += web_search_cost_usd

		# Accumulate web search calls regardless of cost calc path
		total_web_search_calls += web_search_call_count

		# Save to disk
		section_dir = os.path.join(OUTPUT_DIR, sanitize_dirname(section_name))
		os.makedirs(section_dir, exist_ok=True)
		filename = sanitize_filename(question) or "question"
		ext = ".md" if ANSWER_OUTPUT_FORMAT == "markdown" else ".txt"
		path = os.path.join(section_dir, f"{filename}{ext}")
		with open(path, "w", encoding="utf-8") as f:
			f.write(text)
		return section_name, question, text

	# Build tasks
	sections = sections_obj if isinstance(sections_obj, list) else sections_obj.get("sections", [])
	tasks = []
	for section in sections:
		section_name = section.get("name", "Section")
		questions = section.get("questions", [])
		for q in questions:
			if isinstance(q, str) and q.strip():
				tasks.append(answer_one(section_name, q.strip()))

	# Concurrency control
	semaphore = asyncio.Semaphore(ANSWER_MAX_CONCURRENCY)

	async def sem_task(coro):
		async with semaphore:
			return await coro

	results = await asyncio.gather(*(sem_task(t) for t in tasks), return_exceptions=False)

	# Combine into a single markdown or text
	blocks = []
	for section_name, question, text in results:
		block = None
		if ANSWER_OUTPUT_FORMAT == "markdown":
			block = f"## {section_name}\n\n### {question}\n\n{text.strip()}\n"
		else:
			block = f"{section_name}\n\n{question}\n\n{text.strip()}\n"
		blocks.append(block)
	combined = "\n\n".join(blocks)
	combined_name = os.path.join(OUTPUT_DIR, "combined_answers.md" if ANSWER_OUTPUT_FORMAT == "markdown" else "combined_answers.txt")
	with open(combined_name, "w", encoding="utf-8") as f:
		# Optionally strip citations in the combined file as well without disturbing markdown structure
		final_text = remove_citations_from_text(combined) if ANSWER_REMOVE_CITATIONS else combined
		f.write(final_text)

	# Final totals (include question generation phase if applicable)
	if ANSWER_SERVICE_TIER == "flex" and isinstance(ANSWER_MODEL, str) and (ANSWER_MODEL.startswith("gpt-5-mini") or ANSWER_MODEL == "gpt-5"):
		all_input_tokens = GEN_INPUT_TOKENS + total_input_tokens
		all_output_tokens = GEN_OUTPUT_TOKENS + total_output_tokens
		all_web_calls = GEN_WEB_SEARCH_CALLS + total_web_search_calls
		all_model_cost = GEN_MODEL_COST_USD + total_model_cost_usd
		all_web_cost = GEN_WEB_COST_USD + total_web_cost_usd
		all_total_cost = all_model_cost + all_web_cost

		usage_log(f"TOTAL tokens: gen(input={GEN_INPUT_TOKENS}, output={GEN_OUTPUT_TOKENS}) + ans(input={total_input_tokens}, output={total_output_tokens}) => input={all_input_tokens}, output={all_output_tokens}, total={all_input_tokens + all_output_tokens}")
		search_log(f"TOTAL web search calls: gen={GEN_WEB_SEARCH_CALLS}, ans={total_web_search_calls}, all={all_web_calls}")
		cost_log(f"TOTAL cost: gen(model=${GEN_MODEL_COST_USD:.6f}, web=${GEN_WEB_COST_USD:.6f}) + ans(model=${total_model_cost_usd:.6f}, web=${total_web_cost_usd:.6f}) => all(model=${all_model_cost:.6f}, web=${all_web_cost:.6f}, all-in=${all_total_cost:.6f})")
		final_total_log(f"ALL-IN TOTAL COST: ${all_total_cost:.6f} (model=${all_model_cost:.6f} + web=${all_web_cost:.6f})")

	return combined_name


def _fallback_text_to_json(topic, purpose, text):
	lines = [ln.strip(" \t-•*\u2022") for ln in text.splitlines()]
	lines = [ln for ln in lines if ln]
	return {
		"topic": topic,
		"purpose": purpose,
		"sections": [
			{"name": "Questions", "questions": lines}
		]
	}


def save_questions_json(obj, path):
	import json
	with open(path, "w", encoding="utf-8") as f:
		json.dump(obj, f, ensure_ascii=False, indent=2)


# -----------------------------
# Entry point
# -----------------------------
def main():
	global USER_TOPIC, USER_PURPOSE, USER_TIMEFRAME
	if TOTAL_QUESTIONS is None:
		info("The model will generate as many questions as necessary. You can change TOTAL_QUESTIONS in the script to control the count.")
	else:
		info(f"The model will aim to produce exactly {TOTAL_QUESTIONS} total questions. You can change TOTAL_QUESTIONS in the script to adjust.")
	info("Enter a topic OR a specific question.")
	if USER_TOPIC is None:
		USER_TOPIC = input("> ").strip()
	if not USER_TOPIC:
		warn("No topic entered. Exiting.")
		return

	# No need to detect if it's a question; the prompt handles both.

	info("What is the purpose of this research? (e.g., write an explainer, make an investment, build a feature, debate, policy brief) (press Enter to skip)")
	if USER_PURPOSE is None:
		USER_PURPOSE = input("> ").strip()
	if not USER_PURPOSE:
		warn("No purpose provided. Proceeding without explicit focus.")
		USER_PURPOSE = ""

	info("Optional timeframe (press Enter to skip). Examples: 'last 6 months', '2022', 'from 1870 to 1975', 'during the Great Depression'")
	if USER_TIMEFRAME is None:
		USER_TIMEFRAME = input("> ").strip()
	raw = generate_questions(USER_TOPIC, USER_PURPOSE)
	if not raw:
		warn("Received empty output.")
		return

	# Try parse JSON, else fallback
	import json
	try:
		obj = json.loads(raw)
	except Exception:
		obj = _fallback_text_to_json(USER_TOPIC, USER_PURPOSE, raw)

	# Save questions.json under the per-run output folder
	run_dir_for_json = build_run_output_dir(USER_TOPIC, USER_PURPOSE, USER_TIMEFRAME)
	os.makedirs(run_dir_for_json, exist_ok=True)
	json_path = os.path.join(run_dir_for_json, os.path.basename(OUTPUT_JSON_PATH))
	save_questions_json(obj, json_path)
	success(f"Saved questions JSON -> {json_path}")

	# Tally and print counts
	sections = obj.get("sections", []) if isinstance(obj, dict) else []
	num_sections = len(sections)
	total_qs = 0
	for sec in sections:
		qs = sec.get("questions", []) if isinstance(sec, dict) else []
		if isinstance(qs, list):
			total_qs += len(qs)
	info(f"Tally: {num_sections} sections, {total_qs} total questions")

	# Ask user if they want to proceed to answering
	planned_output_dir = build_run_output_dir(USER_TOPIC, USER_PURPOSE, USER_TIMEFRAME)
	info(
		f"Ready to generate answers in parallel using AsyncOpenAI. This will:\n"
		f"- create a run folder '{planned_output_dir}' based on topic/purpose/timeframe\n"
		f"- write each section's answers into its own subfolder\n"
		f"- save each question's answer as a separate file\n"
		f"- create one combined file with all answers.\n"
		"Proceed? (y/N)"
	)
	confirm = input("> ").strip().lower()
	if confirm in ("y", "yes"):
		info("Starting parallel answering...")
		combined_path = asyncio.run(async_generate_answers(USER_TOPIC, USER_PURPOSE, USER_TIMEFRAME, obj))
		success(f"Answers generated. Combined file -> {combined_path}")
	else:
		warn("Skipping answer generation.")


if __name__ == "__main__":
	main()



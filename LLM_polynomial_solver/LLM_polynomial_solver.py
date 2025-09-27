import random
import re
import asyncio
import json
import sympy as sp
from termcolor import colored
from openai import AsyncOpenAI
import os
from datetime import datetime

# Configuration variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = "openai/gpt-5-mini"
NUM_POLYNOMIALS = 5
DEGREE = 14  # Degree of polynomials to generate (2, 3, 4, etc.)
REASONING_EFFORT = "high"

def setup_openai_client():
    """Set up the OpenAI client for OpenRouter"""
    return AsyncOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
    )

def generate_random_polynomial():
    """
    Generate a random polynomial of specified degree that is factorable over the rationals
    Returns both the polynomial and its factored form
    """
    x = sp.symbols('x')

    # Keep trying until we get a polynomial that factors nicely
    while True:
        # Generate rational roots (integers from -10 to 10, avoid duplicates)
        # Use a larger range to ensure we can generate distinct roots for high degrees
        root_range = max(10, DEGREE + 2)  # Ensure enough possible roots
        roots = []
        for i in range(DEGREE):  # DEGREE roots for degree DEGREE polynomial
            root = random.randint(-root_range, root_range)
            # Avoid duplicate roots and zero (to avoid x terms in factorization)
            while root in roots or root == 0:
                root = random.randint(-root_range, root_range)
            roots.append(root)

        # Create factors: (x - r1)(x - r2)...(x - rn)
        factors = [x - root for root in roots]

        # Multiply the factors to get the expanded polynomial
        expanded = sp.expand(sp.prod(factors))

        # Create the expected factored form manually (not relying on sympy.factor)
        # Keep original order for now - we'll handle ordering in validation

        # Create the expected factorization string
        factor_terms = []
        for root in roots:
            if root == 0:
                factor_terms.append("x")
            elif root > 0:
                factor_terms.append(f"(x-{root})")
            else:
                factor_terms.append(f"(x+{abs(root)})")

        # Join the factors
        expected_factorization = "".join(factor_terms)

        # Debug: Print roots to verify they're different
        print(colored(f"Debug - Generated roots: {sorted(roots)}", "cyan"))

        # Get coefficients for display (degree + 1 coefficients)
        coeffs = [expanded.coeff(x, i) for i in range(DEGREE + 1)]

        # Verify the polynomial has the correct degree (has x^DEGREE term)
        if coeffs[0] != 0:  # x^DEGREE coefficient should not be zero
            return expanded, expected_factorization, coeffs

        # If we got a polynomial with wrong degree, try again with new roots

def parse_llm_factorization(response):
    """
    Parse LLM's factorization response and extract factors
    Handles various polynomial degrees and formats
    """
    if not response:
        return None

    # Clean up the response - remove extra whitespace and newlines
    response = re.sub(r'\s+', '', response.strip())

    # Check for polynomial factorization patterns of various degrees
    patterns = [
        # Multiple factors: (x+a)(x+b)... with optional leading x
        r'^(?:x)?(?:\(x[+-]?\d+\))+$',
        # x followed by factors: x(x+a)(x+b)...
        r'^x(?:\(x[+-]?\d+\))+$',
        # Just factors: (x+a)(x+b)...
        r'^(?:\(x[+-]?\d+\))+$',
    ]

    for pattern in patterns:
        if re.match(pattern, response):
            return response  # Return the cleaned response if it matches expected format

    print(colored(f"Response format not recognized: {repr(response)}", "red"))
    return response  # Return as-is if no pattern matches

def validate_factorization(llm_response, correct_factors):
    """
    Validate if LLM's factorization matches the correct one
    """
    try:
        # Parse LLM's response first
        llm_cleaned = parse_llm_factorization(llm_response)
        if not llm_cleaned:
            return False

        # Normalize both expressions to remove spaces and standardize format
        def normalize_expression(expr_str):
            """Normalize expression string for comparison"""
            # Remove all spaces
            expr_str = re.sub(r'\s+', '', expr_str)
            # Ensure consistent ordering of terms
            return expr_str

        expected_normalized = normalize_expression(str(correct_factors))
        llm_normalized = normalize_expression(llm_cleaned)

        # First try factor comparison (most robust for ordering differences)
        def extract_factors(expr):
            """Extract individual factors from expression"""
            factors = re.findall(r'\(x[+-]?\d+\)|x', expr)
            return sorted(factors)  # Sort for consistent comparison

        expected_factors = extract_factors(expected_normalized)
        llm_factors = extract_factors(llm_normalized)

        if expected_factors == llm_factors:
            print(colored(f"Debug - Factor match: {expected_factors}", "green"))
            return True

        # Simple string comparison (for exact matches)
        if expected_normalized == llm_normalized:
            print(colored(f"Debug - Direct match: {expected_normalized} == {llm_normalized}", "green"))
            return True

        # If both fail, try mathematical equivalence
        try:
            x = sp.Symbol('x')  # Use Symbol instead of symbols for clarity

            # Convert to sympy expressions carefully
            correct_expr = sp.sympify(expected_normalized, locals={'x': x})
            llm_expr = sp.sympify(llm_normalized, locals={'x': x})

            # Expand both expressions
            correct_expanded = sp.expand(correct_expr)
            llm_expanded = sp.expand(llm_expr)

            # Check if they're mathematically equivalent
            difference = sp.simplify(correct_expanded - llm_expanded)
            is_equivalent = difference == 0

            # Debug output
            print(colored(f"Debug - Expected: {expected_normalized}", "blue"))
            print(colored(f"Debug - LLM raw: {llm_response}", "cyan"))
            print(colored(f"Debug - LLM cleaned: {llm_normalized}", "cyan"))
            print(colored(f"Debug - Correct expanded: {correct_expanded}", "blue"))
            print(colored(f"Debug - LLM expanded: {llm_expanded}", "cyan"))
            print(colored(f"Debug - Difference: {difference}", "yellow"))
            print(colored(f"Debug - Equivalent: {is_equivalent}", "green" if is_equivalent else "red"))

            return is_equivalent

        except Exception as math_error:
            print(colored(f"Math comparison failed: {math_error}", "red"))
            print(colored(f"No valid comparison method worked", "red"))
            return False

    except Exception as e:
        print(colored(f"Validation error: {e}", "red"))
        return False

async def ask_llm_factorization(client, polynomial_expr):
    """Send a polynomial factorization question to the LLM"""
    try:
        degree_word = {2: "quadratic", 3: "cubic", 4: "quartic", 5: "quintic"}.get(DEGREE, f"degree {DEGREE}")
        question = f"Factor the following {degree_word} polynomial completely: {polynomial_expr}"
        print(colored(f"Asking: {question}", "cyan"))

        # Very specific prompt with exact format requirements

        prompt = f"""Factor this {degree_word} polynomial completely over the rationals: {polynomial_expr}

🚫 ABSOLUTELY FORBIDDEN: Do NOT use ANY formulas, shortcuts, or memorized methods!
❌ NO sum/difference of cubes formula
❌ NO difference of squares formula
❌ NO algebraic identities
❌ NO memorized patterns or rules
❌ NO shortcuts of any kind

✅ REQUIRED: Use ONLY basic algebraic methods:
- Test rational roots by trial and error
- Use polynomial long division if needed
- Group terms when applicable
- Work through the algebra step by step

⚠️ CRITICAL: If you use ANY formula or shortcut, your answer will be WRONG!

RESPONSE FORMAT: Respond with ONLY the factored form using EXACTLY one of these formats:
Format 1: (x+a)(x+b)... - multiple factors
Format 2: x(x+a)(x+b)... - leading x coefficient
Format 3: (x+a)(x+b)... - mixed coefficients

Rules:
- No spaces between factors
- No * symbols for multiplication
- No explanation or extra text
- Only parentheses, x, numbers, +, -
- Use negative signs correctly: (x-1) not (x+-1)

Correct examples:
(x-1)(x+2)(x-3)
x(x-1)(x+2)
(x-2)(x+1)(x-3)

Factor: {polynomial_expr}"""

        completion = await client.chat.completions.create(
            model=MODEL_NAME,
            reasoning_effort=REASONING_EFFORT,
            messages=[
                {
                    "role": "system",
                    "content": """CRITICAL FACTORIZATION RULES - YOU MUST FOLLOW THESE EXACTLY:

🚫 ABSOLUTELY FORBIDDEN: Do NOT use ANY shortcut formulas or memorized methods:
❌ DO NOT use sum/difference of cubes: (a³±b³)=(a±b)(a²∓ab+b²)
❌ DO NOT use difference of squares: (a²-b²)=(a-b)(a+b)
❌ DO NOT use any memorized factorization formulas
❌ DO NOT use any algebraic identities or shortcuts
❌ DO NOT use any formula-based methods whatsoever
❌ DO NOT apply any "rules" or "patterns" you've memorized

✅ REQUIRED: Only use basic algebraic manipulation:
- Trial and error with rational roots
- Long division if needed
- Basic polynomial division
- Grouping when applicable
- Only fundamental algebraic operations

⚠️ WARNING: If you use ANY formula or shortcut, your answer will be marked WRONG.
You MUST factor by working through the algebra step by step."""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        response = completion.choices[0].message.content
        print(colored(f"Raw response: {repr(response)}", "cyan"))
        return response
    except Exception as e:
        print(colored(f"Error asking question: {e}", "red"))
        return None

async def process_single_polynomial(client, poly_num, expanded, correct_factors, coeffs):
    """Process a single polynomial asynchronously"""
    print(colored(f"\nPolynomial {poly_num}:", "yellow"))
    print(colored(f"Polynomial: {expanded}", "green"))
    print(colored(f"Coefficients: {coeffs}", "blue"))
    print(colored(f"Correct factors: {correct_factors}", "magenta"))

    # Ask LLM to factor it
    llm_response = await ask_llm_factorization(client, expanded)

    if llm_response:
        print(colored(f"LLM Response: {llm_response}", "cyan"))

        # Validate the answer
        is_correct = validate_factorization(llm_response, correct_factors)

        status = "✓ CORRECT" if is_correct else "✗ WRONG"
        color = "green" if is_correct else "red"

        print(colored(f"Validation: {status}", color))

        return {
            "polynomial_number": poly_num,
            "expanded_form": str(expanded),
            "coefficients": [str(coeff) for coeff in coeffs],
            "correct_factors": str(correct_factors),
            "llm_response": llm_response,
            "is_correct": is_correct
        }
    else:
        print(colored("No response from LLM", "red"))
        return {
            "polynomial_number": poly_num,
            "expanded_form": str(expanded),
            "coefficients": [str(coeff) for coeff in coeffs],
            "correct_factors": str(correct_factors),
            "llm_response": None,
            "is_correct": False
        }

def analyze_results(results):
    """Analyze the results and provide statistics"""
    total_polynomials = len(results)
    correct_answers = sum(1 for result in results if result["is_correct"])
    accuracy = (correct_answers / total_polynomials) * 100 if total_polynomials > 0 else 0

    print(colored(f"\n{'='*60}", "cyan"))
    print(colored("ANALYSIS RESULTS", "cyan"))
    print(colored(f"{'='*60}", "cyan"))
    print(colored(f"Total Polynomials: {total_polynomials}", "yellow"))
    print(colored(f"Correct Factorizations: {correct_answers}", "green"))
    print(colored(f"Accuracy: {accuracy:.1f}%", "blue"))

    if correct_answers < total_polynomials:
        print(colored("\nINCORRECT FACTORIZATIONS:", "red"))
        for result in results:
            if not result["is_correct"]:
                print(colored(f"P{result['polynomial_number']}: {result['expanded_form']}", "red"))

def save_to_json(results, filename="polynomial_results.json"):
    """Save results to JSON file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"polynomial_results_{timestamp}.json"

    # Create summary stats
    total = len(results)
    correct = sum(1 for r in results if r["is_correct"])
    accuracy = (correct / total) * 100 if total > 0 else 0

    data = {
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "total_polynomials": total,
            "correct_answers": correct,
            "accuracy": round(accuracy, 2),
            "model": MODEL_NAME
        },
        "results": results
    }

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(colored(f"\nResults saved to: {filename}", "green"))
    return filename

async def main():
    """Main function to run polynomial factorization testing"""
    print(colored("Setting up OpenRouter client...", "green"))
    degree_word = {2: "quadratic", 3: "cubic", 4: "quartic", 5: "quintic"}.get(DEGREE, f"degree {DEGREE}")
    print(colored(f"Generating random {degree_word} polynomials...", "green"))

    # Check if API key is set
    if not OPENROUTER_API_KEY or OPENROUTER_API_KEY == "<OPENROUTER_API_KEY>":
        print(colored("ERROR: Please set your OPENROUTER_API_KEY environment variable!", "red"))
        return

    client = setup_openai_client()

    print(colored(f"\nGenerating {NUM_POLYNOMIALS} random {degree_word} polynomials...", "green"))

    # Generate all polynomials first
    polynomials_data = []
    for i in range(NUM_POLYNOMIALS):
        expanded, correct_factors, coeffs = generate_random_polynomial()
        polynomials_data.append((i+1, expanded, correct_factors, coeffs))

    print(colored(f"\nAsking LLM to factor {NUM_POLYNOMIALS} polynomials in parallel...", "green"))
    print(colored("="*80, "cyan"))

    # Create async tasks for all polynomials
    tasks = [
        process_single_polynomial(client, poly_num, expanded, correct_factors, coeffs)
        for poly_num, expanded, correct_factors, coeffs in polynomials_data
    ]

    # Run all factorizations in parallel
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Handle any exceptions
    final_results = []
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(colored(f"Error in polynomial {i+1}: {result}", "red"))
            poly_num, expanded, correct_factors, coeffs = polynomials_data[i]
            final_results.append({
                "polynomial_number": poly_num,
                "expanded_form": str(expanded),
                "coefficients": [str(coeff) for coeff in coeffs],
                "correct_factors": str(correct_factors),
                "llm_response": f"Error: {str(result)}",
                "is_correct": False
            })
        else:
            final_results.append(result)

    print(colored("\n" + "="*60, "cyan"))

    # Analyze and display results
    analyze_results(final_results)

    # Save results to JSON
    json_filename = save_to_json(final_results)

    print(colored(f"\nSummary: {len(final_results)} polynomials processed", "yellow"))
    print(colored(f"JSON results saved to: {json_filename}", "green"))

if __name__ == "__main__":
    asyncio.run(main())

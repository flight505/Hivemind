import csv
import random
from termcolor import colored

# Original complex formula from generate_complex_csv.py
def calculate_complex_output(A, B, C, D, E):
    """Original complex formula that generates the dataset"""
    sum_first_pair = A + B
    product_middle = C * D
    modulo_last = E % 10
    weighted_sum = A * 0.3 + B * 0.2 + C * 0.15 + D * 0.15 + E * 0.2

    if sum_first_pair > 100:
        if product_middle > 2000:
            if modulo_last >= 5 and weighted_sum > 60:
                return 1
            elif A > B and C > D:
                return 2
            elif modulo_last < 3:
                return 3
            else:
                return 4
        else:
            if C + D > 150 and E > 50:
                return 4
            elif sum_first_pair + modulo_last > 120:
                return 1
            else:
                return 2
    else:
        if product_middle < 1000:
            if modulo_last < 4 and weighted_sum < 40:
                return 3
            elif B > C and D > E:
                return 4
            else:
                return 2
        else:
            if weighted_sum > 55 and modulo_last >= 6:
                return 1
            elif A + E > 80:
                return 4
            else:
                return 3

# LLM-generated rules from the best_rules file
def apply_llm_rules(A, B, C, D, E):
    """Apply the GLM-4.5 generated rules"""
    import math

    # Rule 1: If sqrt(A) * E > B + D and ((A+C+D+E)/B > 15 or B < 15), then output class 2
    if B != 0 and math.sqrt(A) * E > B + D and ((A + C + D + E) / B > 15 or B < 15):
        return 2

    # Rule 2: If C + D + E > A + B and A < 30 and (E < 20 or B > 35), then output class 3
    if C + D + E > A + B and A < 30 and (E < 20 or B > 35):
        return 3

    # Rule 3: If (D + E) - (A + B) > 0 and (C < A and C < B and D > A and D > B), then output class 4
    if (D + E) - (A + B) > 0 and (C < A and C < B and D > A and D > B):
        return 4

    # Rule 4: If (C > A and C > B and D > A and D > B) and (E > 50 or (C * E) > (A * B)), then output class 4
    if (C > A and C > B and D > A and D > B) and (E > 50 or (C * E) > (A * B)):
        return 4

    # Rule 5: If E > 75 and C > 50 and D < 25, then output class 4
    if E > 75 and C > 50 and D < 25:
        return 4

    # Rule 6: If A + B > 160 and C < D and E < 75, then output class 3
    if A + B > 160 and C < D and E < 75:
        return 3

    # Rule 7: If A + B + C < D + E and E > 80 and B < 20, then output class 4
    if A + B + C < D + E and E > 80 and B < 20:
        return 4

    # Rule 8: If A > 60 and B < 15 and C > 35 and D > 55, then output class 4
    if A > 60 and B < 15 and C > 35 and D > 55:
        return 4

    # Rule 9: If C > 95 and E < 15, then output class 4
    if C > 95 and E < 15:
        return 4

    # Rule 10: If A > 75 and B < 10 and C > 60, then output class 4
    if A > 75 and B < 10 and C > 60:
        return 4

    # If no rule matches, return default
    return 1

def test_rule_accuracy():
    """Test if LLM rules match the original formula"""
    print(colored("🔍 Testing LLM Rules vs Original Formula", "magenta"))
    print(colored("=" * 50, "magenta"))

    # Test on random samples
    test_cases = 1000
    matches = 0
    mismatches = 0

    random.seed(random.randint(1, 1000000))  # Same seed as original

    print(colored(f"Testing {test_cases} random cases...", "blue"))

    for i in range(test_cases):
        # Generate same random values as original dataset
        A = random.randint(1, 100)
        B = random.randint(1, 100)
        C = random.randint(1, 100)
        D = random.randint(1, 100)
        E = random.randint(1, 100)

        # Get predictions from both methods
        original_output = calculate_complex_output(A, B, C, D, E)
        llm_output = apply_llm_rules(A, B, C, D, E)

        if original_output == llm_output:
            matches += 1
        else:
            mismatches += 1
            if mismatches <= 5:  # Show first few mismatches
                print(colored(f"MISMATCH {mismatches}: A={A}, B={B}, C={C}, D={D}, E={E}", "red"))
                print(colored(f"  Original: {original_output}, LLM: {llm_output}", "red"))

    accuracy = matches / test_cases
    print(colored("📊 RESULTS:", "cyan"))
    print(colored(f"   Test cases: {test_cases}", "yellow"))
    print(colored(f"   Matches: {matches}", "green"))
    print(colored(f"   Mismatches: {mismatches}", "red"))
    print(colored(f"   Accuracy: {accuracy:.1%}", "cyan"))

    if accuracy >= 0.99:
        print(colored("✅ LLM rules are highly accurate approximations!", "green"))
    elif accuracy >= 0.90:
        print(colored("⚠️ LLM rules are good approximations but not exact", "yellow"))
    else:
        print(colored("❌ LLM rules significantly differ from original formula", "red"))

    return accuracy

if __name__ == "__main__":
    test_rule_accuracy()

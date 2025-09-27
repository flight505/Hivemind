"""
Predictor 94
Generated on: 2025-09-09 05:33:00
Accuracy: 57.40%
"""


# PREDICTOR 94 - Accuracy: 57.40%
# Correct predictions: 5740/10000 (57.40%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from the most specific to the most general.
    """

    # 1. Very low C (≤12) – class 3 unless E is very high (→ class 4)
    if C <= 12:
        if E >= 70:
            return 4
        return 3

    # 2. Low C (<30) with a high E → class 4
    if C < 30 and E >= 70:
        return 4

    # 3. Low C with a very low B → class 3
    if C < 30 and B <= 15:
        return 3

    # 4. C in the 13‑15 range (still low) → class 3
    if C <= 15:
        return 3

    # 5. Very low E with modest C → class 3
    if E < 10 and C <= 45:
        return 3

    # 6. Edge case: C between 65‑70, very high B and modest E → class 2
    if 65 <= C < 70 and B >= 90 and E <= 60:
        return 2

    # 7. High C (≥75) together with strong B and high E → class 2
    if C >= 75 and B >= 60 and E >= 60:
        return 2

    # Default fallback
    return 1
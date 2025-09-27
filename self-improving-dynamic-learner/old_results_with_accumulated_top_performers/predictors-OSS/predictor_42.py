"""
Predictor 42
Generated on: 2025-09-09 04:05:02
Accuracy: 54.01%
"""


# PREDICTOR 42 - Accuracy: 54.01%
# Correct predictions: 5401/10000 (54.01%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from most specific to most general.
    """

    # 1. Very low C (≤12) with low B (≤15) → class 3
    if C <= 12:
        if B <= 15:
            return 3
        # 1a. Very low C but very high E → class 4
        if E >= 80:
            return 4
        # otherwise low‑C cases → class 1
        return 1

    # 2. High E (≥90) together with low‑moderate C (<30) → class 4
    if E >= 90 and C < 30:
        return 4

    # 3. High C (≥75) with strong B (≥60) → class 2
    if C >= 75 and B >= 60:
        return 2

    # 4. Low‑moderate C (<30) not caught by the previous rules → class 1
    if C < 30:
        return 1

    # 5. Default fallback → class 1
    return 1
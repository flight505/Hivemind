"""
Predictor 51
Generated on: 2025-09-09 04:11:22
Accuracy: 54.96%
"""


# PREDICTOR 51 - Accuracy: 54.96%
# Correct predictions: 5496/10000 (54.96%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic and comparisons.
    """

    # 1. Very high E together with low C → class 4
    if E >= 90 and C < 30:
        return 4

    # 2. Very low C (≤12)
    if C <= 12:
        # low B with very low C → class 3
        if B <= 15:
            return 3
        # otherwise, if E is relatively high → class 4
        if E >= 70:
            return 4
        # default for low‑C cases
        return 1

    # 3. High C (≥75) together with strong B → class 2
    if C >= 75 and B >= 60:
        return 2

    # 4. Default fallback → class 1
    return 1
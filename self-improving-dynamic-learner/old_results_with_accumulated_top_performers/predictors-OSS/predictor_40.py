"""
Predictor 40
Generated on: 2025-09-09 04:03:27
Accuracy: 57.11%
"""


# PREDICTOR 40 - Accuracy: 57.11%
# Correct predictions: 5711/10000 (57.11%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using simple arithmetic comparisons.
    Rules are evaluated from most specific to most general.
    """

    # 1. Very low C (≤ 12)
    if C <= 12:
        # extremely low B → class 3
        if B <= 5:
            return 3
        # high B with modest E → class 4
        if B >= 80 and E > 30:
            return 4
        # high E pushes to class 4
        if E >= 70:
            return 4
        # low B (≤15) still class 3
        if B <= 15:
            return 3
        # fallback
        return 1

    # 2. High B with low C (B > 80 and C < 30) → class 4
    if B > 80 and C < 30:
        return 4

    # 3. Very low E with low C (E < 10 and C < 40) → class 4
    if E < 10 and C < 40:
        return 4

    # 4. Very high C (≥ 75)
    if C >= 75:
        # strong B and high E → class 2
        if B >= 60 and E >= 60:
            return 2
        # low E → class 1
        if E < 30:
            return 1
        # default for high C
        return 1

    # 5. Very high C (≥ 90) with low B (B < 30) → class 1
    if C >= 90 and B < 30:
        return 1

    # 6. Default fallback
    return 1
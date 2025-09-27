"""
Predictor 3
Generated on: 2025-09-09 03:34:48
Accuracy: 44.34%
"""


# PREDICTOR 3 - Accuracy: 44.34%
# Correct predictions: 4434/10000 (44.34%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only simple arithmetic and comparisons.
    """

    # 1. Very low C values – distinguished by B
    if C < 25:
        if B <= 15:
            # When D is fairly large, treat as class 1, else class 3
            return 1 if D > 60 else 3
        else:
            return 4

    # 2. Medium‑high C values – narrow band gives class 2
    if 70 < C < 85:
        return 2

    # 3. Moderate region – use B and E to separate classes
    if B <= 15:
        return 3

    # 4. High E together with moderate C tends to class 2
    if E > 90 and 40 <= C <= 70:
        2

    # 5. Default fallback
    return 1
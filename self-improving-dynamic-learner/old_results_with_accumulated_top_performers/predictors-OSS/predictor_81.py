"""
Predictor 81
Generated on: 2025-09-09 04:45:15
Accuracy: 56.93%
"""


# PREDICTOR 81 - Accuracy: 56.93%
# Correct predictions: 5693/10000 (56.93%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic and comparisons.
    """

    # 1. High C (≥75) together with strong B and E → class 2
    if C >= 75 and B >= 60 and E >= 60:
        return 2

    # 2. Very low C (≤12)
    if C <= 12:
        #   very high E pushes to class 4
        if E >= 80:
            return 4
        #   otherwise default to class 3
        return 3

    # 3. Low‑mid C (<30) with very high E → class 4
    if C < 30 and E >= 80:
        return 4

    # 4. Default fallback → class 1
    return 1
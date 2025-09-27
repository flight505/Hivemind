"""
Predictor 131
Generated on: 2025-09-09 10:49:44
Accuracy: 58.42%
"""


# PREDICTOR 131 - Accuracy: 58.42%
# Correct predictions: 5842/10000 (58.42%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor derived from the provided 10‑row sample.
    The rules use only basic arithmetic comparisons and are ordered from
    most specific to most general.
    """

    # 1. Very low C (≤ 12)
    if C <= 12:
        # high E pushes the low‑C cases to class 4,
        # otherwise they belong to class 3.
        return 4 if E >= 70 else 3

    # 2. High C (≥ 75) together with strong B and E → class 2
    if C >= 75 and B >= 60 and E >= 60:
        return 2

    # 3. Low C (C < 30) with high E → class 4
    if C < 30 and E >= 70:
        return 4

    # 4. Default fallback
    return 1
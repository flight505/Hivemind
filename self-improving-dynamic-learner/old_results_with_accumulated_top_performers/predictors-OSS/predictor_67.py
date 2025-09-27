"""
Predictor 67
Generated on: 2025-09-09 04:23:14
Accuracy: 49.08%
"""


# PREDICTOR 67 - Accuracy: 49.08%
# Correct predictions: 4908/10000 (49.08%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from the most specific to the most general.
    """

    # 1. Very low C (≤ 12)
    if C <= 12:
        # low B with very low C → class 3
        if B <= 15:
            return 3
        # otherwise default to class 1
        return 1

    # 2. Low‑mid C (12 < C < 30)
    if C < 30:
        # high E with low C and modest B → class 4
        if E >= 90 and B <= 50:
            return 4
        # otherwise default to class 1
        return 1

    # 3. High C (≥ 75)
    if C >= 75:
        # very high C with very low B → class 4
        if B < 30:
            return 4
        # high C with strong B and moderate E → class 2
        if B >= 60 and E < 80:
            return 2
        # all other high‑C cases → class 1
        return 1

    # 4. All remaining cases (30 ≤ C < 75)
    return 1
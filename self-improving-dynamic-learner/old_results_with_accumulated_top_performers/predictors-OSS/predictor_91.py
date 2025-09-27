"""
Predictor 91
Generated on: 2025-09-09 05:23:44
Accuracy: 54.25%
"""


# PREDICTOR 91 - Accuracy: 54.25%
# Correct predictions: 5425/10000 (54.25%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor.
    1. Very high C together with high B → class 2
    2. Very low C together with low B → class 3
    3. Very high E together with low‑moderate C → class 4
    4. Default → class 1
    """
    # 1. High C (≥75) and strong B (≥60) → 2
    if C >= 75 and B >= 60:
        return 2

    # 2. Low C (≤12) and low B (≤15) → 3
    if C <= 12 and B <= 15:
        return 3

    # 3. High E (≥80) with modest C (<30) → 4
    if E >= 80 and C < 30:
        return 4

    # 4. Fallback
    return 1
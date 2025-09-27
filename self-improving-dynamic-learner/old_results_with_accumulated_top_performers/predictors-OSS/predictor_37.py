"""
Predictor 37
Generated on: 2025-09-09 04:02:15
Accuracy: 56.83%
"""


# PREDICTOR 37 - Accuracy: 56.83%
# Correct predictions: 5683/10000 (56.83%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic, comparisons
    and logical tests.  Rules are ordered from most specific to most
    general.
    """

    # 1. Very high E together with low C → class 4
    if E >= 90 and C < 30:
        return 4

    # 2. High C (≥75) with strong B and high E → class 2
    if C >= 75 and B >= 60 and E >= 60:
        return 2

    # 3. Very low C (≤12)
    if C <= 12:
        # low B → class 3
        if B <= 15:
            return 3
        # higher B → class 4
        if B > 30:
            return 4
        # fallback for the middle‑range B
        return 1

    # 4. Low C (<20) with very high D and moderate E → class 4
    if C < 20 and D > 80 and E > 30:
        return 4

    # 5. Default – class 1
    return 1
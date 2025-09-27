"""
Predictor 38
Generated on: 2025-09-09 04:02:30
Accuracy: 55.35%
"""


# PREDICTOR 38 - Accuracy: 55.35%
# Correct predictions: 5535/10000 (55.35%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic, comparisons and logical tests.
    Rules are ordered from most specific to most general.
    """

    # ----- Very low C (≤12) -----
    if C <= 12:
        if B <= 15:                 # low B + very low C → class 3
            return 3
        if B > 30:                  # higher B pushes to class 4
            return 4
        # B in the middle range (16‑30)
        if E >= 70:                 # high E also forces class 4
            return 4
        return 1                    # otherwise class 1

    # ----- Low C (13‑20) -----
    if C <= 20:
        if B <= 15:                 # low B still class 3
            return 3
        if B > 30:                  # medium/high B → class 4
            return 4
        return 1                    # otherwise class 1

    # ----- Very high C (≥75) -----
    if C >= 75:
        if B >= 60 and E >= 60:     # strong B and E give class 2
            return 2
        return 1                    # remaining very high C → class 1

    # ----- High C (65‑74) -----
    if C >= 65:
        if B >= 60 and E >= 70:     # slightly stricter for class 2
            return 2
        return 1

    # ----- Default case -----
    return 1
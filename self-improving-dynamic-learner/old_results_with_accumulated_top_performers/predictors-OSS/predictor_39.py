"""
Predictor 39
Generated on: 2025-09-09 04:03:16
Accuracy: 46.52%
"""


# PREDICTOR 39 - Accuracy: 46.52%
# Correct predictions: 4652/10000 (46.52%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic, comparisons and logic.
    The rules are ordered from most specific to most general.
    """

    # ----- Very low C (<= 12) -----
    if C <= 12:
        # high D together with moderately high E forces class 4
        if D > 70 and E > 45:
            return 4
        # very low B with low C gives class 3
        if B <= 5:
            return 3
        # extremely high B with low C but modest E stays class 1
        if B >= 80 and E < 70:
            return 1
        # low B (<=15) with low C gives class 3
        if B <= 15:
            return 3
        # otherwise class 3
        return 3

    # ----- Low B (<= 5) with higher C -----
    if B <= 5:
        if C >= 50:          # low B + relatively high C → class 4
            return 4
        return 3

    # ----- Very high C (>= 90) -----
    if C >= 90:
        if B >= 60:
            return 2          # strong B pushes to class 2
        return 4              # otherwise class 4

    # ----- High C (>= 75) -----
    if C >= 75:
        if E < 30:           # low E with very high C → class 3
            return 3
        if B >= 60 and E >= 60:
            return 2          # strong B and decent E → class 2
        return 1

    # ----- Mid C (30 – 50) -----
    if 30 <= C <= 50:
        if E >= 65:          # moderately high E forces class 4
            return 4
        if B <= 15:
            return 3
        return 1

    # ----- Low‑mid C (13 – 30) -----
    if C <= 30:
        if E >= 80:
            return 4
        if B <= 15:
            return 3
        return 1

    # ----- Default -----
    return 1
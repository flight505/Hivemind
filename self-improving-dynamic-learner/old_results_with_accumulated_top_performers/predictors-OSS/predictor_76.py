"""
Predictor 76
Generated on: 2025-09-09 04:26:55
Accuracy: 54.74%
"""


# PREDICTOR 76 - Accuracy: 54.74%
# Correct predictions: 5474/10000 (54.74%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from most specific to most general.
    """

    # 1. Very high E together with low C → class 4
    if E >= 90 and C < 30:
        return 4

    # 2. Very high C (≥ 90)
    if C >= 90:
        if B >= 60 and E >= 70:           # strong B and high E
            return 2
        if E < 30:                       # low E pushes to class 4
            return 4
        return 1                         # otherwise class 1

    # 3. High C (≥ 75)
    if C >= 75:
        if B >= 60 and E >= 60:
            return 2                     # typical high‑C, high‑B/E pattern
        return 1

    # 4. Very high C (≥ 60) with low B and low E → class 4
    if C >= 60 and B <= 15 and E <= 15:
        return 4

    # 5. Very high C (≥ 60) with low B (but not extremely low E) → class 3
    if C >= 60 and B <= 15:
        return 3

    # 6. Very low C (≤ 12)
    if C <= 12:
        if B <= 15:
            return 3                     # low B with very low C
        if D > 90 and E > 30:
            return 4                     # very high D together with moderate E
        if E >= 80:
            return 4                     # very high E forces class 4
        return 1                         # default for low‑C region

    # 7. Low C (13 – 30)
    if C < 30:
        if E >= 60 and B > 30:
            return 2                     # moderate B with high E
        if E >= 80:
            return 4                     # very high E regardless of B
        return 1

    # 8. C in 60 – 80 range with low B (already handled above)
    #    Remaining cases default to class 1
    return 1
"""
Predictor 52
Generated on: 2025-09-09 04:11:38
Accuracy: 51.34%
"""


# PREDICTOR 52 - Accuracy: 51.34%
# Correct predictions: 5134/10000 (51.34%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only simple arithmetic and logical tests.
    The rules are ordered from most specific to most general.
    """

    # 1. Very low C (≤12)
    if C <= 12:
        if B <= 15:
            return 3                     # low B with very low C → class 3
        if E >= 70:
            return 4                     # high E pushes to class 4
        return 1                         # otherwise class 1

    # 2. Low C (13‑30)
    if C <= 30:
        if E >= 70:
            return 2                     # high E with low‑C → class 2
        if B <= 15:
            return 3                     # low B with low‑C → class 3
        if B <= 20:
            return 3                     # slightly higher B still → class 3
        if D > 70 and B < 60:
            return 3                     # high D together with modest B → class 3
        return 1                         # default for this range

    # 3. Mid C (31‑50)
    if C <= 50:
        if B <= 15:
            return 3                     # low B → class 3
        if 40 <= C <= 50 and 30 <= B <= 50:
            return 3                     # moderate C & moderate B → class 3
        if B >= 60 and E >= 70:
            return 2                     # strong B & high E → class 2
        return 1                         # default

    # 4. High C (51‑70)
    if C <= 70:
        if B >= 60 and E >= 70:
            return 2                     # high B & high E → class 2
        if B <= 15 and D > 70:
            return 3                     # low B with very high D → class 3
        return 1                         # default

    # 5. Very high C (71‑90)
    if C < 90:
        if C >= 85:
            return 1                     # extremely high C → default to class 1
        if B <= 15:
            return 3                     # low B with high C → class 3
        if B >= 80 and E >= 70:
            return 2                     # very high B & high E → class 2
        if B >= 60 and E < 70:
            return 1                     # high B but not enough E → class 1
        return 1                         # fallback

    # 6. Very high C (≥90)
    if B <= 15 and D > 70:
        return 3                         # low B with very high D → class 3
    return 1                             # default fallback
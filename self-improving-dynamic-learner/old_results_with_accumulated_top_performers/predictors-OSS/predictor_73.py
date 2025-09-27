"""
Predictor 73
Generated on: 2025-09-09 04:25:35
Accuracy: 55.81%
"""


# PREDICTOR 73 - Accuracy: 55.81%
# Correct predictions: 5581/10000 (55.81%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic
    and comparisons.  Rules are ordered from most specific
    to most general.
    """

    # 1. Very high C (≥ 90)
    if C >= 90:
        # low B and low E → class 4
        if B < 50 and E < 30:
            return 4
        # strong B and high E → class 2
        if B >= 60 and E >= 70:
            return 2
        # default for extreme C
        return 1

    # 2. Very low C (≤ 12)
    if C <= 12:
        if B <= 15:                     # low B → class 3
            return 3
        # high D together with low C also → class 3
        if D > 70:
            return 3
        return 1                       # other low‑C cases

    # 3. Low C (13 ‑ 29)
    if C < 30:
        # high B and at least moderate E → class 4
        if B > 60 and E >= 30:
            return 4
        return 1

    # 4. Mid C (30‑45)
    if 30 <= C <= 45:
        # very high B and moderate‑high E → class 2
        if B >= 80 and E >= 45:
            return 2
        return 1

    # 5. High C (70‑89)
    if 70 <= C < 90:
        # strong B (≥ 80) and high E (≥ 70) → class 2
        if B >= 80 and E >= 70:
            return 2
        # very high C (≥ 75) with very high B (≥ 80) → class 2
        if C >= 75 and B >= 80:
            return 2
        # otherwise default to class 1
        return 1

    # 6. Default fallback
    return 1
"""
Predictor 62
Generated on: 2025-09-09 04:19:59
Accuracy: 51.46%
"""


# PREDICTOR 62 - Accuracy: 51.46%
# Correct predictions: 5146/10000 (51.46%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic,
    comparisons and logical tests.  Rules are evaluated from the
    most specific to the most general.
    """

    # 1. Very low C (≤12)
    if C <= 12:
        if B <= 15:                     # low B with very low C → class 3
            return 3
        # very high B together with very low E → also class 3
        if B > 80 and E < 20:
            return 3
        return 1                       # other low‑C cases → class 1

    # 2. Low C (≤20) – patterns that lead to class 4
    if C <= 20:
        # C ≤20 with very high B and very high D → class 4
        if B >= 70 and D >= 70:
            return 4
        # C <30 with high D, moderate B and low E → class 4
        if C < 30 and D > 70 and B >= 30 and E < 30:
            return 4
        # C <30 together with very high E → class 4
        if C < 30 and E >= 90:
            return 4
        # otherwise fall through to later rules
        pass

    # 3. High C (≥70)
    if C >= 70:
        # very low B forces class 1 irrespective of other values
        if B <= 15:
            return 1

        # C ≥75 with strong B and high E → class 2
        if C >= 75 and B >= 60 and E >= 70:
            return 2

        # C ≥75, low B and low‑moderate D/E → class 4
        if C >= 75 and B < 30 and E < 40:
            return 4

        # 70 ≤ C < 80 with high D and modest E → class 3
        if 70 <= C < 80 and D > 60 and E < 70:
            return 3

        # otherwise default to class 1
        return 1

    # 4. Mid C (40 – 70)
    if 40 <= C <= 70:
        # low B together with at least moderate E → class 4
        if B <= 15 and E >= 30:
            return 4
        return 1

    # 5. Default fallback
    return 1
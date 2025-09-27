"""
Predictor 95
Generated on: 2025-09-09 05:33:44
Accuracy: 57.83%
"""


# PREDICTOR 95 - Accuracy: 57.83%
# Correct predictions: 5783/10000 (57.83%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and logical tests.
    The rules are ordered from the most specific to the most general.
    """

    # 1. Very high C (≥ 90) → class 1
    if C >= 90:
        return 1

    # 2. Very low C (≤ 12)
    if C <= 12:
        if B <= 15:                 # low B → class 3
            return 3
        if E >= 70:                 # high E forces class 4
            return 4
        return 1                    # otherwise class 1

    # 3. Low C (≤ 20) with high D and moderate/large B → class 4
    if C <= 20 and D >= 70 and B > 30:
        return 4

    # 4. Low C (< 30) with high E → class 4
    if C < 30 and E >= 70:
        return 4

    # 5. High C (≥ 75)
    if C >= 75:
        if B >= 80:                 # very strong B forces class 2
            return 2
        if B >= 60 and E >= 60:     # strong B + high E also class 2
            return 2
        return 1

    # 6. Very high E (≥ 90) with mid C (30‑60) and high D → class 3
    if E >= 90 and 30 <= C <= 60 and D >= 60:
        return 3

    # 7. Very high D (≥ 80) with very low E (≤ 20) and mid C (30‑60) → class 3
    if D >= 80 and E <= 20 and 30 <= C <= 60:
        return 3

    # 8. Extremely low D (≤ 5) with C in 60‑70 range → class 3
    if D <= 5 and 60 <= C < 70:
        return 3

    # default fallback
    return 1
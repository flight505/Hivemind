"""
Predictor 68
Generated on: 2025-09-09 04:23:41
Accuracy: 52.42%
"""


# PREDICTOR 68 - Accuracy: 52.42%
# Correct predictions: 5242/10000 (52.42%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    Rules are evaluated from the most specific to the most general.
    """

    # 1. Very high C (≥ 90) → class 1
    if C >= 90:
        return 1

    # 2. High C (≥ 75)
    if C >= 75:
        # strong B and high E → class 2
        if B >= 60 and E >= 60:
            return 2
        # very low B with very high C → class 4
        if B < 30:
            return 4
        return 1

    # 3. Mid range C (30‑70)
    if 30 <= C <= 70:
        # high B with very low E → class 1
        if B >= 70 and E < 20:
            return 1
        # high B with high E → class 2
        if B >= 70 and E >= 70:
            return 2
        # low B with high E → class 4
        if B <= 20 and E >= 70:
            return 4
        # low B with modest E → class 3
        if B <= 20 and E < 50:
            return 3
        return 1

    # 4. Very low C (≤ 12)
    if C <= 12:
        if B <= 15:                 # low B with very low C
            return 3
        if E >= 80:                 # very high E pushes to class 4
            return 4
        return 1                    # other low‑C cases

    # 5. Low‑mid C (13‑29) with very high E
    if C < 30:
        if E >= 90:
            return 4
        return 1

    # 6. Default fallback
    return 1
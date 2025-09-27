"""
Predictor 46
Generated on: 2025-09-09 04:07:01
Accuracy: 53.20%
"""


# PREDICTOR 46 - Accuracy: 53.20%
# Correct predictions: 5320/10000 (53.20%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from most specific to most general.
    """

    # 1. Very low C (≤12)
    if C <= 12:
        # low B → class 3
        if B <= 15:
            return 3
        # high E with low C → class 4
        if E >= 70:
            return 4
        return 1

    # 2. Very high B together with low‑mid C
    if B >= 80 and C < 30:
        return 4

    # 3. C in 20‑30 range, high D and low E → class 4
    if 20 <= C <= 30 and D > 50 and E < 20:
        return 4

    # 4. C below 20, high D and low E → class 4
    if C < 20 and D > 50 and E < 20:
        return 4

    # 5. C between 10‑20, high E and high D → class 2
    if 10 <= C <= 20 and E >= 70 and D > 50:
        return 2

    # 6. Any C ≤ 25 with very high E → class 2
    if C <= 25 and E >= 90:
        return 2

    # 7. High B, moderate‑high C and very low E → class 4
    if B >= 80 and C >= 60 and E < 20:
        return 4

    # 8. Very high C (≥90) with low B → class 4
    if C >= 90 and B <= 30:
        return 4

    # 9. High C (≥75) with strong B and high E → class 2
    if C >= 75:
        if B >= 60 and E >= 60:
            return 2
        # low B and low E with high C → class 4
        if B < 30 and E < 40:
            return 4
        return 1

    # default fallback
    return 1
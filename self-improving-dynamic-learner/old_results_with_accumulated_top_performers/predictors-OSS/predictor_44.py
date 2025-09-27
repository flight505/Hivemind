"""
Predictor 44
Generated on: 2025-09-09 04:05:41
Accuracy: 53.48%
"""


# PREDICTOR 44 - Accuracy: 53.48%
# Correct predictions: 5348/10000 (53.48%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from the most specific to the most general.
    """

    # 1. Very low C (≤12)
    if C <= 12:
        # low B → class 3
        if B <= 15:
            return 3
        # very high E with low C → class 4
        if E >= 90:
            return 4
        # low C with high E and moderate/high B → class 2
        if E >= 70 and B >= 50:
            return 2
        # low C with high E (but not high enough for class 2) → class 4
        if E >= 70:
            return 4
        # default low‑C case
        return 1

    # 2. Low C (13‑20)
    if 13 <= C <= 20:
        # high E with low‑mid C → class 4
        if E >= 70 and B > 30:
            return 4
        return 1

    # 3. Extremely low C (≤5) with very high B → class 4
    if C <= 5 and B > 80:
        return 4

    # 4. High B with C around 30‑40 and very low E → class 4
    if B >= 80 and 30 <= C <= 40 and E < 20:
        return 4

    # 5. Low B with high E and moderate C (≥30) → class 4
    if B <= 15 and E >= 70 and C >= 30:
        return 4

    # 6. Very high D with low E → class 3
    if D > 90 and E < 40:
        return 3

    # 7. High C (≥75)
    if C >= 75:
        # very high C (≥90) always class 1
        if C >= 90:
            return 1
        # strong B and high E give class 2
        if B >= 60 and E >= 70:
            return 2
        return 1

    # 8. Mid‑high C (50‑70) with very high D → class 3
    if 50 <= C <= 70 and D > 90:
        return 3

    # 9. Specific pattern from error case 1:
    #    high B, C ≈30, large D and moderate E → class 2
    if B >= 80 and 30 <= C <= 40 and D >= 60:
        return 2

    # 10. Default fallback
    return 1
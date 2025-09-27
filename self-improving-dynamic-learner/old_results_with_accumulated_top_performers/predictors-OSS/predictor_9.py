"""
Predictor 9
Generated on: 2025-09-09 03:40:16
Accuracy: 48.34%
"""


# PREDICTOR 9 - Accuracy: 48.34%
# Correct predictions: 4834/10000 (48.34%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic and logical tests.
    The rules are ordered from most specific to most general.
    """

    # 1. Very high C (>=80)
    if C >= 80:
        if B <= 20:                     # low B with very high C
            return 4
        if B >= 80:                     # very high B with very high C
            return 2
        if B >= 40 and D < 30:          # moderate B, low D
            return 4
        if 20 < B < 40 and D < 30 and A < 30:   # mid B, low D, small A
            return 4
        if 20 < B < 40 and D < 30:               # mid B, low D, larger A
            return 1
        return 1                                         # all other very high C

    # 2. High C (65‑79)
    if 65 <= C < 80:
        if B > 80:                     # very high B → class 1
            return 1
        if B > 60:                     # moderately high B
            return 2
        return 1

    # 3. Very high E (>=95)
    if E >= 95:
        if C < 30:                     # low C together with extreme E
            return 2
        return 4

    # 4. High B (>80) with low C and relatively high E
    if B > 80 and C < 20 and E > 60:
        return 4

    # 5. High B (>80) with very low C and very low E
    if B > 80 and C < 40 and E < 10:
        return 3

    # 6. Extremely low B (<=5) with high D
    if B <= 5 and D > 50:
        return 1

    # 7. Low B (<=15) with high D and high E
    if B <= 15 and D > 70 and E > 70:
        return 1

    # 8. General low B (<=15)
    if B <= 15:
        return 3

    # 9. Very high E (>=90) with low C and moderate B
    if E >= 90 and C < 40 and 30 <= B <= 80:
        return 2

    # 10. Default
    return 1
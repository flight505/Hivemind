"""
Predictor 84
Generated on: 2025-09-09 04:47:00
Accuracy: 56.02%
"""


# PREDICTOR 84 - Accuracy: 56.02%
# Correct predictions: 5602/10000 (56.02%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from the most specific to the most general.
    """

    # 1. Very high C together with very low B → class 4
    if C >= 80 and B < 10:
        return 4
    if C >= 70 and B <= 10:
        return 4

    # 2. High C (75‑89) with strong B and high E → class 2
    if 75 <= C < 90:
        if B >= 60 and E >= 70:
            return 2
        return 1

    # 3. Low C (≤ 12)
    if C <= 12:
        if B <= 15:                     # very low B → class 3
            return 3
        if B >= 80:                     # very high B forces class 4
            return 4
        if E >= 70:                     # high E pushes to class 4
            return 4
        if B > 15 and E < 30:           # low E with moderate B → class 3
            return 3
        if B >= 50 and E >= 60:         # medium‑high B & E → class 2
            return 2
        return 1

    # 4. Low‑mid C (13‑30)
    if C <= 30:
        # very high E with very high D → class 3
        if E >= 70 and D > 90:
            return 3
        # very high E generally → class 4
        if E >= 80:
            return 4
        if E >= 70:
            return 4
        return 1

    # 5. Mid C (31‑45)
    if C <= 45:
        if B >= 70 and E >= 80:         # strong B & very high E → class 2
            return 2
        if E >= 80:                     # very high E otherwise → class 4
            return 4
        # 40‑50 range with low E and modest B → class 3
        if 40 <= C <= 50 and E < 30 and B <= 50:
            return 3
        return 1

    # 6. Upper‑mid C (46‑60)
    if C <= 60:
        if B >= 70 and E >= 80:         # strong B & very high E → class 2
            return 2
        if E >= 80:
            return 4
        # 40‑50 range with low E and modest B → class 3
        if 40 <= C <= 50 and E < 30 and B <= 50:
            return 3
        return 1

    # 7. High C (61‑70)
    if C <= 70:
        if B >= 70 and E >= 80:
            return 2
        if B <= 10 and E < 30:
            return 4
        return 1

    # default fallback
    return 1
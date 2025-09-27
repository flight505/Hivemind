"""
Predictor 114
Generated on: 2025-09-09 07:50:46
Accuracy: 47.88%
"""


# PREDICTOR 114 - Accuracy: 47.88%
# Correct predictions: 4788/10000 (47.88%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic, comparisons and logic.
    The rules are ordered from the most specific to the most general.
    """

    # ------------------------------------------------------------------
    # 1. Very low C (≤ 12)
    if C <= 12:
        if B <= 15:               # low B with very low C → class 3
            return 3
        if E >= 70:               # high E forces class 4
            return 4
        return 1

    # ------------------------------------------------------------------
    # 2. Low C (13‑20)
    if C <= 20:
        # very high B together with high E → class 4
        if B > 80 and E >= 60:
            return 4
        # high D with very low E → class 3  (e.g. 84,57,27,76,19)
        if D > 70 and E < 20:
            return 3
        return 1

    # ------------------------------------------------------------------
    # 3. Low‑mid C (21‑30)
    if C <= 30:
        # strong B and moderate‑high E → class 2  (e.g. 28,89,30,70,57)
        if B >= 80 and E >= 50:
            return 2
        # high D with very low E → class 3
        if D > 70 and E < 20:
            return 3
        return 1

    # ------------------------------------------------------------------
    # 4. Mid C (31‑45)
    if C <= 45:
        # very low B → class 3
        if B <= 15:
            return 3
        # very high B forces class 2  (e.g. 39,100,37,60,22)
        if B >= 80:
            return 2
        # strong B with decent E → class 2
        if B >= 60 and E >= 50:
            return 2
        # very low E → class 4
        if E < 30:
            return 4
        # high D with low‑moderate E → class 3
        if D > 70 and E < 50:
            return 3
        return 1

    # ------------------------------------------------------------------
    # 5. Upper‑mid C (46‑60)
    if C <= 60:
        # strong B & high E → class 2  (e.g. 20,81,49,75,98)
        if B >= 60 and E >= 60:
            return 2
        # very low E → class 4  (e.g. 13,32,53,29,31)
        if E < 35:
            return 4
        # high D with low‑moderate E → class 3
        if D > 70 and E < 50:
            return 3
        return 1

    # ------------------------------------------------------------------
    # 6. High‑mid C (61‑70)
    if C <= 70:
        # strong B → class 2  (e.g. 30,76,83,30,10)
        if B >= 70:
            return 2
        # very low E → class 4
        if E < 30:
            return 4
        # high D with low‑moderate E → class 3
        if D > 70 and E < 50:
            return 3
        return 1

    # ------------------------------------------------------------------
    # 7. Very high C (≥ 75)
    if C >= 75:
        # strong B (or any high B) → class 2
        if B >= 70:
            return 2
        # very low E → class 4
        if E < 30:
            return 4
        return 1

    # ------------------------------------------------------------------
    # default fallback
    return 1
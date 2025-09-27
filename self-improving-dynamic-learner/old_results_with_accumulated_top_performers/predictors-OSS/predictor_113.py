"""
Predictor 113
Generated on: 2025-09-09 07:47:57
Accuracy: 54.92%
"""


# PREDICTOR 113 - Accuracy: 54.92%
# Correct predictions: 5492/10000 (54.92%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic, comparisons and logic.
    The rules are ordered from the most specific to the most general.
    """

    # ------------------------------------------------------------------
    # 1. Very high E together with low C  → class 4
    if E >= 90 and C < 30:
        return 4
    if E >= 80 and C < 30 and E >= 70:
        return 4

    # ------------------------------------------------------------------
    # 2. Very low C (≤ 12)
    if C <= 12:
        if B <= 15:               # low B with very low C
            return 3
        if E >= 70:               # high E forces class 4
            return 4
        return 1

    # ------------------------------------------------------------------
    # 3. Low C (13‑20)
    if C <= 20:
        if E >= 70:               # high E overrides
            return 4
        return 1                     # default for this band

    # ------------------------------------------------------------------
    # 4. Low‑mid C (21‑30)
    if C <= 30:
        if E >= 70:               # high E → class 4
            return 4
        return 1

    # ------------------------------------------------------------------
    # 5. Mid C (31‑45)
    if 31 <= C <= 45:
        if E >= 80:               # very high E → class 4
            return 4
        if E < 30:                # very low E also → class 4
            return 4
        if B >= 80:               # strong B with moderate E → class 2
            return 2
        if B <= 15:               # low B → class 3
            return 3
        # high D with moderate E gives class 3 (e.g. case 5)
        if D > 70 and 30 <= E <= 60:
            return 3
        return 1

    # ------------------------------------------------------------------
    # 6. Upper‑mid C (46‑60)
    if 46 <= C <= 60:
        # very high B & very high E → class 4 (case 8)
        if B >= 80 and E >= 80:
            return 4
        # strong B & high E → class 2 (typical high‑C pattern)
        if B >= 60 and E >= 60:
            return 2
        # high D with moderate B/E gives class 3 (case 5)
        if D > 70 and B >= 60 and 30 <= E <= 60:
            return 3
        return 1

    # ------------------------------------------------------------------
    # 7. High C (61‑70)
    if 61 <= C <= 70:
        # low B forces class 1 (case 9)
        if B < 40:
            return 1
        # very high B & very high E → class 4
        if B >= 80 and E >= 80:
            return 4
        # strong B & high E → class 2
        if B >= 60 and E >= 60:
            return 2
        # very low E keeps class 1 (case 6)
        if E < 20:
            return 1
        return 1

    # ------------------------------------------------------------------
    # 8. Very high C (≥71)
    if C >= 71:
        # high C with strong B and E → class 2 (common pattern)
        if B >= 60 and E >= 60:
            return 2
        # very high C with low D (e.g., D < 20) → class 1
        if D < 20:
            return 1
        return 1

    # ------------------------------------------------------------------
    # default fallback
    return 1
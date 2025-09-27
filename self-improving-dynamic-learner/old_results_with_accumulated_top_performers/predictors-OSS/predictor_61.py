"""
Predictor 61
Generated on: 2025-09-09 04:19:31
Accuracy: 57.83%
"""


# PREDICTOR 61 - Accuracy: 57.83%
# Correct predictions: 5783/10000 (57.83%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from most specific to most general.
    """

    # ---- very high C (>=90) ----
    if C >= 90:
        return 1                       # dominant class for extreme C

    # ---- very low C (<=12) ----
    if C <= 12:
        # extremely high E together with low C
        if E >= 80:
            return 4
        # high E (≥60) but not extreme – still class 4
        if E >= 60:
            return 4
        # high B and very high D can force class 2
        if B >= 70 and D >= 80:
            return 2
        # low‑B region -> class 3
        if B <= 70:
            return 3
        return 1                       # fallback for low‑C

    # ---- low‑mid C (13‑29) ----
    if C < 30:
        # high E (≥70) pushes to class 4
        if E >= 70 and B > 20:
            return 4
        # very low B still class 3
        if B <= 15:
            return 3
        return 1

    # ---- C in 20‑30 range with strong B & D ----
    if 20 <= C <= 30:
        if B >= 80 and D >= 70:
            return 2
        if E >= 60 and B > 20:
            return 4
        return 1

    # ---- high C (75‑89) ----
    if C >= 75:
        # strong B (≥80) forces class 2 irrespective of E
        if B >= 80:
            return 2
        # high B & high E give class 2, otherwise default 1
        if B >= 60 and E >= 60:
            return 2
        # very high E together with high C can be class 4
        if E >= 90:
            return 4
        # low B with very high E can be class 4 as well
        if B <= 15 and E >= 70:
            return 4
        return 1

    # ---- moderate‑high C (70‑74) with low B ----
    if 70 <= C < 75 and B <= 15:
        return 4                         # low B overrides other signals

    # ---- moderate C (40‑59) ----
    if 40 <= C <= 59:
        # high B & very high E → class 2
        if B >= 70 and E >= 80:
            return 2
        # high B & very high E (but D very high) → keep class 1
        if D > 90:
            return 1
        # high B & very high E with moderate D → class 4
        if B >= 70 and E >= 80 and D < 80:
            return 4
        return 1

    # ---- mid C (30‑45) ----
    if 30 <= C <= 45:
        # high B & high E → class 2 (overrides the generic “4” rule)
        if B >= 70 and E >= 80:
            return 2
        # otherwise very high E pushes to class 4
        if E >= 80:
            return 4
        # low E with very high D → class 3
        if D > 70 and E < 30:
            return 3
        return 1

    # ---- low C with very high E (fallback) ----
    if E >= 70 and C < 30 and B > 20:
        return 4

    # ---- default ----
    return 1
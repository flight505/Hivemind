"""
Predictor 34
Generated on: 2025-09-09 04:00:11
Accuracy: 51.64%
"""


# PREDICTOR 34 - Accuracy: 51.64%
# Correct predictions: 5164/10000 (51.64%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic, comparisons and logical tests.
    The rules are ordered from most specific to most general.
    """

    # ---------- Very high C (≥90) ----------
    if C >= 90:
        return 1                     # dominant class for extreme C

    # ---------- Low C region (C ≤ 12) ----------
    if C <= 12:
        # very low C with very low E -> class 3
        if E < 20:
            return 3
        # very low C with moderate D -> class 3
        if D < 30:
            return 3
        # otherwise class 4
        return 4

    # ---------- Mid‑low C (13‑30) ----------
    if 13 <= C <= 30:
        # low‑mid C with high D -> class 4
        if D > 80:
            return 4
        # low‑mid C with high B and very high E -> class 4
        if B >= 80 and E >= 90:
            return 4
        # low‑mid C with high B but low E -> class 4
        if B >= 70 and E < 50:
            return 4
        # low‑mid C with very high B & moderate D -> class 2 (error #3)
        if B >= 80 and D >= 80:
            return 2
        # default for this band
        return 1

    # ---------- C 31‑45 ----------
    if 31 <= C <= 45:
        # high E pushes to class 4
        if E >= 70:
            return 4
        # otherwise class 1
        return 1

    # ---------- C 46‑60 ----------
    if 46 <= C <= 60:
        # high B & high E with low D -> class 2
        if B >= 60 and E >= 60 and D < 20:
            return 2
        # high B & high E with high D -> class 4
        if B >= 60 and E >= 60 and D > 80:
            return 4
        # default
        return 1

    # ---------- C 61‑70 ----------
    if 61 <= C <= 70:
        # low D and high E -> class 2
        if D < 20 and E >= 60:
            return 2
        # very high D -> class 4
        if D > 80:
            return 4
        # high B & high E -> class 2
        if B >= 70 and E >= 60:
            return 2
        return 1

    # ---------- C 71‑79 ----------
    if 71 <= C <= 79:
        # high B with low E -> class 4
        if B >= 70 and E < 50:
            return 4
        # high B with moderate E -> class 2
        if B >= 70 and E >= 70:
            return 2
        # very low D -> class 1
        if D < 10:
            return 1
        # default
        return 1

    # ---------- C 80‑89 ----------
    if 80 <= C <= 89:
        # very high B & high E -> class 2
        if B >= 80 and E >= 70:
            return 2
        # very high B but low E -> class 4
        if B >= 80 and E < 50:
            return 4
        # otherwise class 1
        return 1

    # ---------- Default ----------
    return 1
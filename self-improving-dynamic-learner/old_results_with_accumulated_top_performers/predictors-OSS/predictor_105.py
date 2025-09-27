"""
Predictor 105
Generated on: 2025-09-09 06:32:29
Accuracy: 54.16%
"""


# PREDICTOR 105 - Accuracy: 54.16%
# Correct predictions: 5416/10000 (54.16%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only simple arithmetic and comparisons.
    The rules are ordered from the most specific to the most general.
    """

    # ---------- Very high C (≥ 90) ----------
    if C >= 90:
        if B >= 80:          # strong B with extreme C
            return 2
        return 1

    # ---------- High C (75 – 89) ----------
    if C >= 75:
        if B >= 80:          # very strong B forces class 2
            return 2
        if E < 10:           # extremely low E with high C
            return 3
        return 1

    # ---------- High C (70 – 74) ----------
    if C >= 70:
        return 1

    # ---------- Mid‑high C (60 – 69) ----------
    if C >= 60:
        # class 2 only when both B and E are high
        if B >= 80 and E >= 70:
            return 2
        return 1

    # ---------- Upper‑mid C (50 – 59) ----------
    if C >= 50:
        # very low D indicates class 2
        if D <= 10:
            return 2
        return 1

    # ---------- Low‑mid C (30 – 44) ----------
    if C >= 30:
        # very high E together with high D → class 3
        if E >= 80 and D >= 70:
            return 3
        # low E in this band → class 4
        if E < 30:
            return 4
        return 1

    # ---------- Very low C (≤ 12) ----------
    if C <= 12:
        # low B gives class 3
        if B <= 15:
            return 3
        # strong B and high E give class 2
        if B >= 60 and E >= 60:
            return 2
        # very high E forces class 4
        if E >= 90:
            return 4
        if E >= 80:
            return 4
        return 1

    # ---------- Low‑mid C (13 – 29) ----------
    # high E (≥90) overrides to class 4
    if E >= 90:
        return 4

    # C ≤ 15 with high D → class 4
    if C <= 15 and D >= 70:
        return 4

    # Default fallback
    return 1
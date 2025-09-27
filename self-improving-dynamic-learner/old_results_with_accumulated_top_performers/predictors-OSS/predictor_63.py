"""
Predictor 63
Generated on: 2025-09-09 04:20:20
Accuracy: 54.00%
"""


# PREDICTOR 63 - Accuracy: 54.00%
# Correct predictions: 5400/10000 (54.00%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and logical tests.
    The rules are evaluated from the most specific to the most general.
    """

    # ---- very high C (≥ 90) ----
    if C >= 90:
        # very high D together with very high E → class 1
        if D > 90 and E > 80:
            return 1
        # high D with low E still class 3
        if E < 30 and D > 60:
            return 3
        # very low E with very high C → class 4
        if E < 20:
            return 4
        # strong B and high E → class 2
        if B >= 60 and E >= 70:
            return 2
        return 1

    # ---- high C (75‑89) ----
    if C >= 75:
        # high B, very high D and modest E → class 3
        if B >= 80 and D > 70 and E < 50:
            return 3
        # low E with strong B → class 2
        if B >= 60 and E < 20:
            return 2
        # strong B and high E → class 2
        if B >= 60 and E >= 70:
            return 2
        # very high D with low E → class 3
        if D > 70 and E < 30:
            return 3
        return 1

    # ---- very low C (≤ 12) ----
    if C <= 12:
        # low B → class 3
        if B <= 15:
            return 3
        # very low E with low C → class 3
        if E < 10:
            return 3
        # very high E with low C → class 4
        if E >= 80:
            return 4
        return 1

    # ---- low C (13‑29) ----
    if C < 30:
        # very high B with very high E → class 4
        if B > 80 and E >= 70:
            return 4
        # low B with very high E → class 4
        if B <= 15 and E >= 70:
            return 4
        # very high E (≥90) irrespective of B → class 4
        if E >= 90:
            return 4
        return 1

    # ---- middle C (40‑60) ----
    if 40 <= C <= 60:
        # strong B together with high E → class 2
        if B >= 50 and E >= 70:
            return 2
        return 1

    # ---- broad C (50‑70) ----
    if 50 <= C < 70:
        # low B with very high E → class 2
        if B <= 15 and E >= 70:
            return 2
        return 1

    # default fallback
    return 1
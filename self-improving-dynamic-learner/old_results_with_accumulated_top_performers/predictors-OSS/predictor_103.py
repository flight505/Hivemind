"""
Predictor 103
Generated on: 2025-09-09 06:28:33
Accuracy: 48.40%
"""


# PREDICTOR 103 - Accuracy: 48.40%
# Correct predictions: 4840/10000 (48.40%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic and comparisons.
    The conditions are ordered from most specific to most general.
    """

    # -------------------------------------------------
    # 1. Very low C (≤ 12)
    # -------------------------------------------------
    if C <= 12:
        # low B → class 3
        if B <= 15:
            return 3
        # high D together with moderate/high E → class 4
        if D > 50 and E >= 50:
            return 4
        # otherwise a high E (≥ 60) forces class 4
        if E >= 60:
            return 4
        # default for very low C
        return 1

    # -------------------------------------------------
    # 2. Low C (13 – 30)
    # -------------------------------------------------
    if C <= 30:
        # low‑moderate B (≤ 20) → class 3
        if B <= 20:
            return 3
        # very high E forces class 4
        if E >= 70:
            return 4
        return 1

    # -------------------------------------------------
    # 3. Very high C (≥ 90)
    # -------------------------------------------------
    if C >= 90:
        # patterns observed for extremely high C give class 3
        return 3

    # -------------------------------------------------
    # 4. High C (80 – 89)
    # -------------------------------------------------
    if C >= 80:
        # strong B together with strong D → class 2
        if B >= 80 and D >= 80:
            return 2
        # very low B → class 4
        if B <= 10:
            return 4
        return 1

    # -------------------------------------------------
    # 5. High C (75 – 79)
    # -------------------------------------------------
    if C >= 75:
        if B <= 10:
            return 4
        # strong B and high E give class 2
        if B >= 60 and E >= 60:
            return 2
        return 1

    # -------------------------------------------------
    # 6. High C (70 – 74)
    # -------------------------------------------------
    if C >= 70:
        if B <= 10:
            return 4
        # need high D together with high B/E for class 2
        if D >= 70 and B >= 60 and E >= 60:
            return 2
        return 1

    # -------------------------------------------------
    # 7. Mid‑high C (60 – 69)
    # -------------------------------------------------
    if C >= 60:
        if B <= 10:
            return 4
        if D >= 70 and B >= 60 and E >= 60:
            return 2
        return 1

    # -------------------------------------------------
    # 8. Mid C (45 – 59)
    # -------------------------------------------------
    if C >= 45:
        if B >= 40 and E >= 50:
            return 2
        return 1

    # -------------------------------------------------
    # 9. Lower‑mid C (30 – 44)
    # -------------------------------------------------
    if C >= 30:
        if B >= 40 and E >= 50:
            return 2
        if B <= 15 and E < 30:
            return 3
        return 1

    # -------------------------------------------------
    # 10. Default fallback
    # -------------------------------------------------
    return 1
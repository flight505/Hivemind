"""
Predictor 77
Generated on: 2025-09-09 04:27:32
Accuracy: 55.64%
"""


# PREDICTOR 77 - Accuracy: 55.64%
# Correct predictions: 5564/10000 (55.64%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from most specific to most general.
    """

    # -----------------------------------------------------------------
    # 1. Very low C (≤ 12)
    # -----------------------------------------------------------------
    if C <= 12:
        # very high E → class 4
        if E >= 70:
            return 4
        # high D together with moderate E also forces class 4
        if D > 80 and E >= 50:
            return 4
        # low B → class 3
        if B <= 15:
            return 3
        # high B with very low E → class 1 (e.g. A=51,B=76,E=29)
        if B >= 60 and E < 40:
            return 1
        # default for low‑C region
        return 3

    # -----------------------------------------------------------------
    # 2. Low C (13 – 29)
    # -----------------------------------------------------------------
    if C < 30:
        # high E with a modest B gives class 4, but only when B is not large
        if E >= 70 and B < 60:
            return 4
        # low B (or not‑large B) with moderate E gives class 3
        if B < 30 or (B < 60 and E < 50):
            return 3
        # otherwise class 1
        return 1

    # -----------------------------------------------------------------
    # 3. Mid C (30 – 45)
    # -----------------------------------------------------------------
    if 30 <= C <= 45:
        # strong B and high E → class 2
        if B >= 70 and E >= 70:
            return 2
        # strong B with very high E also → class 2
        if B >= 70 and E >= 80:
            return 2
        # otherwise default
        return 1

    # -----------------------------------------------------------------
    # 4. Upper‑mid C (46 – 60)
    # -----------------------------------------------------------------
    if 46 <= C <= 60:
        if B >= 70 and E >= 80:
            return 2
        return 1

    # -----------------------------------------------------------------
    # 5. High C (61 – 69)
    # -----------------------------------------------------------------
    if 61 <= C <= 69:
        # low E pushes to class 4
        if E < 20:
            return 4
        # very low B with high C tends to class 3
        if B <= 20:
            return 3
        return 1

    # -----------------------------------------------------------------
    # 6. Very high C (70 – 89)
    # -----------------------------------------------------------------
    if 70 <= C < 90:
        # extremely high B and E → class 2
        if B >= 80 and E >= 80:
            return 2
        # low B with moderate‑high C → class 3
        if B <= 20:
            return 3
        # otherwise class 1
        return 1

    # -----------------------------------------------------------------
    # 7. Extremely high C (≥ 90)
    # -----------------------------------------------------------------
    if C >= 90:
        return 1

    # -----------------------------------------------------------------
    # Default fallback
    # -----------------------------------------------------------------
    return 1
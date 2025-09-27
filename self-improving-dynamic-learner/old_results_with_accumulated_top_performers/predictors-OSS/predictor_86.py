"""
Predictor 86
Generated on: 2025-09-09 04:48:24
Accuracy: 45.66%
"""


# PREDICTOR 86 - Accuracy: 45.66%
# Correct predictions: 4566/10000 (45.66%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from most specific to most general and aim
    to correct recent error patterns while keeping a simple structure.
    """

    # 1. Very high C (≥ 90)
    if C >= 90:
        # very low E → class 4
        if E < 30:
            return 4
        # both B and E relatively high → class 2
        if B >= 50 and E >= 50:
            return 2
        # otherwise default to class 1
        return 1

    # 2. Extremely low B with high C → class 3
    if B <= 5 and C >= 70:
        return 3

    # 3. High C (75‑89)
    if 75 <= C < 90:
        # strong B and high E → class 2
        if B >= 60 and E >= 60:
            return 2
        # low E → class 4
        if E < 30:
            return 4
        # otherwise class 1
        return 1

    # 4. Mid C range (30‑45)
    if 30 <= C <= 45:
        # very high E
        if E >= 80:
            if B >= 60:
                return 2          # strong B with very high E
            return 4              # otherwise very high E gives class 4
        # high E (≥70) but not extreme
        if E >= 70:
            if B >= 60:
                return 2
            return 4
        # high B alone can also force class 4
        if B >= 70:
            return 4
        return 1

    # 5. Upper‑mid C (46‑70)
    if 46 <= C < 75:
        # low E together with moderate C ⇒ class 4
        if E < 30:
            return 4
        return 1

    # default fallback
    return 1
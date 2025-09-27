"""
Predictor 59
Generated on: 2025-09-09 04:18:36
Accuracy: 47.72%
"""


# PREDICTOR 59 - Accuracy: 47.72%
# Correct predictions: 4772/10000 (47.72%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from most specific to most general.
    """

    # 1. Very high C (>= 90)
    if C >= 90:
        if E < 20:          # very low E with ultra‑high C → class 4
            return 4
        if B >= 60 and E >= 60:   # strong B and high E → class 2
            return 2
        return 1           # otherwise class 1

    # 2. Very low C (<= 12)
    if C <= 12:
        if E >= 80:        # high E with very low C → class 4
            return 4
        return 3           # otherwise class 3

    # 3. Low‑mid C (13 – 35)
    if 13 <= C <= 35:
        if E >= 90:        # very high E still forces class 4
            return 4
        # when D is very high, the record tends to be class 1
        if D >= 90 and (B > 80 or C <= 20):
            return 1
        return 3           # default for this band

    # 4. Mid C (36 – 45)
    if 36 <= C <= 45:
        if E >= 95:        # extremely high E → class 4
            return 4
        return 3           # otherwise class 3

    # 5. High C (75 – 89)
    if C >= 75:
        if B >= 60 and E >= 60:   # strong B and E with high C → class 2
            return 2
        return 1           # otherwise class 1

    # 6. Default fallback
    return 1
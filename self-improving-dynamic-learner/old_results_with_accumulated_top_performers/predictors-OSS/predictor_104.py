"""
Predictor 104
Generated on: 2025-09-09 06:28:59
Accuracy: 51.47%
"""


# PREDICTOR 104 - Accuracy: 51.47%
# Correct predictions: 5147/10000 (51.47%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from most specific to most general.
    """

    # --------------------- Very high C (≥ 90) ---------------------
    if C >= 90:
        if B >= 60 and E >= 60:
            return 2                     # strong B & E
        return 1                         # default for extreme C

    # --------------------- High C (75 – 89) ----------------------
    if 75 <= C < 90:
        if B >= 60 and E >= 60:
            return 2
        return 1

    # --------------------- Upper‑mid C (65 – 74) -----------------
    if 65 <= C < 75:
        if B >= 60 and E >= 60:
            return 2
        return 1

    # --------------------- Mid‑high C (50 – 64) -----------------
    if 50 <= C < 65:
        # moderate B together with moderate‑high E → class 2
        if B >= 25 and E >= 50:
            return 2
        return 1

    # --------------------- Mid C (30 – 49) ----------------------
    if 30 <= C < 50:
        # very high E together with high D → class 3
        if E >= 80 and D >= 70:
            return 3
        if E >= 70 and D >= 70:
            return 3
        # low E with relatively low B → class 4
        if E < 30 and B < 50:
            return 4
        return 1

    # --------------------- Low‑mid C (13 – 29) ------------------
    if 13 <= C < 30:
        # very low B
        if B <= 15:
            # moderate/high E pushes to class 4, otherwise class 3
            if E >= 50:
                return 4
            return 3
        # higher B
        if B >= 60 and E >= 60:
            return 2                     # strong B & E
        if D >= 70:
            return 4                     # large D with low‑C forces class 4
        return 1

    # --------------------- Very low C (≤ 12) -------------------
    if C <= 12:
        # very low B
        if B <= 15:
            # moderate/high E should be class 4, else class 3
            if E >= 50:
                return 4
            return 3
        # higher B
        if B >= 60 and E >= 60:
            return 2                     # strong B & E
        if E >= 70:
            return 4
        return 1

    # --------------------- Fallback ----------------------------
    return 1
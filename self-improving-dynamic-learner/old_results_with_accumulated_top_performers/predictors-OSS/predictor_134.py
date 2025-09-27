"""
Predictor 134
Generated on: 2025-09-09 10:54:15
Accuracy: 53.99%
"""


# PREDICTOR 134 - Accuracy: 53.99%
# Correct predictions: 5399/10000 (53.99%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only simple arithmetic and comparisons.
    The rules are ordered from the most specific to the most general
    and incorporate patterns observed in the training data and the
    recent error cases.
    """

    # 1. Very high C (≥ 90) – dominant class 1
    if C >= 90:
        return 1

    # 2. High C (≥ 75)
    if C >= 75:
        # strong B (≥ 60) forces class 2 regardless of E
        if B >= 60:
            return 2
        return 1

    # 3. Upper‑mid C (65‑74)
    if C >= 65:
        # low B and very low E → class 4  (captures 69‑C cases)
        if B <= 20 and E < 30:
            return 4
        return 1

    # 4. Mid C (45‑64) – high D with moderate E gives class 3
    if 45 <= C <= 64:
        if D >= 90 and 40 <= C <= 60 and E < 70:
            return 3
        return 1

    # 5. Mid‑low C (30‑44)
    if 30 <= C <= 44:
        # very low B → class 3
        if B <= 15:
            return 3
        # low B with high E → class 4
        if B <= 20 and E >= 70:
            return 4
        return 1

    # 6. Low C (≤ 30)
    #    – high D combined with low E yields class 4
    if D >= 70 and E < 60:
        return 4

    #    – very high E pushes to class 4, but strong B forces class 2
    if E >= 80:
        if B >= 60:
            return 2
        return 4
    if E >= 70:
        if B >= 60:
            return 2
        return 4

    #    – low B with low C gives class 3
    if B <= 15:
        return 3

    # 7. Very low C (≤ 12) – already covered by the previous rules,
    #    but keep the classic pattern for completeness
    if C <= 12:
        if B <= 15:
            return 3
        return 1

    # 8. Default fallback
    return 1
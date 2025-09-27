"""
Predictor 48
Generated on: 2025-09-09 04:08:25
Accuracy: 55.69%
"""


# PREDICTOR 48 - Accuracy: 55.69%
# Correct predictions: 5569/10000 (55.69%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and comparisons.
    The rules are evaluated from most specific to most general.
    """

    # 1. Very high C (≥ 90)
    if C >= 90:
        # high‑C with low B → class 1 (e.g. C=100, B=29)
        if B < 50:
            return 1
        # high‑C with high B and very high E → class 2
        if B >= 60 and E >= 70:
            return 2
        # otherwise treat as class 4
        return 4

    # 2. Low C (≤ 12)
    if C <= 12:
        # very low B → class 3, unless E or D are large
        if B <= 15:
            if E >= 70 or D > 80:      # e.g. C=3, D=99, E=65
                return 4
            return 3
        # very high B with low‑E → class 1 (e.g. B=99, C=4, E=18)
        if B > 80 and E < 30:
            return 1
        # high‑E or high‑D with moderate B → class 4
        if E >= 70 or D > 80:
            return 4
        return 3

    # 3. Moderate C (13 – 30)
    if 13 <= C <= 30:
        # moderate C with high E (≈80) → class 2
        if 25 <= C <= 35 and E >= 80:
            return 2
        # low B plus relatively high E → class 4
        if B <= 15 and E >= 50:
            return 4
        # low B plus low E → class 3
        if B <= 15:
            return 3

    # 4. C in the 40 – 60 range
    if 40 <= C <= 60:
        # high B and very high E, together with high D → class 3
        if B >= 60 and E >= 80 and D > 70:
            return 3
        # high B and very high E (but D not extreme) → class 2
        if B >= 60 and E >= 80:
            return 2
        # otherwise default to class 1
        return 1

    # 5. C ≥ 75 (high but not extreme)
    if C >= 75:
        if B >= 60 and E >= 70:
            return 2
        return 1

    # 6. Very high B (≥ 90) with very low C (≤ 10)
    if B >= 90 and C <= 10:
        return 4

    # 7. C around 30 – 35 with very high E and relatively low B
    if 30 <= C <= 35 and E >= 80 and B < 50:
        return 4

    # 8. C ≥ 80 with B < 50 (but not caught by rule 1)
    if C >= 80 and B < 50:
        return 4

    # 9. Default fallback
    return 1
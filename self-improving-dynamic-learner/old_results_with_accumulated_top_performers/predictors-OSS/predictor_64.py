"""
Predictor 64
Generated on: 2025-09-09 04:20:40
Accuracy: 51.67%
"""


# PREDICTOR 64 - Accuracy: 51.67%
# Correct predictions: 5167/10000 (51.67%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic,
    comparisons and logical tests.  Rules are evaluated from the most
    specific to the most general.
    """

    # 1. Very low C with very high D and high B → class 4
    if C <= 12 and D > 80 and B > 70:
        return 4

    # 2. Very low C with low B → class 3
    if C <= 12 and B <= 15:
        return 3

    # 3. Very high E together with very low B → keep class 1
    if E >= 90 and B <= 15:
        return 1

    # 4. Very high C (≥80)
    if C >= 80:
        # low B (≤20) forces class 4
        if B <= 20:
            return 4
        # high D and low E also forces class 4
        if D > 60 and E < 30:
            return 4
        # otherwise default to class 1
        return 1

    # 5. Mid‑high C (45‑70)
    if 45 <= C <= 70:
        # low B (≤15) → class 4
        if B <= 15:
            return 4
        # high B with high D → class 2
        if B >= 70 and D > 60:
            return 2
        # otherwise default to class 1
        return 1

    # 6. Low‑mid C (20‑35)
    if 20 <= C <= 35:
        # low B and low E → class 3
        if B < 50 and E < 30:
            return 3
        # otherwise default to class 1
        return 1

    # 7. Default fallback
    return 1
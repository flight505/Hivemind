"""
Predictor 10
Generated on: 2025-09-09 03:41:45
Accuracy: 34.56%
"""


# PREDICTOR 10 - Accuracy: 34.56%
# Correct predictions: 3456/10000 (34.56%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only simple arithmetic and logical tests.
    """

    # 1. Very low B → class 3
    if B <= 15:
        return 3

    # 2. High E together with low C and a moderate D (10‑79) → class 4
    if E >= 70 and C <= 40 and 10 <= D < 80:
        return 4

    # 3. High C (>70) but only when B is not extremely high → class 2
    if C > 70 and B < 90:
        return 2

    # 4. Very high B with low C and D not too low → class 4
    if B > 80 and C < 30 and D >= 10:
        return 4

    # 5. Very high A and B (both >90) → class 2
    if A > 90 and B > 90:
        return 2

    # 6. Low D (<20) combined with high B (≥60) and modest E (<60) → class 2
    if D < 20 and B >= 60 and E < 60:
        return 2

    # 7. Moderate B (30‑50) and moderate D (50‑70) → class 4
    if 30 <= B <= 50 and 50 <= D <= 70:
        return 4

    # 8. High C (≥60) with low B and low D → class 4
    if C >= 60 and B < 20 and D < 30:
        return 4

    # 9. Low B (≤20) with very low D and relatively high C → class 3
    if B <= 20 and D < 20 and C > 50:
        return 3

    # 10. Default → class 1
    return 1
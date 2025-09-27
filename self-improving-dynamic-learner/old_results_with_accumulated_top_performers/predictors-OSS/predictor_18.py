"""
Predictor 18
Generated on: 2025-09-09 03:47:12
Accuracy: 58.22%
"""


# PREDICTOR 18 - Accuracy: 58.22%
# Correct predictions: 5822/10000 (58.22%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using basic arithmetic and comparisons.
    The rules are ordered from most specific to most general.
    """

    # 1. Very high E together with low C → class 4
    if E >= 90 and B > 15 and C < 30:
        return 4

    # 2. Very high B and high E with low‑moderate C → class 4
    if B >= 90 and E >= 70 and C < 40:
        return 4

    # 3. Low B (≤15):
    if B <= 15:
        # low C gives class 3
        if C <= 12:
            return 3
        # very low D also gives class 3
        if D < 10:
            return 3
        return 1

    # 4. Very low C (≤12) with moderate B:
    if C <= 12:
        # very small B still class 3 (handled above), otherwise:
        if B <= 20:
            return 3
        if D > 80:
            return 4
        return 1

    # 5. High C (≥75):
    if C >= 75:
        # high B and sufficiently high E → class 2
        if B >= 60 and E >= 70:
            return 2
        return 1

    # 6. Mid C (20‑30) with moderate B and decent E → class 2
    if 20 <= C <= 30 and 40 <= B <= 60 and E >= 60:
        return 2

    # 7. Very large A and B (both >90) → class 2
    if A > 90 and B > 80:
        return 2

    # 8. Very high D together with very low C → class 4
    if D > 90 and C < 15:
        return 4

    # 9. Very low D with modest B → class 3
    if D < 10 and B < 40:
        return 3

    # default
    return 1
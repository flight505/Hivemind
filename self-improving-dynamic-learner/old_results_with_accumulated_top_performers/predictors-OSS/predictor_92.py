"""
Predictor 92
Generated on: 2025-09-09 05:25:11
Accuracy: 54.97%
"""


# PREDICTOR 92 - Accuracy: 54.97%
# Correct predictions: 5497/10000 (54.97%)

def predict_output(A, B, C, D, E):
    """
    Rule‑based predictor using only basic arithmetic and logical tests.
    The rules are ordered from the most specific to the most general,
    aiming to correct the previously mis‑predicted examples while
    keeping the overall logic simple.
    """

    # 1. Very high C (≥80) – class 2 only when B and E are both very high
    if C >= 80:
        if B >= 80 and E >= 80:
            return 2
        return 1

    # 2. High C (75‑79) – class 2 when B and E are strongly high
    if C >= 75:
        if B >= 60 and E >= 70:
            return 2
        return 1

    # 3. High C (≥70) with very low E → class 4
    if C >= 70 and E < 30:
        return 4

    # 4. High C (70‑79) with extremely high B but very low E → class 4
    if C >= 70 and B > 80 and E < 20:
        return 4

    # 5. Very low C (≤12)
    if C <= 12:
        if B <= 15:                     # low B → class 3
            return 3
        if D >= 80 and E >= 50:        # high D together with moderate‑high E → class 4
            return 4
        if D >= 80:                    # high D alone → class 3
            return 3
        if E >= 70:                    # high E pushes to class 4
            return 4
        return 1                       # other low‑C cases

    # 6. Low‑C (≤30) with very high D → class 3
    if C <= 30 and D >= 90:
        return 3

    # 7. Low‑C (≤20) with modest B and medium‑high E → class 4
    if C <= 20 and B > 30 and E >= 40:
        return 4

    # 8. Very low B with high D → class 3
    if B <= 15 and D >= 70:
        return 3

    # 9. Mid‑high C (65‑74) with decent B and high E → class 2
    if 65 <= C < 75 and B >= 30 and E >= 60:
        return 2

    # 10. Medium C (30‑60) with very high D and high E → class 3
    if 30 <= C <= 60 and D >= 90 and E >= 60:
        return 3

    # 11. Low‑C (<30) with very high E → class 4
    if C < 30 and E >= 80:
        return 4

    # default fallback
    return 1
"""
Predictor 56
Generated on: 2025-09-09 04:13:33
Accuracy: 48.84%
"""


# PREDICTOR 56 - Accuracy: 48.84%
# Correct predictions: 4884/10000 (48.84%)

def predict_output(A, B, C, D, E):
    """
    Simple rule‑based predictor using only basic arithmetic and comparisons.
    The rules are ordered from most specific to most general.
    """

    # 1. High C (≥75) together with high B (≥60) → class 2
    if C >= 75 and B >= 60:
        return 2

    # 2. Very high E (≥90) → class 4
    if E >= 90:
        return 4

    # 3. Very low C (≤12)
    if C <= 12:
        if B <= 15:           # low B with very low C → class 3
            return 3
        if E >= 80:           # high E pushes to class 4
            return 4
        return 3              # default for low‑C cases

    # 4. Low‑moderate C (<30) with high E (≥70) → class 4
    if C < 30 and E >= 70:
        return 4

    # 5. Low C (≤20) – special handling
    if C <= 20:
        if B > 50 and D > 80:   # high B together with very high D → class 4
            return 4
        if B <= 25:            # low‑to‑moderate B → class 3
            return 3
        return 1               # otherwise class 1

    # 6. Very high D with very low E → class 3
    if D > 80 and E < 20:
        return 3

    # 7. High B (≥60) with very high D and moderate C → class 3
    if B >= 60 and D > 70 and 30 <= C <= 50:
        return 3

    # 8. High B (≥60) with very low D and moderate C → class 3
    if B >= 60 and D < 10 and 30 <= C <= 50:
        return 3

    # 9. Very high B with moderate C and low E → class 4
    if B > 80 and 30 <= C <= 60 and E < 30:
        return 4

    # 10. Default fallback → class 1
    return 1
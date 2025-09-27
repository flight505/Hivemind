"""
Predictor 15
Generated on: 2025-09-09 03:45:09
Accuracy: 48.90%
"""


# PREDICTOR 15 - Accuracy: 48.90%
# Correct predictions: 4890/10000 (48.90%)

def predict_output(A, B, C, D, E):
    # 1. Very high E together with low C → class 4
    if E >= 95 and C < 30:
        return 4

    # 2. Very low C
    if C <= 10:
        # low B with very low C → class 3
        if B <= 15:
            return 3
        # high B with very low C:
        #   if D is also very high → class 4, otherwise class 1
        if B > 80:
            return 4 if D > 80 else 1
        return 1

    # 3. High B (≥70) with low C and relatively high E → class 4
    if B >= 70 and C < 30 and E > 70:
        return 4

    # 4. High B (≥70) with low‑medium C (30‑69) → class 2
    if B >= 70 and 30 <= C < 70:
        return 2

    # 5. Low‑C & moderate B but very low E → class 4
    if C < 30 and B > 60 and E < 30:
        return 4

    # 6. Very high C (≥75)
    if C >= 75:
        if B > 60:                     # high B
            # when B is not extreme and D is very high → class 3
            if B < 90 and D > 70:
                return 3
            # otherwise high‑C & high‑B → class 2
            return 2
        # low B with very high C → class 1
        return 1

    # 7. Upper‑mid C (70‑74) with high B and very high D → class 3
    if 70 <= C < 75 and B > 60 and D > 70:
        return 3

    # 8. Mid‑high C (65‑74) when not caught above → default to class 1
    if C >= 65:
        return 1

    # 9. Low B (≤15)
    if B <= 15:
        if C < 20:
            return 3
        return 1

    # 10. Default fallback
    return 1
"""
Predictor 14
Generated on: 2025-09-09 03:44:37
Accuracy: 47.09%
"""


# PREDICTOR 14 - Accuracy: 47.09%
# Correct predictions: 4709/10000 (47.09%)

def predict_output(A, B, C, D, E):
    # 1. Very high E
    if E >= 90:
        if C >= 30 and B > 60:
            return 2
        return 4

    # 2. Very high C (≥80)
    if C >= 80:
        # special case: very low B, very low D and low E → class 3
        if B <= 15 and D < 10 and E < 20:
            return 3
        # high C with very low D and low E → class 3
        if D < 5 and E < 10:
            return 3
        # moderate B with very high C → class 4
        if B <= 40:
            return 4
        # extremely high B with very high C → class 2
        if B >= 80:
            return 2

    # 3. High C (70‑79) with very low D (special case)
    if 70 <= C < 75 and D < 15:
        return 1

    # 4. High C (≥70)
    if C >= 70:
        if B > 60:
            return 2
        return 1

    # 5. Very low C (≤10)
    if C <= 10:
        if B <= 15:
            return 3
        if E > 50:
            return 4
        return 3

    # 6. Extremely high D together with low C and medium B
    if D > 90 and C < 30 and B > 40:
        return 4

    # 7. Moderate‑high D with moderate C and higher B
    if D > 70 and C < 45 and B >= 50:
        return 3

    # 8. High B & high E with mid‑range C
    if B > 60 and E > 70 and 30 <= C <= 60:
        return 4

    # 9. Low B rule
    if B <= 15:
        if C < 20:
            return 3
        return 1

    # 10. Very low E with modest C
    if E < 10 and C < 50:
        return 3

    # Default
    return 1
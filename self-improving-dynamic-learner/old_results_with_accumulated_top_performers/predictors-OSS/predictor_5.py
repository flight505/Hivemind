"""
Predictor 5
Generated on: 2025-09-09 03:36:26
Accuracy: 38.91%
"""


# PREDICTOR 5 - Accuracy: 38.91%
# Correct predictions: 3891/10000 (38.91%)

def predict_output(A, B, C, D, E):
    # 1. Low B with relatively high A and at least moderate C → class 1
    if B <= 15 and A > 60 and C >= 20:
        return 1

    # 2. Low B with very high D → class 1
    if B <= 15 and D > 70:
        return 1

    # 3. Low B and moderately/large C → class 4
    if B <= 15 and C >= 40:
        return 4

    # 4. Remaining low‑B cases (very low C) → class 3
    if B <= 15:
        return 3

    # 5. Extremely low E → class 3
    if E <= 5:
        return 3

    # 6. Very high E
    if E >= 80:
        if B > 70:
            # high B together with high E → class 2 (unless D is tiny)
            return 1 if D < 30 else 2
        else:
            return 4

    # 7. High D together with moderate B → class 3
    if D > 80 and B < 50:
        return 3

    # 8. Very high C
    if C > 80:
        if B <= 20:                     # low B + very high C → class 1
            return 1
        elif B > 70:
            if D < 30:                  # low D overrides → class 1
                return 1
            elif D > 70:                # high D + high B + very high C → class 2
                return 2
            else:                       # other cases → class 4
                return 4
        else:
            return 4

    # 9. High C (70‑79) with mid‑high B → class 2
    if 70 <= C < 80 and 60 <= B <= 80:
        return 2

    # 10. Moderate C (30‑69) with high B → class 2
    if 30 <= C < 70 and B > 70:
        return 2

    # default class
    return 1
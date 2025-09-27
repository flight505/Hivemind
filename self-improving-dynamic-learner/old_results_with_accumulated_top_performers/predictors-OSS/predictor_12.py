"""
Predictor 12
Generated on: 2025-09-09 03:43:02
Accuracy: 49.90%
"""


# PREDICTOR 12 - Accuracy: 49.90%
# Correct predictions: 4990/10000 (49.90%)

def predict_output(A, B, C, D, E):
    # 1. Extremely high E → class 4
    if E >= 95:
        return 4

    # 2. Very low C (including the borderline values)
    if C <= 15:
        # high B (or moderately high) with low C → class 4
        if B > 60:
            return 4
        # extremely low C with very low B → class 3
        if B <= 15 and C < 5:
            return 3
        # other low‑C cases → class 1
        return 1

    # 3. Very high C
    if C >= 75:
        # very low D → class 2
        if D < 10:
            return 2
        # very high D and low E → class 3
        if D > 90 and E < 50:
            return 3
        # high B together with very high E → class 2
        if B > 80 and E > 80:
            return 2
        # high B (but not extreme) → class 2 when D extreme, else 1
        if B > 60:
            if D < 20 or D > 80:
                return 2
            return 1
        return 1

    # 4. High‑mid C (60 ≤ C < 75)
    if 60 <= C < 75:
        # high B & very high E → class 2
        if B > 80 and E > 80:
            return 2
        # moderate‑high B with relatively high E and not very low D → class 4
        if B > 40 and E >= 55 and D >= 20:
            return 4
        # moderate‑high B with very low E → class 3
        if B > 40 and E < 10:
            return 3
        return 1

    # 5. Mid/low C (13 ≤ C < 60)
    # high B and very high E → class 2
    if B > 80 and E > 80:
        return 2
    # low B with very low C (still below 20) → class 3
    if B <= 20 and C < 20:
        return 3

    # 6. Default
    return 1
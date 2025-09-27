"""
Predictor 17
Generated on: 2025-09-09 03:46:40
Accuracy: 49.63%
"""


# PREDICTOR 17 - Accuracy: 49.63%
# Correct predictions: 4963/10000 (49.63%)

def predict_output(A, B, C, D, E):
    # 1. Very low C (<=12)
    if C <= 12:
        if B <= 15:
            return 3                     # matches rows with low C & low B
        if E >= 60:
            return 4                     # low C, high E → class 4
        return 1

    # 2. Very high E (>=90)
    if E >= 90:
        if C < 30:
            return 4                     # low C + very high E
        elif C < 50:                     # 30‑49 range
            if D < 20:
                return 2                 # low D pushes to class 2
            return 3                     # otherwise class 3
        else:                             # C >= 50
            if B <= 60:
                return 2                 # high E + lower B
            return 3                     # high E + higher B

    # 3. Very high C (>=70)
    if C >= 70:
        if B >= 80:
            if D > 80:
                return 2                 # high C, very high B and very high D
            return 1                     # otherwise class 1
        if B >= 60:
            return 2                     # moderate‑high B with high C
        return 1                         # low B with high C

    # 4. High‑mid C (65‑69)
    if C >= 65:
        if B >= 80:
            return 1
        if B >= 60:
            return 2
        return 1

    # 5. Mid C (40‑64)
    if C >= 40:
        if B > 80 and E < 50:
            return 4                     # high B but low E
        if B > 80 and E > 80:
            return 2                     # high B and high E
        return 1

    # 6. Low‑mid C (20‑39)
    if C >= 20:
        if B > 60 and E < 30:
            return 3                     # moderate B, very low E
        if B > 80 and E >= 90:
            return 4                     # very high E with high B
        return 1

    # 7. C just below 20 (but >12)
    if C < 20:
        if B <= 15:
            return 3
        if E >= 70:
            return 4
        return 1

    # default
    return 1
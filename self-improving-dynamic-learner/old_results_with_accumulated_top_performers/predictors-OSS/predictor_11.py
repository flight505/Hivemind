"""
Predictor 11
Generated on: 2025-09-09 03:42:16
Accuracy: 50.15%
"""


# PREDICTOR 11 - Accuracy: 50.15%
# Correct predictions: 5015/10000 (50.15%)

def predict_output(A, B, C, D, E):
    # 1. Very high C (>=75)
    if C >= 75:
        if B > 60:
            # 2 is favoured when D is very low or very high
            if D < 20 or D > 80:
                return 2
            else:
                return 1
        else:
            return 1

    # 2. Extremely high E (>=95) → class 4
    if E >= 95:
        return 4

    # 3. Very low C (<=10)
    if C <= 10:
        # low C with very low B and relatively high E → class 4
        if E >= 60 and B <= 10:
            return 4
        # low C with low B → class 3
        if B <= 15:
            return 3
        return 1

    # 4. Medium‑high C (60‑74)
    if 60 <= C < 75:
        # moderate B and relatively high E → class 4
        if B <= 40 and E >= 55:
            return 4
        # moderate B and very low E → class 3
        if B <= 40 and E < 10:
            return 3

    # 5. Low B with modest C → class 3
    if B <= 20 and C < 40:
        return 3

    # 6. High B with C in the 20‑30 band
    if B > 80 and 20 <= C <= 30:
        # when D is not too high → class 2, otherwise fall back to 1
        if D < 80:
            return 2
        else:
            return 1

    # 7. Default fallback
    return 1
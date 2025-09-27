"""
Predictor 13
Generated on: 2025-09-09 03:43:35
Accuracy: 50.20%
"""


# PREDICTOR 13 - Accuracy: 50.20%
# Correct predictions: 5020/10000 (50.20%)

def predict_output(A, B, C, D, E):
    # 1. Very low C
    if C <= 5:
        if B <= 15:
            return 3
        else:
            return 1

    # 2. Very high C with low B → class 4
    if C >= 80 and B <= 15:
        return 4

    # 3. High C with high B (C > 70, B >= 60) → class 2,
    #    except when C is very high (>85) and E is very low (<=10) → class 1
    if C > 70 and B >= 60:
        if C > 85 and E <= 10:
            return 1
        return 2

    # 4. Low B with modest C → class 3
    if B <= 15 and C < 20:
        return 3

    # 5. High E with low C and low B → class 4
    if E > 80 and C <= 30 and B <= 20:
        return 4

    # 6. C in 30‑39 range with high B and high E → class 4
    if 30 <= C < 40 and B > 60 and E > 60:
        return 4

    # 7. Very high E with low → class 4
    if E >= 95 and C <= 30:
        return 4

    # Default
    return 1
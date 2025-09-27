"""
Predictor 4
Generated on: 2025-09-09 03:35:26
Accuracy: 37.92%
"""


# PREDICTOR 4 - Accuracy: 37.92%
# Correct predictions: 3792/10000 (37.92%)

def predict_output(A, B, C, D, E):
    # 1. Small B values tend to be class 3
    if B <= 20:
        return 3

    # 2. Very high E drives several classes
    if E > 85:
        # when both B and C are very high, class 1
        if B > 80 and C > 80:
            return 1
        # high E together with high D and high C gives class 3
        if D > 80 and C > 80:
            return 3
        # otherwise moderate‑high C with high E is class 2
        if C > 60:
            return 2
        # low C with very high E is class 4
        return 4

    # 3. High C values (≥75) distinguish classes 1,2,3,4
    if C > 75:
        # very high B with high D stays in class 2
        if B >= 80 and D > 80:
            return 2
        # very high B but not high D is class 1
        if B >= 80:
            return 1
        # very high D together with very high C is class 3
        if D > 80 and C > 80:
            return 3
        # very low D with high C is class 3
        if D < 10:
            return 3
        # default for high C
        return 2

    # 4. Very low C values
    if C < 10:
        if B <= 15:
            return 3
        return 1

    # 5. High D with moderate B and not‑too‑high C gives class 3
    if D > 80 and B > 30 and B < 90 and C < 40:
        return 3

    # 6. Default class
    return 1
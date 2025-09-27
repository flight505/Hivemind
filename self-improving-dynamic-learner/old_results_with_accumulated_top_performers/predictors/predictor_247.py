"""
Predictor 247
Generated on: 2025-09-09 06:09:33
Accuracy: 42.25%
"""


# PREDICTOR 247 - Accuracy: 42.25%
# Correct predictions: 4225/10000 (42.25%)

def predict_output(A, B, C, D, E):
    high_A = A > 70
    high_B = B > 70
    high_C = C > 60
    high_D = D > 70
    high_E = E > 80
    low_B = B < 25
    low_C = C < 25
    low_D = D < 20
    if high_C and low_B:
        return 4
    if high_E:
        if C > 80:
            return 2
        elif A + B + C < 60:
            return 2
        else:
            return 4
    if high_B and C < 20:
        return 4
    if high_B:
        if high_A and low_C:
            return 1
        else:
            return 2
    if high_D and C < 15 and B < 50:
        if A >= 85:
            return 4
        else:
            return 3
    if high_A and low_B and low_C and not high_D:
        if E < 50:
            return 3
        else:
            return 4
    if low_B and low_C:
        return 3
    if min(A, B, C, D, E) > 40 and max(A, B, C, D, E) < 80:
        return 1
    return 1
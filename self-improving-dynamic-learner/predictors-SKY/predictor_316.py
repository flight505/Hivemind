"""
Predictor 316
Generated on: 2025-09-09 15:25:04
Accuracy: 50.90%
"""


# PREDICTOR 316 - Accuracy: 50.90%
# Correct predictions: 5090/10000 (50.90%)

def predict_output(A, B, C, D, E):
    if C < 30 and E > 70:
        return 4
    if B > 60 and C > 60:
        if D < 20 and A > 70:
            return 1
        else:
            return 2
    if B < 30 and C < 30:
        if D > 80 and E < 20:
            return 1
        else:
            return 3
    if B > 80 and C < 30 and E > 60:
        return 4
    if E > 90:
        return 4
    if B > 70 and C < 25 and E < 30:
        return 1
    if B > 90 and C < 25:
        return 1
    if D > 90 and B < 25 and C < 25 and E < 30:
        return 1
    if C > 90 and E > 90 and B < 30:
        return 4
    if B > 70 and C < 45 and E < 30 and D > 70:
        return 3
    if B < 20 and C > 70 and E < 10:
        return 3
    if B < 40 and C > 50 and E < 20:
        return 3
    return 1
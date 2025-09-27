"""
Predictor 311
Generated on: 2025-09-09 15:21:48
Accuracy: 50.97%
"""


# PREDICTOR 311 - Accuracy: 50.97%
# Correct predictions: 5097/10000 (50.97%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if B > 90 and C > 90:
        return 2
    if D > 90 and B < 25 and C < 25 and E < 30:
        return 1
    if C > 90 and E > 90 and B < 30:
        return 4
    if B > 80 and C < 30 and E > 60:
        return 4
    if B > 60 and C > 70 and E >= 70:
        if A >= 50:
            return 1
        else:
            return 2
    if B < 30 and C > 60 and D < 50:
        return 4
    if B > 60 and C > 50 and E < 20:
        return 4
    if B < 25 and C < 40 and D > 60 and E < 20:
        return 4
    if B > 65 and C < 40 and A > 50:
        return 2
    if B < 20 and C < 20:
        return 3
    if B > 60 and C < 20 and D < 50 and E < 50:
        return 3
    if B < 50 and C > 60 and D < 20:
        return 3
    if B < 20 and C < 40 and D < 30:
        return 3
    return 1
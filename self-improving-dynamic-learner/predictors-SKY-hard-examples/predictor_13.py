"""
Predictor 13
Generated on: 2025-09-09 17:13:17
Accuracy: 47.57%
"""


# PREDICTOR 13 - Accuracy: 47.57%
# Correct predictions: 4757/10000 (47.57%)

def predict_output(A, B, C, D, E):
    if D > 90 and B > 80 and C > 75:
        return 3
    if B < 25 and C < 25:
        if E < 50:
            return 3
        else:
            return 1
    if B < 20 and C > 50:
        return 3
    if B > 60 and C > 75 and A < 60 and E > 40:
        return 2
    if B > 80 and E > 70 and C < 60:
        return 2
    if B > 50 and C < 25 and E < 30 and D < 25:
        return 3
    if A < 10 and B < 35 and 25 < C < 45 and E < 20:
        return 4
    if D > 90 and C < 30:
        return 3
    if E > 90 and C < 30:
        return 4
    if E < 25 and C > 40 and (B < 60 or C > 80):
        return 4
    if B > 60 and E > 90 and D > 20:
        return 2
    if B > 55 and E > 90 and C < 60:
        return 2
    if B > 60 and C > 55 and C < 70 and E < 30:
        return 2
    return 1
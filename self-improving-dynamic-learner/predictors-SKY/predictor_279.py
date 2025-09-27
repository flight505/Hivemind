"""
Predictor 279
Generated on: 2025-09-09 14:59:57
Accuracy: 45.63%
"""


# PREDICTOR 279 - Accuracy: 45.63%
# Correct predictions: 4563/10000 (45.63%)

def predict_output(A, B, C, D, E):
    if B > 90 and C >= 70 and D < 15 and E > 70:
        return 1
    if B < 20 and C < 20:
        return 3
    if E > 90 and C < 40:
        return 4
    if B > 80 and E > 90 and D < 25:
        return 4
    if B < 20 and C < 10 and E > 75:
        return 4
    if B > 60 and C > 70 and E < 25:
        return 4
    if B > 70 and C < 5 and D < 30:
        return 3
    if B < 15 and C > 45 and E < 30:
        return 3
    if B > 55 and C > 35 and D < 30:
        return 3
    if B < 20 and C > 40 and D > 60:
        return 3
    if A < 10 and B > 45 and C < 10 and E > 70:
        return 2
    if B > 60 and C > 70:
        return 2
    if B > 70 and C < 25 and E < 30:
        return 1
    if A > 70 and B > 40 and C < 40 and E < 30:
        return 1
    return 1
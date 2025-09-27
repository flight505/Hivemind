"""
Predictor 53
Generated on: 2025-09-09 23:21:45
Accuracy: 55.52%
"""


# PREDICTOR 53 - Accuracy: 55.52%
# Correct predictions: 5552/10000 (55.52%)

def predict_output(A, B, C, D, E):
    if D > 75 and E < 25:
        return 3
    if A < 10 and B > 70 and E < 20:
        return 4
    if C < 20 and D > 50 and E >= 25:
        return 4
    if A > 30 and B > 30 and C > 30 and A < 60 and B < 60 and C < 60 and D < 40 and E < 30:
        return 4
    if B > 70 and C < 30 and D > 80 and E > 80:
        return 4
    if A < 15 and B < 30 and D < 35 and E > 45:
        return 4
    if A > 75 and B > 60 and C < 15 and D > 55:
        return 4
    if C > 85 and B < 35 and E < 15:
        return 4
    if E > 80 and D < 40:
        return 4
    if B < 15 and E < 20:
        return 4
    if A > 90 and E < 10:
        return 2
    if B > 90:
        return 2
    if B < 10 and C > 90:
        if A > 60:
            return 4
        elif A < 40:
            return 2
    if A < 5 and C < 10:
        return 3
    else:
        return 1
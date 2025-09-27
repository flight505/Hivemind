"""
Predictor 39
Generated on: 2025-09-09 23:21:45
Accuracy: 53.25%
"""


# PREDICTOR 39 - Accuracy: 53.25%
# Correct predictions: 5325/10000 (53.25%)

def predict_output(A, B, C, D, E):
    if A < 10 and B > 70 and E < 20:
        return 4
    if C < 20 and D > 50 and E > 80:
        return 4
    if C > 70 and B < 30 and A > 10:
        return 4
    if C > 60 and E < 10:
        return 4
    if C < 20 and E > 70:
        return 4
    if B < 15 and E < 20:
        return 4
    if E > 80 and D < 40:
        return 4
    if B > 80 and D > 80:
        return 3
    if A < 5 and C < 10:
        return 3
    if B < 10 and C > 90:
        if A > 60:
            return 4
        else:
            return 2
    if B < 10 and D > 80:
        return 3
    if B > 90 and C > 70:
        return 2
    if A > 90 and E < 10:
        return 2
    else:
        return 1
"""
Predictor 36
Generated on: 2025-09-09 23:21:45
Accuracy: 50.64%
"""


# PREDICTOR 36 - Accuracy: 50.64%
# Correct predictions: 5064/10000 (50.64%)

def predict_output(A, B, C, D, E):
    if A < 10 and B > 70 and E < 20:
        return 4
    if C < 15 and D > 80:
        return 4
    if C > 70 and B < 30 and A > 10:
        return 4
    if C < 15 and D < 30 and E > 70:
        return 4
    if C > 60 and D < 40 and E < 10:
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
    if B > 90:
        return 2
    if A > 90 and E < 10:
        return 2
    if B < 10 and D > 80:
        return 3
    else:
        return 1
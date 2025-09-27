"""
Predictor 37
Generated on: 2025-09-09 23:21:45
Accuracy: 54.74%
"""


# PREDICTOR 37 - Accuracy: 54.74%
# Correct predictions: 5474/10000 (54.74%)

def predict_output(A, B, C, D, E):
    if A < 10 and B > 70 and E < 20:
        return 4
    if C < 15 and E > 70:
        return 4
    if E < 5 and C > 60:
        return 4
    if C > 70 and D < 20:
        return 4
    if C < 20 and D > 70:
        return 4
    if C > 70 and B < 30 and E < 40:
        return 4
    if B < 15 and E < 20:
        return 4
    if E > 80 and D < 40:
        return 4
    if B > 80 and D > 80:
        return 3
    if C > 90 and D > 90 and B > 20:
        return 3
    if A < 5 and C < 10:
        return 3
    if B < 10 and C > 90:
        if A > 60:
            return 4
        else:
            return 2
    if B > 90 and C > 50:
        return 2
    if A > 90 and E < 10:
        return 2
    if B < 10 and D > 80:
        return 3
    else:
        return 1
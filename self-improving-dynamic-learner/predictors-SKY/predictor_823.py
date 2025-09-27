"""
Predictor 823
Generated on: 2025-09-09 21:14:05
Accuracy: 50.56%
"""


# PREDICTOR 823 - Accuracy: 50.56%
# Correct predictions: 5056/10000 (50.56%)

def predict_output(A, B, C, D, E):
    if E > 90:
        if C < 30:
            return 4
        else:
            return 1
    if B > 60 and C < 20 and E > 20:
        return 3
    if E < 20 and B > 60:
        return 1
    if D > 90 and E > 70:
        return 3
    if A > 80 and B > 80 and C > 60:
        return 1
    if B > 60 and C > 40:
        return 2
    if B < 20 and C < 20:
        return 3
    if D > 70:
        return 1
    if E < 10 and B < 50 and C < 40:
        return 3
    return 1
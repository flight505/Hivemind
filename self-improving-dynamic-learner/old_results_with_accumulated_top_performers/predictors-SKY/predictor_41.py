"""
Predictor 41
Generated on: 2025-09-09 04:10:02
Accuracy: 52.39%
"""


# PREDICTOR 41 - Accuracy: 52.39%
# Correct predictions: 5239/10000 (52.39%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40 and C < 30:
        return 4
    if C >= 70 and B > 60:
        if A >= 50:
            return 1
        else:
            return 2
    if C >= 70 and D < 30 and B <= 60:
        return 4
    if D > 90 and C > 50:
        return 3
    if C > 50 and E < 30 and D < 60:
        return 4
    if B < 20 and C < 20 and E > 60:
        return 2
    if B < 20 and C < 50 and D > 70:
        return 3
    if B > 60 and C < 40 and E > 70:
        return 2
    if B > 30 and D > 80 and C < 40 and E < 20:
        return 3
    if C < 20 and B < 20:
        return 3
    return 1
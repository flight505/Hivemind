"""
Predictor 617
Generated on: 2025-09-09 18:45:58
Accuracy: 54.62%
"""


# PREDICTOR 617 - Accuracy: 54.62%
# Correct predictions: 5462/10000 (54.62%)

def predict_output(A, B, C, D, E):
    if C < 15 and B < 50:
        return 3
    if E > 90 and D > 80 and C < 60:
        return 3
    if B > 40 and C > 40 and D < 5:
        return 3
    if E > 90 and C < 25:
        return 4
    if B > 90 and C < 40 and E > 90:
        return 4
    if C > 80 and D < 20:
        return 4
    if B > 65 and C < 30 and E > 60:
        return 4
    if A > 70 and B < 20 and E >= 70 and D < 15:
        return 4
    if C > 50 and B < 10 and E < 20:
        return 4
    if B > 60 and C > 70 and E > 60:
        return 2
    if B > 60 and C > 70 and E < 30:
        return 4
    return 1
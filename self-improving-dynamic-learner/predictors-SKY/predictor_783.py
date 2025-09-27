"""
Predictor 783
Generated on: 2025-09-09 20:47:43
Accuracy: 54.66%
"""


# PREDICTOR 783 - Accuracy: 54.66%
# Correct predictions: 5466/10000 (54.66%)

def predict_output(A, B, C, D, E):
    if E > 80 and C < 30:
        if B < 40:
            return 4
        else:
            return 2
    if C < 25 and D > 90 and E < 20:
        return 4
    if B > 70 and C < 25 and E > 60:
        return 4
    if E < 10 and B > 55 and C > 40:
        return 4
    if B < 20 and C < 25:
        return 3
    if 55 < B < 65 and 50 < C < 60 and D > 70 and E > 70:
        return 3
    if B > 75 and C > 65 and D < 20:
        return 1
    if B > 60 and C > 65 and E > 60:
        return 2
    if B < 20 and C < 30 and E > 60:
        return 2
    return 1
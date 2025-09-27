"""
Predictor 7
Generated on: 2025-09-09 12:08:22
Accuracy: 49.19%
"""


# PREDICTOR 7 - Accuracy: 49.19%
# Correct predictions: 4919/10000 (49.19%)

def predict_output(A, B, C, D, E):
    if C < 30 and E > 75 and B < 60:
        return 4
    if B > 60 and C > 70 and D < 25 and E < 30:
        return 4
    if D < 20 and E > 85:
        return 4
    if B > 50 and C < 30 and E > 60 and D > 30:
        return 4
    if B < 20:
        if C < 15:
            return 3
        else:
            return 1
    if C < 15:
        return 3
    if 40 < B < 50 and C > 40 and E < 40:
        return 3
    if B > 50 and C < 30 and E > 80:
        return 2
    if B > 50 and C > 60 and E < 60:
        return 3
    if B > 50 and C > 72 and E > 55:
        return 2
    return 1
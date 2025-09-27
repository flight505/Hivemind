"""
Predictor 313
Generated on: 2025-09-09 15:23:10
Accuracy: 58.58%
"""


# PREDICTOR 313 - Accuracy: 58.58%
# Correct predictions: 5858/10000 (58.58%)

def predict_output(A, B, C, D, E):
    if B > 60 and C > 60:
        if A < 15 or A > 50:
            return 1
        else:
            return 2
    if E > 90:
        return 4
    if B > 90 and C > 25 and E >= 70:
        return 2
    if B < 20 and C < 20:
        if E > 70:
            return 4
        else:
            return 3
    if B < 15 and C > 25 and E < 50:
        return 4
    if C < 10 and B < 50:
        return 3
    if E > 80 and C < 45:
        return 4
    if B > 80 and C < 30 and E > 60:
        return 4
    if D > 90 and B < 25 and C < 25 and E < 30:
        return 1
    if C > 90 and E > 90 and B < 30:
        return 4
    return 1
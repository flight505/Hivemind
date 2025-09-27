"""
Predictor 68
Generated on: 2025-09-09 12:50:51
Accuracy: 53.45%
"""


# PREDICTOR 68 - Accuracy: 53.45%
# Correct predictions: 5345/10000 (53.45%)

def predict_output(A, B, C, D, E):
    if C < 30 and E > 70 and B < 40:
        return 4
    if B > 60 and C < 10 and E > 60:
        return 4
    if C > 90 and E < 20:
        return 4
    if B > 80 and E > 80 and C < 30:
        return 4
    if B < 20 and C > 70 and D < 50 and E > 60:
        return 4
    if B < 20 and C < 20 and E > 10:
        return 3
    if A > 80 and B > 50 and C < 30 and E < 60:
        return 3
    if 40 < C < 50 and B > 50 and E > 50:
        return 3
    if B > 40 and C < 30 and E < 30:
        return 3
    if B > 60 and C >= 75 and E >= 70:
        return 2
    if B > 45 and 40 < C < 60 and E > 70 and D < 50:
        return 2
    if A + B > 160 and C < 40 and E < 45:
        return 2
    return 1
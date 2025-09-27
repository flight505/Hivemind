"""
Predictor 334
Generated on: 2025-09-09 15:34:47
Accuracy: 55.73%
"""


# PREDICTOR 334 - Accuracy: 55.73%
# Correct predictions: 5573/10000 (55.73%)

def predict_output(A, B, C, D, E):
    if B > 90 and C > 90 and D > 50:
        return 2
    if B > 90 and C > 90 and D <= 50:
        return 1
    if A > 90 and B < 10 and C < 5 and D > 90:
        return 4
    if B < 30 and C > 90:
        return 4
    if C < 30 and E > 70 and B < 80:
        return 4
    if B > 80 and C < 30 and E > 60:
        return 4
    if B + C < 10 and E > 90:
        return 4
    if E > 90 and C > 70:
        return 4
    if C > 70 and E < 20:
        return 4
    if B < 20 and C < 15:
        return 3
    if C < 15 and D > 60 and B > 40:
        return 3
    if B > 60 and C < 5 and D < 10:
        return 3
    if B < 30 and C < 25 and E < 40:
        return 3
    if B > 60 and B < 90 and C > 70 and A < 50:
        return 2
    if B > 60 and E > 55 and C < 40:
        return 2
    if A + B > 160 and C < 40 and E > 50:
        return 2
    if B > 90 and C > 60:
        return 1
    if B > 60 and C > 60 and A > 50:
        return 1
    if D > 90 and B < 25 and C < 25 and E < 30:
        return 1
    if B > 50 and C < 25 and E < 5:
        return 1
    return 1
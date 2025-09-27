"""
Predictor 867
Generated on: 2025-09-09 21:36:34
Accuracy: 57.65%
"""


# PREDICTOR 867 - Accuracy: 57.65%
# Correct predictions: 5765/10000 (57.65%)

def predict_output(A, B, C, D, E):
    if D < 10 and E > 80:
        return 1
    if C > 85 and B > 60 and E > 40:
        return 1
    if C > 80 and B > 80 and E < 60:
        return 1
    if D > 80 and B < 30 and C < 20:
        return 1
    if B > 90 and 30 <= C < 50 and E < 30:
        return 1
    if B > 60 and C > 40 and E > 80 and D < 25:
        return 4
    if B > 50 and C > 80 and D > 90 and E < 50:
        return 3
    if B > 90 and C > 90 and E < 10:
        return 1
    if B > 70 and C > 60 and E > 80:
        return 1
    if A > 80 and B > 70 and C < 50 and E < 50:
        return 1
    if B > 90 and 30 <= C < 50 and E > 50:
        return 2
    if A > 90 and B < 30 and C < 20 and E < 10:
        return 1
    if E > 90 and C > 50 and B < 60:
        return 1
    if B < 10 and C < 40 and E < 10:
        return 3
    if B > 90 and C > 90:
        return 2
    if C > 90 and E > 90 and B < 30:
        return 4
    if C > 90 and E > 90 and B < 70:
        return 1
    if C > 90 and E > 90 and B > 50:
        return 2
    if D > 90 and B < 25 and C < 25 and E < 30:
        return 1
    if B > 80 and C < 30 and E > 60:
        return 4
    if B < 15 and C < 25 and E > 75:
        return 4
    if A > 80 and B > 65 and C < 40 and E < 10:
        return 1
    if B < 10 and C > 75 and E < 10:
        return 1
    if B > 75 and C < 50 and E < 15:
        return 1
    if C > 80 and B > 55 and D > 65 and E < 55:
        return 3
    return 1
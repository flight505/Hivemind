"""
Predictor 874
Generated on: 2025-09-09 21:39:46
Accuracy: 49.31%
"""


# PREDICTOR 874 - Accuracy: 49.31%
# Correct predictions: 4931/10000 (49.31%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B < 30 and C > 60:
        if E < 20:
            return 3
        else:
            return 4
    if B < 10 and C > 50:
        return 3
    if C < 15 and E > 50:
        return 4
    if B < 15 and E > 50:
        return 2
    if A > 90 and B > 70 and C < 40:
        return 4
    if B < 5 and C > 50:
        return 4
    if C > 90 and B > 90 and E > 90:
        return 1
    if B > 50 and E < 5 and D < 25:
        return 3
    if B > 70 and C < 45 and D > 90:
        return 3
    if B > 60 and C < 30:
        return 4
    if E > 90 and C > 50 and B < 60:
        return 1
    if B > 70 and C > 60 and E > 80:
        return 1
    if A > 80 and B > 70 and C < 50 and E < 50:
        return 1
    if B > 90 and 30 <= C < 50 and E > 50:
        return 2
    if B > 60 and C > 60 and A < 40:
        return 2
    return 1
"""
Predictor 728
Generated on: 2025-09-09 20:05:56
Accuracy: 58.52%
"""


# PREDICTOR 728 - Accuracy: 58.52%
# Correct predictions: 5852/10000 (58.52%)

def predict_output(A, B, C, D, E):
    if B > 90 and C < 25:
        return 1
    if B < 30 and C < 25 and E > 90:
        return 1
    if C < 25 and E > 90:
        return 4
    if B < 10 and C > 80:
        return 1
    if B < 20 and C < 20 and D > 90:
        return 3
    if B < 25 and C < 25 and E < 30:
        return 3
    if B > 80 and C < 40 and D > 80 and A > 10:
        return 3
    if B > 90 and C > 90 and D > 90:
        return 3
    if B > 90 and 45 < C < 55:
        return 2
    if A < 10 and B > 80 and C < 40 and D > 80:
        return 1
    if B > 90 and 60 < C < 75 and D < 20:
        return 1
    if 20 < B < 40 and C < 20 and D > 90:
        return 1
    if 20 < B < 40 and C > 50 and D > 70 and E < 40:
        return 1
    if A < 40 and B > 60 and C > 70:
        return 2
    if B > 60 and C > 40 and E > 80 and D < 25:
        return 4
    if D > 80 and B < 30 and C < 20:
        return 1
    if B > 90 and 30 <= C < 50 and E > 50:
        return 2
    if C > 90 and E > 90 and B < 30:
        return 4
    if B > 80 and C < 30 and E > 60:
        return 4
    if B < 40 and C > 50 and E < 50 and D < 20:
        return 3
    if B > 70 and C < 45 and E < 30 and D > 70:
        return 3
    return 1
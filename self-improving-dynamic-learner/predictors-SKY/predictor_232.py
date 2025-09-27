"""
Predictor 232
Generated on: 2025-09-09 14:29:34
Accuracy: 53.39%
"""


# PREDICTOR 232 - Accuracy: 53.39%
# Correct predictions: 5339/10000 (53.39%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    if A > 95 and B < 60 and C < 30 and E > 90:
        return 3
    if B > 80 and C < 20 and D < 20 and E < 25:
        return 3
    if E > 90 and C < 25:
        return 4
    if C > 90 and E > 90 and B > 70:
        return 4
    if C > 80 and E < 20:
        return 4
    if B < 15 and C > 60:
        return 4
    if C > 60 and E < 5 and D > 60:
        return 4
    if B < 25 and C > 50 and E < 15 and D > 60:
        return 4
    if B < 25 and 35 < C < 45 and E > 50 and D < 30:
        return 4
    if B > 80 and C < 10 and D > 90 and E < 10:
        return 4
    if A < 40 and B > 60 and C > 55:
        return 2
    if A < 35 and B < 45 and C < 45 and E > 90:
        return 2
    if A > 90 and B > 80 and C > 40 and E < 15 and D > 50:
        return 2
    if 50 < A < 60 and B > 65 and 45 < C < 55 and E < 5:
        return 2
    return 1
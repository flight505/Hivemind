"""
Predictor 489
Generated on: 2025-09-09 17:15:28
Accuracy: 52.80%
"""


# PREDICTOR 489 - Accuracy: 52.80%
# Correct predictions: 5280/10000 (52.80%)

def predict_output(A, B, C, D, E):
    if C > 80 and E < 40:
        return 4
    if B > 80 and C < 10 and E > 50:
        return 4
    if B < 10 and C > 80:
        return 4
    if E < 20 and D > 60 and B < 40 and C < 50:
        return 4
    if E > 90 and C < 30:
        return 4
    if B > 70 and C > 80 and E < 25:
        return 3
    if B > 80 and C < 10 and D > 90 and E < 40:
        return 3
    if B < 20 and C < 20:
        return 3
    if A < 30 and B > 60 and C > 70:
        return 2
    if B > 70 and C > 50 and E < 30 and A >= 30:
        return 2
    if C > 70 and D > 90 and E > 80:
        return 1
    if B > 60 and C > 60 and E > 60 and D > 70:
        return 1
    if B > 90 and 30 <= C < 50 and E < 30:
        return 1
    if B > 70 and C > 60 and E > 80:
        return 1
    if C < 20 and E < 20:
        return 1
    if B > 90 and C > 70 and D < 20:
        return 1
    if B < 30 and C > 50 and D > 70:
        return 1
    if B > 90 and C < 25 and D > 80:
        return 1
    return 1
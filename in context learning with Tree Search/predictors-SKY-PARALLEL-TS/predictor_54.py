"""
Predictor 54
Generated on: 2025-09-09 23:21:45
Accuracy: 51.50%
"""


# PREDICTOR 54 - Accuracy: 51.50%
# Correct predictions: 5150/10000 (51.50%)

def predict_output(A, B, C, D, E):
    if D > 70 and E < 25:
        return 3
    if A > 90 and E < 10:
        return 2
    if B > 90:
        return 2
    if C > 90 and D < 20:
        return 2
    if B < 10 and C > 90 and D < 50:
        return 2
    if A < 10 and B > 70 and E < 20:
        return 4
    if C < 25 and D > 50 and E > 40:
        return 4
    if C > 70 and B < 30 and E < 40:
        return 4
    if B < 15 and E < 20:
        return 4
    if E > 80 and D < 40:
        return 4
    if C > 80 and E < 15:
        return 4
    if min(A, B, C) > 30 and max(A, B, C) < 60 and D < 40 and E < 30:
        return 4
    if A < 20 and B < 30 and E > 40:
        return 4
    if A < 5 and C < 10:
        return 3
    else:
        return 1
"""
Predictor 322
Generated on: 2025-09-09 15:28:29
Accuracy: 58.40%
"""


# PREDICTOR 322 - Accuracy: 58.40%
# Correct predictions: 5840/10000 (58.40%)

def predict_output(A, B, C, D, E):
    if A < 40 and B > 60 and C > 70:
        return 2
    if A < 40 and B > 80 and 40 < C < 60 and E > 60:
        return 2
    if A < 50 and B > 80 and C < 30 and E > 70:
        return 2
    if B < 20 and D < 20 and E > 60:
        return 2
    if C < 30 and E > 70 and B < 50:
        return 4
    if B < 20 and C < 20:
        return 3
    if B < 40 and C > 50 and D < 20:
        return 3
    if A > 80 and B > 80 and C > 60:
        return 1
    if B < 20 and C > 70:
        return 1
    if B > 70 and C < 40 and E < 30:
        return 1
    if A > 90 and C < 10:
        return 1
    if B > 60 and C > 70 and E < 30:
        return 1
    return 1
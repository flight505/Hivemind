"""
Predictor 281
Generated on: 2025-09-09 15:00:47
Accuracy: 44.92%
"""


# PREDICTOR 281 - Accuracy: 44.92%
# Correct predictions: 4492/10000 (44.92%)

def predict_output(A, B, C, D, E):
    if B > 80 and C < 30 and E > 60:
        return 4
    if E > 90 and C < 40:
        return 4
    if A > 90 and E > 80 and C > 50:
        return 4
    if B > 70 and E > 70 and C > 40:
        return 4
    if B < 10 and E < 10:
        return 4
    if B < 20 and C < 20:
        return 3
    if C > 50 and B < 20:
        return 3
    if B > 70 and C < 45 and E < 30 and D > 70:
        return 3
    if B > 60 and C > 60:
        return 2
    if B > 90 and C > 60 and E < 30:
        return 1
    if C > 60 and E < 30:
        return 1
    if B > 70 and C < 25 and E < 30:
        return 1
    if A > 70 and B > 40 and C < 40 and E < 30:
        return 1
    return 1
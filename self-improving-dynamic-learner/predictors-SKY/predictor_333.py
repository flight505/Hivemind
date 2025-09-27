"""
Predictor 333
Generated on: 2025-09-09 15:33:48
Accuracy: 58.93%
"""


# PREDICTOR 333 - Accuracy: 58.93%
# Correct predictions: 5893/10000 (58.93%)

def predict_output(A, B, C, D, E):
    if A > 90 and B < 15 and C < 5 and D > 90:
        return 4
    if B < 30 and C > 90:
        return 4
    if C < 40 and E > 60:
        return 4
    if B > 80 and 45 < C < 55 and D > 80 and E > 70:
        return 3
    if A < 20 and B > 80 and C > 25:
        return 2
    if B > 60 and C > 60 and A > 50:
        return 1
    if B > 60 and C > 60 and A < 50:
        return 2
    if B > 70 and C < 10:
        return 3
    if B < 20 and C < 20 and D > 80:
        return 3
    if B > 20 and B < 30 and C < 20 and D > 80 and E < 20:
        return 1
    if B < 30 and C < 20:
        return 3
    return 1
"""
Predictor 574
Generated on: 2025-09-09 18:16:47
Accuracy: 58.98%
"""


# PREDICTOR 574 - Accuracy: 58.98%
# Correct predictions: 5898/10000 (58.98%)

def predict_output(A, B, C, D, E):
    if E > 80 and D < 30 and C < 40:
        return 4
    if B < 20 and C < 25 and E > 70:
        return 4
    if B < 40 and C < 20 and D > 80 and E < 30 and A > 50:
        return 4
    if A > 90 and B > 60 and C < 20 and D > 70:
        return 4
    if B > 80 and C < 30 and E > 70 and D > 50:
        return 2
    if A < 50 and B > 60 and C > 70 and E >= 70:
        return 2
    if B < 20 and C < 30 and E > 60:
        return 2
    if B + C + E < 60:
        return 3
    return 1
"""
Predictor 817
Generated on: 2025-09-09 21:10:41
Accuracy: 58.98%
"""


# PREDICTOR 817 - Accuracy: 58.98%
# Correct predictions: 5898/10000 (58.98%)

def predict_output(A, B, C, D, E):
    if E > 90 and C < 30:
        return 4
    if C < 15 and E > 80:
        return 4
    if C < 15 and D > 60 and B > 30:
        return 4
    if B > 70 and C < 15:
        return 2
    if B > 60 and C > 70 and A < 50:
        return 2
    if B > 90 and C > 50 and A < 40:
        return 2
    if B < 20 and C < 20:
        return 3
    if C < 15 and B > 50:
        return 3
    if C > 70 and E < 10:
        return 3
    if B < 40 and C < 30 and E < 40 and D < 50:
        return 3
    return 1
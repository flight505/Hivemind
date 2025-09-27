"""
Predictor 816
Generated on: 2025-09-09 21:09:52
Accuracy: 51.24%
"""


# PREDICTOR 816 - Accuracy: 51.24%
# Correct predictions: 5124/10000 (51.24%)

def predict_output(A, B, C, D, E):
    if E > 90 and C < 30:
        return 4
    if B > 70 and C < 15:
        return 2
    if B > 90 and C > 50 and E < 60:
        return 2
    if C > 90 and E > 70 and B < 30:
        return 2
    if B > 55 and C > 50 and A < 50:
        return 2
    if B > 60 and C > 70 and A < 40:
        return 2
    if B < 20 and C < 15:
        return 3
    if B < 20 and E < 30:
        return 3
    if B < 40 and D > 70 and E > 70:
        return 3
    return 1
"""
Predictor 662
Generated on: 2025-09-09 19:17:10
Accuracy: 48.12%
"""


# PREDICTOR 662 - Accuracy: 48.12%
# Correct predictions: 4812/10000 (48.12%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15 and E < 40:
        return 3
    if B < 20 and C < 30 and E > 50:
        return 4
    if B < 20 and C > 60 and E > 40:
        return 4
    if B < 20 and C > 50 and D > 50 and E < 10:
        return 4
    if B > 50 and C < 30 and E > 60:
        return 4
    if B > 60 and C > 75 and E > 65:
        return 2
    if B > 60 and C < 40 and E > 80:
        return 2
    if C > 80 and B > 40 and E < 40:
        return 3
    if B > 40 and C < 20 and E < 50:
        return 3
    if B < 40 and D > 80 and E > 60:
        return 3
    if E > 90:
        return 4
    return 1
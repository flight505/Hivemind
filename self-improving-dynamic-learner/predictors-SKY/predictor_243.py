"""
Predictor 243
Generated on: 2025-09-09 14:35:10
Accuracy: 50.71%
"""


# PREDICTOR 243 - Accuracy: 50.71%
# Correct predictions: 5071/10000 (50.71%)

def predict_output(A, B, C, D, E):
    if B < 16 and C < 13 and E < 40:
        return 3
    if E >= 90:
        return 4
    if B > 80 and C < 40 and E > 60:
        return 4
    if C > 80 and B > 40 and E < 20:
        return 4
    if B < 20 and C > 60 and E > 50:
        return 4
    if B > 50 and C > 60 and E < 10:
        return 4
    if B < 30 and C > 50 and E < 20 and D > 60:
        return 4
    if B < 25 and C > 35 and E > 50 and D < 30:
        return 4
    if B > 80 and C < 10 and E < 10 and D > 90:
        return 4
    if B < 25 and C < 25 and E < 25 and A < 30:
        return 4
    if B > 60 and C >= 60 and E >= 60 and A < 50:
        return 2
    return 1
"""
Predictor 540
Generated on: 2025-09-09 17:50:36
Accuracy: 50.54%
"""


# PREDICTOR 540 - Accuracy: 50.54%
# Correct predictions: 5054/10000 (50.54%)

def predict_output(A, B, C, D, E):
    if B >= 70 and D > 80 and 25 < C < 50:
        return 3
    if B < 20 and C < 15 and E <= 40:
        return 3
    if 30 < B < 40 and C < 20 and E < 40:
        return 3
    if 30 < A < 60 and 25 < B < 35 and C < 20 and E < 15 and D > 90:
        return 1
    if B < 30 and C > 90 and E > 90:
        return 4
    if E > 65 and B < 40 and C < 50:
        return 4
    if C > 50 and E < 25:
        return 4
    if C < 20 and E < 20:
        return 4
    if C > 60 and E < 45 and B < 30:
        return 4
    if B > 60 and C > 75 and E > 65:
        return 2
    return 1
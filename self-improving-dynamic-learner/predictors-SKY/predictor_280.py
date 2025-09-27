"""
Predictor 280
Generated on: 2025-09-09 15:00:29
Accuracy: 54.99%
"""


# PREDICTOR 280 - Accuracy: 54.99%
# Correct predictions: 5499/10000 (54.99%)

def predict_output(A, B, C, D, E):
    if B > 80 and C < 35:
        return 4
    if E > 90 and C < 40:
        return 4
    if B < 20 and C < 20 and E > 60:
        return 4
    if A > 90 and B < 30 and E > 80:
        return 4
    if B < 30 and C < 20 and E < 40:
        return 3
    if C < 25 and E < 30 and B < 50:
        return 3
    if B > 50 and C > 60 and D < 20 and E < 40:
        return 3
    if A > 80 and B < 40 and C < 35 and D > 80 and E < 15:
        return 3
    if B < 20 and C > 70 and E > 90:
        return 2
    if B > 60 and C > 70 and A < 50:
        return 2
    if B > 70 and C > 60 and D < 20:
        return 1
    if A + B > 160 and C > 40:
        return 2
    return 1
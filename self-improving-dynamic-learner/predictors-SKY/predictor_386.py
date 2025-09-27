"""
Predictor 386
Generated on: 2025-09-09 16:06:22
Accuracy: 48.99%
"""


# PREDICTOR 386 - Accuracy: 48.99%
# Correct predictions: 4899/10000 (48.99%)

def predict_output(A, B, C, D, E):
    if C > 80 and E < 30:
        return 4
    if E > 80 and C < 25 and D < 60:
        return 4
    if B > 90 and C < 20:
        return 4
    if B < 20 and C > 30 and E > 30 and D > 30:
        return 4
    if B > 60 and C > 70 and E >= 70:
        return 2
    if B < 40 and C > 60 and E > 50 and D < 20:
        return 2
    if B < 20 and C < 20 and E < 40:
        return 3
    if B < 25 and 50 < C < 60 and E < 55:
        return 3
    if B > 60 and C < 50 and E > 80:
        return 3
    return 1
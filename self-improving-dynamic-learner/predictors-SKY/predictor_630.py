"""
Predictor 630
Generated on: 2025-09-09 18:55:40
Accuracy: 49.66%
"""


# PREDICTOR 630 - Accuracy: 49.66%
# Correct predictions: 4966/10000 (49.66%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if C < 30 and D > 80 and E > 80:
        return 3
    if B > 50 and C < 40 and E < 40:
        return 3
    if B > 90 and C > 70 and E < 20:
        return 4
    if B < 40 and C > 50 and E > 40 and D < 50:
        return 4
    if E > 90 and C < 30 and D <= 80:
        return 4
    if B > 60 and C > 75 and E >= 70:
        return 2
    if B < 30 and E >= 70 and C < 50:
        return 2
    return 1
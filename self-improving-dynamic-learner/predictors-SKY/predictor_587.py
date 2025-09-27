"""
Predictor 587
Generated on: 2025-09-09 18:24:44
Accuracy: 53.23%
"""


# PREDICTOR 587 - Accuracy: 53.23%
# Correct predictions: 5323/10000 (53.23%)

def predict_output(A, B, C, D, E):
    if C < 40 and E > 60:
        return 4
    if B < 20 and C > 70:
        return 4
    if B < 20 and C < 20:
        return 3
    if C > 70 and E >= 70:
        return 2
    if B > 90 and C > 50 and E > 80:
        return 2
    if D > 80 and B < 30 and C < 20:
        return 1
    if B > 70 and C > 60:
        return 1
    return 1
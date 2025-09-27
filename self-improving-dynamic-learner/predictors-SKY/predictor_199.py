"""
Predictor 199
Generated on: 2025-09-09 14:08:56
Accuracy: 41.80%
"""


# PREDICTOR 199 - Accuracy: 41.80%
# Correct predictions: 4180/10000 (41.80%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if C > 75 and E < 30:
        return 4
    if B > 70 and C < 60 and E < 50 and A < 50:
        return 4
    if B > 70 and C < 20 and E < 20:
        return 4
    if D > 60 and E < 20 and C > 40:
        return 4
    if B < 30 and C > 35 and E > 50:
        return 4
    if 30 < B < 70 and C < 30 and E > 50:
        return 4
    if C > 75 and E > 65:
        return 2
    if B < 20 and C < 20:
        return 3
    return 1
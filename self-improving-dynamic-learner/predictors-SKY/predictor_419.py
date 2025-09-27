"""
Predictor 419
Generated on: 2025-09-09 16:25:43
Accuracy: 56.65%
"""


# PREDICTOR 419 - Accuracy: 56.65%
# Correct predictions: 5665/10000 (56.65%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    if E > 90 and C < 25:
        return 4
    if B > 60 and C > 75 and E > 65:
        return 2
    return 1
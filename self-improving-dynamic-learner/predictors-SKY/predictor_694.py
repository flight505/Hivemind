"""
Predictor 694
Generated on: 2025-09-09 19:41:07
Accuracy: 54.71%
"""


# PREDICTOR 694 - Accuracy: 54.71%
# Correct predictions: 5471/10000 (54.71%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    if B > 60 and C > 70 and A < 40:
        return 2
    if E > 90:
        return 4
    return 1
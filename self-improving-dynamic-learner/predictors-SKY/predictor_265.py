"""
Predictor 265
Generated on: 2025-09-09 14:50:04
Accuracy: 50.00%
"""


# PREDICTOR 265 - Accuracy: 50.00%
# Correct predictions: 5000/10000 (50.00%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    if B > 60 and C > 70:
        return 2
    if E > 90:
        return 4
    return 1
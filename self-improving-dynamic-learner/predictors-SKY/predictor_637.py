"""
Predictor 637
Generated on: 2025-09-09 19:00:56
Accuracy: 49.91%
"""


# PREDICTOR 637 - Accuracy: 49.91%
# Correct predictions: 4991/10000 (49.91%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B > 60 and C > 70:
        return 2
    if E > 90:
        return 4
    return 1
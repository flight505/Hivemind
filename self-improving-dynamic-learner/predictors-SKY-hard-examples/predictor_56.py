"""
Predictor 56
Generated on: 2025-09-09 17:41:47
Accuracy: 49.86%
"""


# PREDICTOR 56 - Accuracy: 49.86%
# Correct predictions: 4986/10000 (49.86%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if E > 90:
        return 4
    if B > 60 and C > 70:
        return 2
    return 1
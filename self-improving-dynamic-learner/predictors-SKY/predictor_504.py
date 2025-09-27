"""
Predictor 504
Generated on: 2025-09-09 17:23:54
Accuracy: 36.78%
"""


# PREDICTOR 504 - Accuracy: 36.78%
# Correct predictions: 3678/10000 (36.78%)

def predict_output(A, B, C, D, E):
    if B < 20:
        return 3
    if E > 90:
        return 4
    if C > 75:
        return 2
    return 1
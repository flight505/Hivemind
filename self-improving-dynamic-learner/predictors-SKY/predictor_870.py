"""
Predictor 870
Generated on: 2025-09-09 21:37:41
Accuracy: 56.53%
"""


# PREDICTOR 870 - Accuracy: 56.53%
# Correct predictions: 5653/10000 (56.53%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if E > 90 and B < 40 and C < 25:
        return 4
    if B > 60 and C > 60 and A < 40:
        return 2
    return 1
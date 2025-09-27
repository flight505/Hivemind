"""
Predictor 782
Generated on: 2025-09-09 20:46:39
Accuracy: 49.95%
"""


# PREDICTOR 782 - Accuracy: 49.95%
# Correct predictions: 4995/10000 (49.95%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    if E > 90:
        return 4
    if B > 60 and C > 70:
        return 2
    return 1
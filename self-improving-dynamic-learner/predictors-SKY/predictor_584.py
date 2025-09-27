"""
Predictor 584
Generated on: 2025-09-09 18:22:24
Accuracy: 56.53%
"""


# PREDICTOR 584 - Accuracy: 56.53%
# Correct predictions: 5653/10000 (56.53%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B > 60 and C > 75 and E > 60:
        return 2
    if E > 90 and C < 30:
        return 4
    if B > 80 and C < 30:
        return 1
    if D > 80 and C < 20:
        return 1
    if B > 70 and C > 60 and E > 70:
        return 1
    return 1
"""
Predictor 342
Generated on: 2025-09-09 15:37:39
Accuracy: 51.10%
"""


# PREDICTOR 342 - Accuracy: 51.10%
# Correct predictions: 5110/10000 (51.10%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if B > 60 and C > 75:
        return 2
    if B < 20 and C < 15:
        return 3
    return 1
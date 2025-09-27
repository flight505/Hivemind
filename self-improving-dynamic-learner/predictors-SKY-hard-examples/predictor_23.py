"""
Predictor 23
Generated on: 2025-09-09 17:20:05
Accuracy: 52.64%
"""


# PREDICTOR 23 - Accuracy: 52.64%
# Correct predictions: 5264/10000 (52.64%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B > 60 and C > 70:
        return 2
    if E > 90 and C < 30:
        return 4
    return 1
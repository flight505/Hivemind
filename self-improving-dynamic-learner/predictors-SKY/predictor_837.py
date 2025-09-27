"""
Predictor 837
Generated on: 2025-09-09 21:21:36
Accuracy: 52.73%
"""


# PREDICTOR 837 - Accuracy: 52.73%
# Correct predictions: 5273/10000 (52.73%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    if B > 60 and C > 70:
        return 2
    if E > 90 and C < 30:
        return 4
    return 1
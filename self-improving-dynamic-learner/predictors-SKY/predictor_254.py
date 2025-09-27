"""
Predictor 254
Generated on: 2025-09-09 14:42:13
Accuracy: 54.57%
"""


# PREDICTOR 254 - Accuracy: 54.57%
# Correct predictions: 5457/10000 (54.57%)

def predict_output(A, B, C, D, E):
    if A < 40 and B > 60 and C > 60:
        return 2
    if B < 20 and C < 20:
        return 3
    if E > 90:
        return 4
    return 1
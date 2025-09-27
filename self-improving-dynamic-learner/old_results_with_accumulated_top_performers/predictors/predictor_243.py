"""
Predictor 243
Generated on: 2025-09-09 06:04:11
Accuracy: 37.05%
"""


# PREDICTOR 243 - Accuracy: 37.05%
# Correct predictions: 3705/10000 (37.05%)

def predict_output(A, B, C, D, E):
    if E > 80:
        return 4
    elif B > 70 or D > 70:
        return 1
    elif B < 25 and C < 25:
        return 3
    else:
        return 2
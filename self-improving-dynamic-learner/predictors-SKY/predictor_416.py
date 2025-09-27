"""
Predictor 416
Generated on: 2025-09-09 16:22:52
Accuracy: 50.15%
"""


# PREDICTOR 416 - Accuracy: 50.15%
# Correct predictions: 5015/10000 (50.15%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    elif B < 20 and C < 20:
        return 3
    elif B > 60 and C > 70:
        return 2
    else:
        return 1
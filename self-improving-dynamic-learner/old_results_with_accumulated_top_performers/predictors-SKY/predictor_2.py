"""
Predictor 2
Generated on: 2025-09-09 03:33:10
Accuracy: 48.75%
"""


# PREDICTOR 2 - Accuracy: 48.75%
# Correct predictions: 4875/10000 (48.75%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    elif B > 60 and C > 70:
        return 2
    elif C < 15:
        return 3
    else:
        return 1
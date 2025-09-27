"""
Predictor 324
Generated on: 2025-09-09 08:23:31
Accuracy: 23.30%
"""


# PREDICTOR 324 - Accuracy: 23.30%
# Correct predictions: 2330/10000 (23.30%)

def predict_output(A, B, C, D, E):
    if E > 90 or (B < 20 and C < 20):
        return 4
    elif C > 60 and A <= 30:
        return 2
    elif B > 60 and C > 60:
        return 1
    else:
        return 3
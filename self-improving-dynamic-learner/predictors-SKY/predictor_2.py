"""
Predictor 2
Generated on: 2025-09-09 12:02:23
Accuracy: 47.46%
"""


# PREDICTOR 2 - Accuracy: 47.46%
# Correct predictions: 4746/10000 (47.46%)

def predict_output(A, B, C, D, E):
    if B < 20:
        return 3
    elif C < 25 and A < 50 and E > 75:
        return 4
    elif B > 50 and E > 60 and A < 60:
        return 2
    else:
        return 1
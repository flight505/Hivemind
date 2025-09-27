"""
Predictor 0
Generated on: 2025-09-09 23:16:45
Accuracy: 46.70%
"""


# PREDICTOR 0 - Accuracy: 46.70%
# Correct predictions: 4670/10000 (46.70%)

def predict_output(A, B, C, D, E):
    if A < 10 and B > 70:
        return 4
    elif C < 10 and D > 90:
        return 4
    elif A > 90:
        return 2
    elif B < 10:
        return 3
    else:
        return 1
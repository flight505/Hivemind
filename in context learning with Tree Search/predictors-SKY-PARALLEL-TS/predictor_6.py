"""
Predictor 6
Generated on: 2025-09-09 23:16:45
Accuracy: 36.22%
"""


# PREDICTOR 6 - Accuracy: 36.22%
# Correct predictions: 3622/10000 (36.22%)

def predict_output(A, B, C, D, E):
    if (A < 15 or C < 15) and (B > 60 or D > 60):
        return 4
    elif A + B > 150:
        return 2
    elif C + D > 140:
        return 3
    else:
        return 1
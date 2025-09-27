"""
Predictor 329
Generated on: 2025-09-09 08:33:44
Accuracy: 32.32%
"""


# PREDICTOR 329 - Accuracy: 32.32%
# Correct predictions: 3232/10000 (32.32%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    elif E > 90:
        return 4
    elif C > 60 and (A > 50 or B > 60):
        return 1
    elif B > 60 and C > 60:
        return 2
    else:
        return 3
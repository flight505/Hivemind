"""
Predictor 8
Generated on: 2025-09-09 23:16:45
Accuracy: 30.81%
"""


# PREDICTOR 8 - Accuracy: 30.81%
# Correct predictions: 3081/10000 (30.81%)

def predict_output(A, B, C, D, E):
    if A + B > 150:
        return 2
    elif C > 70:
        return 3
    elif (A < 10 and B > 70) or (D > 80 and E > 80):
        return 4
    else:
        return 1
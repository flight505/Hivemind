"""
Predictor 11
Generated on: 2025-09-09 23:16:45
Accuracy: 41.63%
"""


# PREDICTOR 11 - Accuracy: 41.63%
# Correct predictions: 4163/10000 (41.63%)

def predict_output(A, B, C, D, E):
    if A > 75 and B > 60:
        return 2
    elif C > 60 and D < 40:
        return 3
    elif (A < 10 and B > 70) or (D > 80 and E > 80):
        return 4
    else:
        return 1
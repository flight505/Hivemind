"""
Predictor 9
Generated on: 2025-09-09 23:16:45
Accuracy: 50.29%
"""


# PREDICTOR 9 - Accuracy: 50.29%
# Correct predictions: 5029/10000 (50.29%)

def predict_output(A, B, C, D, E):
    if A + E < 20:
        return 2
    elif C > 60 and D < 20:
        return 3
    elif (A < 10 and B > 70) or (D > 80 and E > 80):
        return 4
    else:
        return 1
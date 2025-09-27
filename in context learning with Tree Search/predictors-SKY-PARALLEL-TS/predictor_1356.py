"""
Predictor 1356
Generated on: 2025-09-10 02:12:16
Accuracy: 55.05%
"""


# PREDICTOR 1356 - Accuracy: 55.05%
# Correct predictions: 5505/10000 (55.05%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90):
        return 4
    elif A > 90 and E < 10:
        return 2
    elif B > 90 and D > 80:
        return 3
    else:
        return 1
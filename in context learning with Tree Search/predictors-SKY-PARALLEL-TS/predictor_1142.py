"""
Predictor 1142
Generated on: 2025-09-10 01:35:54
Accuracy: 39.81%
"""


# PREDICTOR 1142 - Accuracy: 39.81%
# Correct predictions: 3981/10000 (39.81%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (C > 90) or (B > 90) or (D > 55 and E < 10) or (C > 60 and E > 80):
        return 4
    elif (B > 70 and C > 60) or (D < 15 and E > 50):
        return 2
    elif B > 70 and C < 10:
        return 3
    else:
        return 1
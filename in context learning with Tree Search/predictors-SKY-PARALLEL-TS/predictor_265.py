"""
Predictor 265
Generated on: 2025-09-09 23:43:38
Accuracy: 55.73%
"""


# PREDICTOR 265 - Accuracy: 55.73%
# Correct predictions: 5573/10000 (55.73%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 90) or (A > 90 and D < 30 and E > 70) or (B > 80 and E < 10):
        return 4
    elif (A > 80 and B > 80) or (A < 10 and E > 50 and C < 35 and D < 30):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40):
        return 3
    else:
        return 1
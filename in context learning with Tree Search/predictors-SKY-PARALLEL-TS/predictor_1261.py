"""
Predictor 1261
Generated on: 2025-09-10 01:54:58
Accuracy: 57.66%
"""


# PREDICTOR 1261 - Accuracy: 57.66%
# Correct predictions: 5766/10000 (57.66%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E > 10) or (C < 20 and D > 40) or (A > 60 and B < 25 and C < 30 and D > 40) or (C > 60 and D < 25 and A < 50):
        return 4
    elif (B > 90 and C > 90) or (A < 10 and B > 70 and E < 10) or (B > 90 and E < 10):
        return 2
    elif A > 50 and D > 50 and C < 50 and E < 40:
        return 3
    else:
        return 1
"""
Predictor 983
Generated on: 2025-09-10 01:11:30
Accuracy: 54.86%
"""


# PREDICTOR 983 - Accuracy: 54.86%
# Correct predictions: 5486/10000 (54.86%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (E < 10 and D > 40 and B < 50):
        return 4
    elif (B > 90 and C < 40) or (A < 5 and B < 40 and E > 50):
        return 2
    elif (C < 10 and E < 5) or (B < 15 and D < 10):
        return 3
    else:
        return 1
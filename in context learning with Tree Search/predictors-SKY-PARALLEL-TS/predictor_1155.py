"""
Predictor 1155
Generated on: 2025-09-10 01:37:38
Accuracy: 54.81%
"""


# PREDICTOR 1155 - Accuracy: 54.81%
# Correct predictions: 5481/10000 (54.81%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (B < 10 and D > C) or (E > 70 and B < 40 and D < 30 and C < 35):
        return 4
    elif A > 90 and E < 10 and B < 30:
        return 2
    elif A > 50 and B < 20 and D < 10:
        return 3
    else:
        return 1
"""
Predictor 863
Generated on: 2025-09-10 00:55:50
Accuracy: 54.72%
"""


# PREDICTOR 863 - Accuracy: 54.72%
# Correct predictions: 5472/10000 (54.72%)

def predict_output(A, B, C, D, E):
    if (B < 10 and C > 50):
        return 4
    if (A < 10 and B > 70 and E < 20):
        return 4
    if (C < 15 and D > 90 and B < 70):
        return 4
    if (B > 80 and A > 10 and C > 40 and D > 20):
        return 2
    if (A > 50 and C < 50 and D > 70 and B > 40):
        return 3
    else:
        return 1
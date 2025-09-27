"""
Predictor 1377
Generated on: 2025-09-10 02:16:28
Accuracy: 54.21%
"""


# PREDICTOR 1377 - Accuracy: 54.21%
# Correct predictions: 5421/10000 (54.21%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90 and E > 80) or (B > 65 and E < 5) or (C > 60 and D < 25 and E > 80):
        return 4
    elif (A < 15 and C < 15 and D > 70 and E > 50) or (B > 85 and C > 90):
        return 2
    elif A > 60 and B < 20 and D < 10:
        return 3
    else:
        return 1
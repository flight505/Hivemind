"""
Predictor 22
Generated on: 2025-09-09 23:19:12
Accuracy: 50.24%
"""


# PREDICTOR 22 - Accuracy: 50.24%
# Correct predictions: 5024/10000 (50.24%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 20 and D > 69) or (B < 20 and C > 60) or (E > 90):
        return 4
    elif (B > 90 and E < 15) or (D > 90 and E > 70) or (A > 70 and B < 20 and C < 10):
        return 3
    elif A > 90 and E < 10:
        return 2
    else:
        return 1
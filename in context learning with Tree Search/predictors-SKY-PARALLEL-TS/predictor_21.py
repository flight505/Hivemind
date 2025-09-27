"""
Predictor 21
Generated on: 2025-09-09 23:19:12
Accuracy: 51.92%
"""


# PREDICTOR 21 - Accuracy: 51.92%
# Correct predictions: 5192/10000 (51.92%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 20 and D > 65) or (B < 20 and C > 60) or (A > 70 and E > 90):
        return 4
    elif A > 90 and E < 10:
        return 2
    elif (B > 90 and E < 15) or (A > 70 and B < 20 and C < 10) or (D > 90 and E > 80):
        return 3
    else:
        return 1
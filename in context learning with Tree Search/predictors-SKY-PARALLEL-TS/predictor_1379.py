"""
Predictor 1379
Generated on: 2025-09-10 02:16:28
Accuracy: 55.19%
"""


# PREDICTOR 1379 - Accuracy: 55.19%
# Correct predictions: 5519/10000 (55.19%)

def predict_output(A, B, C, D, E):
    if (A < 30 and B > 70 and E < 20) or (C < 15 and D > 80 and E > 80) or (C > 60 and D < 30 and E > 80):
        return 4
    elif (C < 15 and D > 70 and E > 50) or (B > 80 and C > 90):
        return 2
    elif A > 60 and B < 20 and D < 10:
        return 3
    else:
        return 1
"""
Predictor 433
Generated on: 2025-09-10 00:02:23
Accuracy: 50.88%
"""


# PREDICTOR 433 - Accuracy: 50.88%
# Correct predictions: 5088/10000 (50.88%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 10 and D > 90) or (A < 10 and C > 70) or (B < 20 and C > 90) or (A < 30 and B < 25 and C < 35 and D > 40 and E < 30):
        return 4
    elif (B > 70 and D > 90 and E > 80) or (A > 80 and B < 15 and D < 5) or (B < 10 and D > 80):
        return 3
    elif (A > 50 and B > 70 and C < 50) or (A > 90 and E < 10):
        return 2
    else:
        return 1
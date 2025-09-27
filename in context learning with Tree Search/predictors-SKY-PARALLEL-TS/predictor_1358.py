"""
Predictor 1358
Generated on: 2025-09-10 02:12:16
Accuracy: 49.87%
"""


# PREDICTOR 1358 - Accuracy: 49.87%
# Correct predictions: 4987/10000 (49.87%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C > 30) or
        (C < 10 and D > 90) or
        (B > 50 and D < 25 and C > 40) or
        (A > 70 and C < 10 and D > 70) or
        (E > 90 and B > 70) or
        (A < 40 and B < 20 and C < 30 and D > 40) or
        (C < 30 and E > 65 and A > 10 and B > 70)):
        return 4
    elif (A > 90 and E < 10) or (B > 85 and C > 80):
        return 2
    elif (B < 10 and D > 80) or (A > 40 and C < 20 and D > 35) or (A > 70 and B < 30 and E < 20):
        return 3
    else:
        return 1
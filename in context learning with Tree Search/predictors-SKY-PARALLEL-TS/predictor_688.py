"""
Predictor 688
Generated on: 2025-09-10 00:34:06
Accuracy: 54.64%
"""


# PREDICTOR 688 - Accuracy: 54.64%
# Correct predictions: 5464/10000 (54.64%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and E < 20) or
        (C < 20 and D > 90) or
        (C < 20 and E > 80 and B > 50) or
        (E < 15 and C > 30 and B > 25) or
        (A > 60 and E > 80 and C < 30) or
        (B > 70 and C > 70 and E < 20)):
        return 4
    if ((A < 10 and B > 70 and E > 70) or
        (A < 10 and B < 20 and E > 90) or
        (B > 75 and E > 80 and C > 60) or
        (C > 80 and D < 10 and A > 50)):
        return 2
    if (A > 90 and B < 10 and D > 50):
        return 3
    else:
        return 1
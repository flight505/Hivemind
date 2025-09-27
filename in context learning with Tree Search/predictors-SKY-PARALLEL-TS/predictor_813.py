"""
Predictor 813
Generated on: 2025-09-10 00:50:43
Accuracy: 58.34%
"""


# PREDICTOR 813 - Accuracy: 58.34%
# Correct predictions: 5834/10000 (58.34%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90) or
        (A > 70 and B < 20 and C < 10 and D > 60) or
        (B > 80 and C < 30 and E > 80) or
        (A < 30 and B > 50 and C > 50 and D < 40) or
        (A < 40 and B > 50 and C > 40 and E < 10)):
        return 4
    elif (B > 75 and C > 40 and A < 50):
        return 2
    elif (A > 50 and B < 10 and C < 10 and E < 10):
        return 3
    else:
        return 1
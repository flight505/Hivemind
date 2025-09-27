"""
Predictor 1161
Generated on: 2025-09-10 01:37:38
Accuracy: 58.83%
"""


# PREDICTOR 1161 - Accuracy: 58.83%
# Correct predictions: 5883/10000 (58.83%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (B > 70 and E > 60 and C < 50) or (A > 80 and E > 80 and D < 25) or (A < 30 and C > 60 and E < 15):
        return 4
    elif (A > 50 and C < 15 and D > 65) or (A < 25 and B > 45 and C < 30 and D < 40) or (A > 90 and B < 40 and D > 70) or (B > 70 and C < 10 and D > 80):
        return 3
    elif (B > 70 and C > 80 and A < 50) or (B > 65 and C > 50 and E > 65 and A < 50):
        return 2
    else:
        return 1
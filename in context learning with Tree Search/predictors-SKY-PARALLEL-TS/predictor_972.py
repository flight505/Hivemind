"""
Predictor 972
Generated on: 2025-09-10 01:11:30
Accuracy: 58.83%
"""


# PREDICTOR 972 - Accuracy: 58.83%
# Correct predictions: 5883/10000 (58.83%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 60) or
        (C < 30 and E > 65) or
        (A > 70 and B < 20 and C > 70) or
        (A < 30 and C > 75 and D < 30) or
        (A > 80 and B > 70 and C < 40 and D > 50 and E > 80) or
        (A > 75 and B < 40 and C < 35 and D < 25 and E > 95) or
        (A < 10 and B < 30 and C < 5 and D > 95 and E > 85)):
        return 4
    if ((B > 85 and C > 80) or
        (B > 70 and D < 20 and A < 50 and E > 40) or
        (D < 5 and C > 50 and E > 50) or
        (B > 90 and E > 85) or
        (A < 40 and D < 20 and E > 50 and C > 40 and B > 70)):
        return 2
    if ((A > 50 and C < 50 and D > 70 and B > 40) or
        (A < 50 and D < 25 and E < 20) or
        (D < 15 and C > 40 and B < 80) or
        (C <= 10 and E < 60) or
        (A > 75 and B < 25 and C < 45 and D > 60) or
        (A > 50 and B < 20 and C < 15) or
        (A > 80 and B < 30 and C < 45) or
        (A < 25 and B < 25 and C < 15 and D > 70) or
        (50 < A < 60 and B < 20 and C < 15 and D > 30 and E < 20)):
        return 3
    else:
        return 1
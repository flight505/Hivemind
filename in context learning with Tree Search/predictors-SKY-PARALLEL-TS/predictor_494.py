"""
Predictor 494
Generated on: 2025-09-10 00:08:08
Accuracy: 58.83%
"""


# PREDICTOR 494 - Accuracy: 58.83%
# Correct predictions: 5883/10000 (58.83%)

def predict_output(A, B, C, D, E):
    if ((B - A > 60 and E < 25) or
        (D - C > 75 and E > 75) or
        (E - C > 70 and A > 35) or
        (C < 20 and D > 60) or
        (A > 50 and B < 25 and C > 60) or
        (B > 90 and C < 10) or
        (A < 15 and B > 80 and C > 55 and E < 30)):
        return 4
    if ((B > 85 and C > 80 and A < 60 and D > 20) or
        (B > 75 and C > 60 and E > 60 and A < 55) or
        (B > 90 and E > 85 and C > 60) or
        (B > 80 and D < 10 and E > 80) or
        (A < 50 and B > 80 and C > 70)):
        return 2
    if ((A > 45 and C < 50 and D > 60 and B > 40) or
        (C > 90 and B < 20 and D < 10) or
        (D > 90 and B > 80 and E < 40) or
        (A < 20 and D > 55 and C < 15) or
        (C > 40 and D < 15 and B < 80 and E < 50) or
        (A < 15 and C > 90 and D < 5)):
        return 3
    else:
        return 1
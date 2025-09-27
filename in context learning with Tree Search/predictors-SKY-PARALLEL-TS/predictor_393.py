"""
Predictor 393
Generated on: 2025-09-09 23:57:59
Accuracy: 56.54%
"""


# PREDICTOR 393 - Accuracy: 56.54%
# Correct predictions: 5654/10000 (56.54%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C < 70 and E < 30) or
        (C < 15 and D > 55) or
        (C < 25 and E > 70) or
        (B > 90) or
        (A > 80 and E > 80) or
        (C > 60 and E < 5) or
        (B > 80 and D > 80 and C < 15) or
        (A > 80 and B > 80) or
        (A > 70 and C < 30 and D > 50 and E > 70)):
        return 4
    elif ((A > 50 and B < 30 and C > 60 and D < 5) or
          (A < 40 and D < 10 and E < 20 and C < 25) or
          (A > 50 and C < 50 and D > 70 and B > 40)):
        return 3
    elif ((B > 90 and C > 70) or
          (B > 90 and D > 70) or
          (B > 85 and C > 80)):
        return 2
    else:
        return 1
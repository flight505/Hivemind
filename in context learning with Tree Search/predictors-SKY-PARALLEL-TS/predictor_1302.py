"""
Predictor 1302
Generated on: 2025-09-10 02:02:09
Accuracy: 54.65%
"""


# PREDICTOR 1302 - Accuracy: 54.65%
# Correct predictions: 5465/10000 (54.65%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (A > 90 and D < 30 and E > 70) or
        (B > 70 and C > 80 and E < 10) or
        (C > 50 and E < 10 and A < 20) or
        (B > 90 and D < 30) or
        (A > 90 and B > 50 and C > 50 and D < 30 and E > 70)):
        return 4
    elif ((C < 10 and B > 50 and A < 5) or
          (A > 70 and B < 40 and C < 10 and D > 50 and E < 10)):
        return 3
    elif ((E > 60 and D < 20 and B < 30) or
          (B > 70 and C > 90 and D > 90)):
        return 2
    else:
        return 1
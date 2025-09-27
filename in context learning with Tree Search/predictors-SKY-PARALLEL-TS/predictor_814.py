"""
Predictor 814
Generated on: 2025-09-10 00:50:43
Accuracy: 57.05%
"""


# PREDICTOR 814 - Accuracy: 57.05%
# Correct predictions: 5705/10000 (57.05%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 60) or
        (B > 80 and E > 80) or
        (A < 30 and B > 50 and C > 50 and D < 40) or
        (A < 40 and B > 50 and C > 40 and E < 10) or
        (A > 70 and B < 20 and C < 10 and D > 60) or
        (A < 30 and B > 80 and C < 30 and E > 80) or
        (A < 30 and B > 50 and C > 50 and D < 40) or
        (A > 35 and B < 60 and C > 45 and D < 55 and E < 10)):
        return 4
    elif ((B > 85 and C > 60 and A < 30) or
          (B > 75 and C < 50 and A < 50 and D > 70) or
          (B > 80 and C > 55 and A < 30 and D > 60) or
          (A > 90 and E < 10) or
          (B > 70 and D < 20 and A < 50 and E > 40)):
        return 2
    elif ((A > 50 and B < 10 and C < 10 and D < 40 and E < 10) or
          (B < 10 and E < 10) or
          (A > 40 and B < 10 and C < 5 and D < 35 and E < 5)):
        return 3
    else:
        return 1
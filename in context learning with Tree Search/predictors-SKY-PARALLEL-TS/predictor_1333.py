"""
Predictor 1333
Generated on: 2025-09-10 02:07:02
Accuracy: 53.24%
"""


# PREDICTOR 1333 - Accuracy: 53.24%
# Correct predictions: 5324/10000 (53.24%)

def predict_output(A, B, C, D, E):
    if ((A < 15 and B > 70 and C < 60) or
        (C < 20 and D > 80) or
        (B < 20 and E > 55) or
        (C < 25 and E > 60) or
        (D < 10 and E > 80) or
        (B > 95 and E > 65) or
        (A > 50 and B < 15 and E > 60)):
        return 4
    elif ((A > 90 and E < 10) or
          (D < 5 and E > 70) or
          (B > 90 and E > 50 and D > 70 and C < 70) or
          (C < 15 and E > 50 and A < 20 and D > 40) or
          (E > 75 and B < 70 and C < 50)):
        return 2
    elif ((A > 70 and B < 20) or
          (C > 80 and D < 10) or
          (B < 15 and D < 20) or
          (B > 90 and C > 85 and E < 15) or
          (A < 15 and B > 70 and C > 85)):
        return 3
    else:
        return 1
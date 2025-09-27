"""
Predictor 419
Generated on: 2025-09-10 00:02:23
Accuracy: 47.93%
"""


# PREDICTOR 419 - Accuracy: 47.93%
# Correct predictions: 4793/10000 (47.93%)

def predict_output(A, B, C, D, E):
    if ((B - A > 60 and E < 20) or
        (D - C > 80 and E > 80) or
        (C < 15 and D > 65) or
        (B < 20 and C > 60 and E < 10) or
        (E > 90 and D < 50) or
        (B > 85 and D > 80) or
        (B < 15 and C > 80)):
        return 4
    elif ((B < 25 and E > 60) or
          (C < 12 and D > 45 and A < 10) or
          (B > 90 and C > 55) or
          (E > 75 and A > 55 and B > 55 and D > 35 and C < 50)):
        return 2
    elif ((C > 80 and D > 70) or
          (C < 15 and D > 50) or
          (D < 10 and C < 30 and A < 60)):
        return 3
    else:
        return 1
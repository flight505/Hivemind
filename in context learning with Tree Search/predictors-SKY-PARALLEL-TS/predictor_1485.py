"""
Predictor 1485
Generated on: 2025-09-10 02:35:36
Accuracy: 57.01%
"""


# PREDICTOR 1485 - Accuracy: 57.01%
# Correct predictions: 5701/10000 (57.01%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and E < 35 and C > 25) or
        (A < 10 and B > 90 and E > 80) or
        (C < 15 and D > 80) or
        (C < 25 and E > 65 and A > 50) or
        (A < 20 and C > 75 and D < 35) or
        (B < 15 and C > 75 and E < 10) or
        (A > 70 and B < 25 and C > 60 and D < 40) or
        (A < 15 and B > 80 and C > 55 and E < 30) or
        (A > 60 and B < 20 and C < 20 and D > 50)):
        return 4
    elif ((B > 85 and A < 20) or
          (B > 80 and C > 60) or
          (B > 90 and D > 80) or
          (B > 70 and C > 50 and E > 70) or
          (A < 10 and B > 50 and C < 30 and E > 60) or
          (B < 15 and D < 10 and E > 50)):
        return 2
    elif ((A > 45 and C < 50 and D > 55 and B > 35) or
          (C < 15 and B > 60 and D < 35) or
          (A < 15 and B > 60 and C < 15 and E < 50) or
          (B > 80 and D > 85 and E < 35) or
          (A > 60 and B < 20 and C < 20 and D > 60)):
        return 3
    else:
        return 1
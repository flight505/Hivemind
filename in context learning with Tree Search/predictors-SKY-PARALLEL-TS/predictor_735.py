"""
Predictor 735
Generated on: 2025-09-10 00:41:18
Accuracy: 57.23%
"""


# PREDICTOR 735 - Accuracy: 57.23%
# Correct predictions: 5723/10000 (57.23%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C < 40) or
        (C < 25 and D > 70 and E > 80 and B > 55) or
        (A > 60 and B < 30 and C > 35 and D > 30 and E < 25) or
        (A > 35 and B > 70 and C < 30 and D > 55 and E < 50) or
        (B > 70 and C < 30 and D > 70) or
        (A > 80 and B < 20) or
        (E > 80 and C < 25) or
        (C < 15 and D > 90 and E > 80)):
        return 4
    elif ((B > 85 and C > 80) or
          (A > 90 and E < 10) or
          (D < 5 and C > 50 and E > 50) or
          (B > 70 and D < 20 and A < 50 and E > 40) or
          (A < 15 and B > 50 and C < 20 and D < 30 and E > 70) or
          (B > 75 and C > 50 and E > 60 and A < 50 and D < 80)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (B > 80 and D > 90) or
          (A < 40 and B > 90 and D > 90) or
          (C <= 10 and E < 60) or
          (A > 75 and B < 25 and C < 45 and D > 60) or
          (A < 35 and B > 60 and C < 5 and D > 75 and E < 40) or
          (A > 95 and B > 40 and C > 40 and D > 55 and E > 50) or
          (A > 75 and B < 30 and C > 40 and D > 90)):
        return 3
    else:
        return 1
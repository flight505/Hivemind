"""
Predictor 846
Generated on: 2025-09-10 00:55:50
Accuracy: 57.65%
"""


# PREDICTOR 846 - Accuracy: 57.65%
# Correct predictions: 5765/10000 (57.65%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 55) or
        (C < 25 and E > 70) or
        (A > 80 and B < 30 and C < 30 and D < 30 and E > 70) or
        (C > 70 and D < 25 and E < 25 and A < 50 and B > 40) or
        (A > 80 and B < 10 and D > 70 and E < 10)):
        return 4
    elif ((B > 70 and C > 40 and D > 30) or
          (B > 70 and D < 20 and A < 50 and E > 40)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (A < 50 and D < 25 and E < 20 and B < 80) or
          (D < 15 and C > 40 and B < 80) or
          (C <= 10 and E < 60) or
          (A > 75 and B < 25 and C < 45 and D > 60) or
          (B > 60 and C > 70 and D > 60 and E < 15) or
          (A > 20 and B < 45 and C < 20 and D < 40 and E < 15) or
          (C > 70 and D > 65 and E < 15) or
          (B < 25 and C < 25 and D < 25)):
        return 3
    else:
        return 1
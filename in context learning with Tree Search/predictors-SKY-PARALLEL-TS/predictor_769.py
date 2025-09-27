"""
Predictor 769
Generated on: 2025-09-10 00:44:16
Accuracy: 60.25%
"""


# PREDICTOR 769 - Accuracy: 60.25%
# Correct predictions: 6025/10000 (60.25%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C < 50) or
        (C < 15 and D > 80) or
        (A > 70 and B < 10 and C > 60 and E < 10) or
        (A > 60 and B < 15 and C > 70 and E < 25 and D < 30) or
        (A < 20 and C > 55 and E < 25) or
        (C < 25 and E > 65) or
        (B > 70 and D < 20 and E > 90) or
        (C > 90 and E < 10 and D > 50) or
        (A < 30 and C > 75 and D < 30) or
        (A > 70 and B < 20 and C > 70)):
        return 4
    elif ((B > 85 and C > 80 and D < 80) or
          (B > 70 and D < 20 and A < 50 and E > 40 and C > 35) or
          (B > 90 and E > 85 and A > 65 and C < 70) or
          (D < 5 and C > 50 and B < 50 and E > 50) or
          (A < 40 and D < 25 and E > 50 and C > 40) or
          (B > 75 and C > 50 and E > 60 and A < 50)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (C <= 10 and E < 60 and B < 50) or
          (A > 60 and C < 45 and D > 50) or
          (D < 15 and C > 40 and B < 80) or
          (A < 40 and B > 90 and D > 90) or
          (A > 45 and C < 50 and D > 55)):
        return 3
    else:
        return 1
"""
Predictor 1087
Generated on: 2025-09-10 01:28:10
Accuracy: 61.58%
"""


# PREDICTOR 1087 - Accuracy: 61.58%
# Correct predictions: 6158/10000 (61.58%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C < 40) or
        (C < 15 and D > 60 and B > 30) or
        (C < 25 and E > 65) or
        (A < 30 and C > 75 and D < 30 and E > 20) or
        (A > 80 and B < 10 and D > 70 and E < 10) or
        (A > 90 and C < 5 and D > 90) or
        (B > 70 and C > 60 and D < 20) or
        (C < 15 and D > 80) or
        (A < 20 and B > 65 and C > 60 and D < 25) or
        (B > 75 and C > 90 and D < 20 and E > 80)):
        return 4
    elif ((B > 80 and C > 75 and A < 80) or
          (B > 70 and D < 20 and A < 50 and E > 40 and C < 60) or
          (D < 5 and C > 50 and E > 50) or
          (A < 40 and D < 25 and E > 50 and C > 40 and B > 70 and C < 60) or
          (B > 70 and C > 60 and E < 25 and A < 50) or
          (A < 25 and B < 10 and D < 15 and E > 60) or
          (A < 10 and B > 45 and C > 65 and D < 10 and E > 45)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (A < 50 and D < 25 and E < 20 and B < 80) or
          (D < 15 and C > 40 and B < 80) or
          (C <= 10 and E < 60 and B < 50) or
          (A > 75 and B < 25 and C < 45 and D > 60) or
          (B > 80 and C > 85 and D > 80) or
          (A < 40 and B > 90 and D > 90) or
          (B > 80 and D > 90 and E < 30) or
          (A > 60 and B < 15 and C < 15 and D > 70) or
          (A < 50 and B > 20 and C > 55 and D < 20 and E < 40) or
          (A < 20 and B > 70 and C > 85 and D < 10) or
          (B < 10 and C < 20 and D > 30 and E > 40)):
        return 3
    else:
        return 1
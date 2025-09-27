"""
Predictor 872
Generated on: 2025-09-10 00:58:03
Accuracy: 62.85%
"""


# PREDICTOR 872 - Accuracy: 62.85%
# Correct predictions: 6285/10000 (62.85%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 55 and E > 80) or
        (C < 25 and E > 65) or
        (D < 5 and E > 70 and A > 50 and B < 30 and C < 40) or
        (C > 60 and B < 20 and E < 10 and A > 40) or
        (A < 50 and B > 55 and C < 15 and D > 90) or
        (A > 75 and B > 40 and C < 25 and D > 95 and E < 20) or
        (A > 80 and B < 10 and D > 70 and E < 10) or
        (A < 30 and C > 75 and D < 30) or
        (B > 70 and D < 10 and E > 90) or
        (A > 80 and B < 30 and C > 70 and E > 90) or
        (A > 50 and B > 50 and C > 50 and C < 80 and D < 35 and E > 90)):
        return 4
    elif ((B > 85 and C > 80) or
          (B > 70 and D < 20 and A < 50 and E > 40 and C > 70) or
          (D < 5 and C > 50 and B < 50 and E > 50) or
          (B < 15 and D < 6 and E > 50) or
          (A < 40 and D < 25 and E > 50 and C > 40 and B < 60) or
          (A < 30 and B > 90 and C > 95 and D > 80)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (A < 50 and D < 25 and E < 20 and B < 80) or
          (D < 15 and C > 40 and B < 80 and A < 70 and E < 50 and B > 55) or
          (C <= 10 and E < 60 and B < 50) or
          (A > 75 and B < 25 and C < 45 and D > 60) or
          (B > 80 and C > 85 and D > 80 and A < 50 and E < 60) or
          (A < 40 and B > 90 and D > 90) or
          (B > 80 and D > 90 and E < 30) or
          (A > 60 and B < 15 and C < 15 and D > 70)):
        return 3
    else:
        return 1
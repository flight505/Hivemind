"""
Predictor 1194
Generated on: 2025-09-10 01:43:05
Accuracy: 55.24%
"""


# PREDICTOR 1194 - Accuracy: 55.24%
# Correct predictions: 5524/10000 (55.24%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90) or
        (A > 60 and B < 35 and C > 40 and D < 25 and E < 10) or
        (A < 20 and B < 30 and C > 90 and D < 30 and E < 30) or
        (A > 60 and B < 35 and C > 75 and D < 25 and E < 25) or
        (A < 30 and B > 80 and C < 20 and D > 75)):
        return 4
    elif ((A > 90 and E < 10) or
          (B > 85 and C > 80) or
          (D < 5 and E > 50) or
          (B > 70 and D < 20 and E > 40) or
          (A < 40 and D < 25 and E > 50 and C > 40)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (A < 50 and D < 25 and E < 20 and B < 80) or
          (D < 15 and C > 40 and B < 80) or
          (C <= 10 and E < 60) or
          (A > 75 and B < 25 and C < 45 and D > 60) or
          (A > 80 and B < 35 and C < 40 and D > 90) or
          (A < 50 and B > 70 and C > 75 and D > 75 and E < 15)):
        return 3
    else:
        return 1
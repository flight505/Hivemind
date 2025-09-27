"""
Predictor 528
Generated on: 2025-09-10 00:14:11
Accuracy: 57.42%
"""


# PREDICTOR 528 - Accuracy: 57.42%
# Correct predictions: 5742/10000 (57.42%)

def predict_output(A, B, C, D, E):
    if ((A <= 10 and B > 70) or
        (C < 15 and D > 55) or
        (C < 25 and E > 70) or
        (A > 50 and C < 30 and D > 70 and B > 60) or
        (A > 40 and B < 40 and C < 30 and E < 20 and D > 40) or
        (A > 70 and B < 10 and E > 60) or
        (A > 90 and B > 80 and C < 30) or
        (A > 50 and B < 35 and C > 80) or
        (A > 40 and B < 20 and D < 15 and E > 90)):
        return 4
    elif ((A > 89 and E < 10 and D < 10) or
          (B > 85 and C > 80) or
          (C > 55 and D < 10 and E > 85)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (A < 50 and D < 25 and E < 20 and B < 80) or
          (D < 15 and C > 40 and B < 80 and E > 20) or
          (C < 10 and E < 60) or
          (A > 40 and B > 50 and D > 90) or
          (B > 60 and C < 20 and E < 30) or
          (B > 70 and C > 70 and D > 70 and E > 90) or
          (A > 90 and B < 10 and D > 80 and E < 10) or
          (A < 30 and B < 40 and C < 30 and D < 25 and E < 40)):
        return 3
    else:
        return 1
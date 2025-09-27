"""
Predictor 1022
Generated on: 2025-09-10 01:15:51
Accuracy: 57.49%
"""


# PREDICTOR 1022 - Accuracy: 57.49%
# Correct predictions: 5749/10000 (57.49%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C < 85) or
        (C < 15 and D > 60) or
        (C < 25 and E > 65) or
        (A > 65 and B < 30 and C > 40 and D < 30) or
        (A > 70 and B < 30 and C > 90 and D < 35) or
        (A < 25 and B < 5 and C < 10 and D < 25 and E > 70) or
        (A > 80 and D < 35 and E > 70)):
        return 4
    elif ((B > 85 and C > 80 and E > 20) or
          (B > 70 and D < 20 and A < 50 and E > 40) or
          (A < 5 and C < 5 and D > 50 and E > 80) or
          (A < 35 and B < 20 and C > 30 and D < 10 and E > 60) or
          (A < 55 and B > 75 and C < 30 and D > 70 and E > 75) or
          (B > 70 and C > 60 and E < 25 and A < 50)):
        return 2
    elif ((A > 50 and C < 50 and D > 65 and B > 40) or
          (A < 50 and D < 25 and E < 40 and B < 80) or
          (D < 15 and C > 40 and B < 80) or
          (C <= 10 and E < 60 and B < 50) or
          (A > 80 and B > 50 and C < 40 and D > 50 and E > 50) or
          (A < 15 and B < 30 and C < 15 and D < 30 and E > 40) or
          (C > 80 and D > 70)):
        return 3
    else:
        return 1
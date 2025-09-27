"""
Predictor 655
Generated on: 2025-09-10 00:31:36
Accuracy: 58.82%
"""


# PREDICTOR 655 - Accuracy: 58.82%
# Correct predictions: 5882/10000 (58.82%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and E < 20) or
        (C < 15 and D > 60) or
        (C > 90 and B < 20) or
        (B < 10 and C < 15 and E > 60) or
        (B > 80 and D > 85 and C < 25) or
        (A > 85 and C > 70 and D < 30 and E > 75) or
        (A < 10 and E < 5)):
        return 4
    elif (A > 90 and E < 10) or (B > 85 and C > 80):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40 and E < 80) or
          (A < 50 and D < 25 and E < 20 and B < 80) or
          (D < 15 and C > 40 and A < 70) or
          (C <= 10 and E < 60 and B < 80) or
          (A < 30 and B < 40 and C < 30 and D < 25 and E < 40)):
        return 3
    else:
        return 1
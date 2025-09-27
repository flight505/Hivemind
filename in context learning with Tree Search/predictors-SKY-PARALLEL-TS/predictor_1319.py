"""
Predictor 1319
Generated on: 2025-09-10 02:07:02
Accuracy: 54.48%
"""


# PREDICTOR 1319 - Accuracy: 54.48%
# Correct predictions: 5448/10000 (54.48%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90) or
        (B < 15 and C > 75) or
        (A > 95 and C < 15 and E > 60) or
        (B > 80 and C < 15 and D > 80) or
        (A > 75 and E > 85) or
        (B < 15 and C > 90) or
        (A > 70 and B < 30 and C < 15 and D > 50 and E > 60)):
        return 4
    elif ((B > 90 and E > 80) or
          (A > 90 and E < 10) or
          (B > 80 and D < 35 and E < 10)):
        return 2
    elif ((B > 75 and C > 70 and D > 80) or
          (A > 50 and C < 50 and D > 70 and B > 40) or
          (A < 40 and B > 75 and C > 70 and D > 80 and E < 25)):
        return 3
    else:
        return 1
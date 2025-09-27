"""
Predictor 1301
Generated on: 2025-09-10 02:02:09
Accuracy: 47.29%
"""


# PREDICTOR 1301 - Accuracy: 47.29%
# Correct predictions: 4729/10000 (47.29%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (A > 90) or
        (E > 70 and D < 30) or
        (B > 70 and C > 80 and E < 10) or
        (A < 20 and B < 15 and C > 50 and D < 50 and E < 10) or
        (A > 65 and B > 95 and C > 50 and D < 30 and E > 75) or
        (A > 70 and B > 95 and C < 60 and D < 30 and E > 75) or
        (A < 20 and B > 70 and C > 80 and D > 50 and E < 10)):
        return 4
    elif ((A > 90 and E < 10) or
          (B > 85 and C > 80) or
          (A < 25 and B < 30 and C > 30 and D < 20 and E > 65)):
        return 2
    elif ((B < 10 and D > 80) or
          (A < 5 and B > 55 and C < 10 and D < 30 and E < 40) or
          (A > 40 and B < 50 and C < 50 and D > 45)):
        return 3
    else:
        return 1
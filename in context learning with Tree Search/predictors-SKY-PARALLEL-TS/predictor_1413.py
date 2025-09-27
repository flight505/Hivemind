"""
Predictor 1413
Generated on: 2025-09-10 02:26:25
Accuracy: 50.69%
"""


# PREDICTOR 1413 - Accuracy: 50.69%
# Correct predictions: 5069/10000 (50.69%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (B > 60 and C > 60 and E < 20) or
        (E > 95 and D < 30) or
        (C > 90 and D < 40 and A > 20) or
        (A > 70 and B < 25 and C > 60 and E < 20)):
        return 4
    elif ((B > 75 and C > 60 and E < 50) or
          (A > 90 and E < 10)):
        return 2
    elif ((A > 60 and B < 20 and D < 20) or
          (A > 80 and B < 10 and D < 15) or
          (B < 10 and D > 80) or
          (B > 70 and C > 80 and D < 10)):
        return 3
    else:
        return 1
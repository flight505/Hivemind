"""
Predictor 1503
Generated on: 2025-09-10 02:35:36
Accuracy: 49.40%
"""


# PREDICTOR 1503 - Accuracy: 49.40%
# Correct predictions: 4940/10000 (49.40%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C > 30) or
        (C < 15 and D > 80) or
        (B > 90 and E > 70) or
        (A > 80 and B > 80 and C < 15 and D > 90) or
        (A > 60 and B > 60 and E > 70 and D > 45) or
        (B > 65 and C < 40 and D > 45 and E > 70) or
        (A > 65 and E > 90 and D < 25 and C < 40)):
        return 4
    elif ((B > 85 and C > 80 and E < 25 and A < 50 and D < 50) or
          (A < 40 and B < 15 and E > 50) or
          (B > 70 and D < 20 and A < 50) or
          (B > 60 and C > 90 and E > 50) or
          (B < 10 and C > 90 and E > 40)):
        return 2
    elif ((B > 80 and C > 80 and D > 90 and E < 5) or
          (A < 10 and B > 90) or
          (A > 50 and D > 90 and E < 10) or
          (B < 20 and D > 70) or
          (A > 45 and B < 20 and C < 40 and E > 40 and D < 10)):
        return 3
    else:
        return 1
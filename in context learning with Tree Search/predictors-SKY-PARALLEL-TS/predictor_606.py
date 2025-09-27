"""
Predictor 606
Generated on: 2025-09-10 00:24:42
Accuracy: 56.63%
"""


# PREDICTOR 606 - Accuracy: 56.63%
# Correct predictions: 5663/10000 (56.63%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (A < 30 and B > 80 and D < 25 and E > 90) or
        (A > 40 and B < 25 and C > 50 and D > 40 and E < 40) or
        (C > 90 and D < 30) or
        (C < 25 and E > 65 and A > 10)):
        return 4
    elif ((A > 90 and E < 10) or
          (B > 90 and C > 70 and D < 40 and A < 40) or
          (A < 40 and D < 20 and E > 50 and C > 40 and B > 50)):
        return 2
    elif ((B < 10 and D > 80) or
          (A > 60 and C < 40 and D > 50 and E < 10) or
          (A < 10 and D < 20 and E > 40 and C > 15 and B < 50) or
          (A < 10 and B > 60 and C < 25 and D < 20 and E > 40)):
        return 3
    else:
        return 1
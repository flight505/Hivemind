"""
Predictor 804
Generated on: 2025-09-10 00:50:43
Accuracy: 57.10%
"""


# PREDICTOR 804 - Accuracy: 57.10%
# Correct predictions: 5710/10000 (57.10%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (C < 15 and D > 80 and E > 80) or
        (B < 25 and C > 60 and D < 20) or
        (A > 80 and B < 10 and C < 50 and D < 50) or
        (A > 70 and B < 20 and C < 40 and D > 50 and E < 25) or
        (A < 30 and C > 90 and D < 35 and E < 15) or
        (B > 90 and C < 35 and D > 55 and A > 70)):
        return 4
    elif ((B > 85 and C > 80 and A < 50 and D > 90) or
          (B > 85 and E < 10) or
          (D < 5 and E > 50)):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (B > 90 and E < 15) or
          (A > 90 and B < 10 and D > 90)):
        return 3
    else:
        return 1
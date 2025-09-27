"""
Predictor 690
Generated on: 2025-09-10 00:34:06
Accuracy: 53.35%
"""


# PREDICTOR 690 - Accuracy: 53.35%
# Correct predictions: 5335/10000 (53.35%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and E < 20) or
        (C < 20 and D > 90) or
        (C < 20 and E > 80 and B > 50) or
        (E < 15 and C > 30 and B > 25) or
        (A > 60 and E > 80 and C < 30 and D < 50) or
        (B > 70 and C > 70 and E < 20) or
        (E < 5 and A < 30 and C > 35)):
        return 4
    elif ((A < 10 and B > 70 and E > 70) or
          (A < 10 and B < 20 and E > 90) or
          (B > 75 and E > 80 and C > 60) or
          (C > 80 and D < 10 and A > 50) or
          (E > 70 and D < 20)):
        return 2
    elif (A > 90 and B < 10 and D > 50) or (A > 95 and B < 15):
        return 3
    else:
        return 1
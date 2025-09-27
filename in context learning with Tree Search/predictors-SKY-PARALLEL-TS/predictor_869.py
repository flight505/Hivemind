"""
Predictor 869
Generated on: 2025-09-10 00:58:03
Accuracy: 57.06%
"""


# PREDICTOR 869 - Accuracy: 57.06%
# Correct predictions: 5706/10000 (57.06%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (C > 90 and D < 20) or
        (C > 80 and D < 25 and E < 20) or
        (A > 60 and B < 20 and D < 5 and E > 70) or
        (A > 60 and B < 40 and C < 40 and D < 25 and E > 90) or
        (C < 25 and E > 65)):
        return 4
    elif ((A > 90 and E < 10) or
          (B > 80 and C > 60 and E > 70) or
          (A < 5 and B > 50 and E > 60 and C < 10) or
          (B > 90 and E < 10)):
        return 2
    elif ((B < 10 and D > 80) or
          (A > 70 and E > 90 and C < 50) or
          (A > 80 and D > 90 and C < 30) or
          (A > 60 and B < 10 and C > 70 and D < 5)):
        return 3
    else:
        return 1
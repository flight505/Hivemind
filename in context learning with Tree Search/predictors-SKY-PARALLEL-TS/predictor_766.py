"""
Predictor 766
Generated on: 2025-09-10 00:44:16
Accuracy: 53.26%
"""


# PREDICTOR 766 - Accuracy: 53.26%
# Correct predictions: 5326/10000 (53.26%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 80) or
        (B < 15 and C > 80) or
        (A > 90 and B > 70 and C < 20) or
        (A < 30 and B > 70 and D > 60) or
        (B < 10 and C > 50 and E < 10)):
        return 4
    elif ((C > 90 and E < 10) or
          (A > 90 and B > 80)):
        return 2
    elif (B > 90 and D > 80):
        return 3
    else:
        return 1
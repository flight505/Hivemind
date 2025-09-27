"""
Predictor 882
Generated on: 2025-09-10 00:58:03
Accuracy: 48.46%
"""


# PREDICTOR 882 - Accuracy: 48.46%
# Correct predictions: 4846/10000 (48.46%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90) or
        (B < 15 and C > 80) or
        (E < 10 and C > 50) or
        (B > 80 and E > 90) or
        (C > 70 and E > 90) or
        (C > 80 and E < 20) or
        (C > 70 and D < 20 and E > 90) or
        (C > 80 and B < 20 and E < 20) or
        (E < 10 and B > 50)):
        return 4
    elif ((A > 90 and B > 85) or
          (B > 95 and E < 10) or
          (B > 90 and D > 80 and E < 10) or
          (A > 90 and B > 80 and C < 40)):
        return 2
    elif ((A > 70 and D > 50 and B < 40) or
          (A > 70 and C < 50 and D > 50)):
        return 3
    else:
        return 1
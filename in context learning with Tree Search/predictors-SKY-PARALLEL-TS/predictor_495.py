"""
Predictor 495
Generated on: 2025-09-10 00:08:08
Accuracy: 53.57%
"""


# PREDICTOR 495 - Accuracy: 53.57%
# Correct predictions: 5357/10000 (53.57%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 80) or
        (B > 55 and C < 30 and E > 70) or
        (B > 80 and E > 70 and C < 50)):
        return 4
    elif ((C > 90 and B < 20) or
          (D < 10 and B > 40) or
          (A < 20 and B < 50 and E < 30)):
        return 3
    elif (B > 80 and C > 50 and E > 40):
        return 2
    else:
        return 1
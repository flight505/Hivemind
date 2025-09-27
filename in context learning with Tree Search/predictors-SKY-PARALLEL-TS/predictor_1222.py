"""
Predictor 1222
Generated on: 2025-09-10 01:46:44
Accuracy: 53.42%
"""


# PREDICTOR 1222 - Accuracy: 53.42%
# Correct predictions: 5342/10000 (53.42%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and E < 20) or
        (C < 10 and D > 90) or
        (B > 70 and E > 90 and D < 20) or
        (A < 5 and D < 25 and E < 40)):
        return 4
    elif ((A > 90 and E < 10) or
          (A > 50 and B > 85 and C > 80)):
        return 2
    elif ((B < 10 and D > 80) or
          (A > 80 and D > 90)):
        return 3
    else:
        return 1
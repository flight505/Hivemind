"""
Predictor 856
Generated on: 2025-09-10 00:55:50
Accuracy: 53.66%
"""


# PREDICTOR 856 - Accuracy: 53.66%
# Correct predictions: 5366/10000 (53.66%)

def predict_output(A, B, C, D, E):
    if ((C < 20 and D > 80 and E > 80) or
        (A < 10 and B > 70) or
        (C < 10 and D > 50) or
        (C < 20 and D > 85 and A > 60)):
        return 4
    elif (B > 75 and C > 45):
        return 2
    elif ((B >= 75 and D > 80 and E > 80) or
          (A > 80 and B < 20 and C < 20)):
        return 3
    else:
        return 1
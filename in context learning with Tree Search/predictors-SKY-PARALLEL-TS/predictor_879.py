"""
Predictor 879
Generated on: 2025-09-10 00:58:03
Accuracy: 52.60%
"""


# PREDICTOR 879 - Accuracy: 52.60%
# Correct predictions: 5260/10000 (52.60%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C < 60) or
        (C < 15 and D > 75) or
        (B > 95 and D > 75) or
        (A > 95 and E > 95)):
        return 4
    elif ((B > 80 and C > 90 and D < 10) or
          (E > 95) or
          (A > 90 and E < 10)):
        return 2
    elif ((B > 70 and C > 90 and D > 70) or
          (C > 90 and D < 10) or
          (B < 10 and D > 80)):
        return 3
    else:
        return 1
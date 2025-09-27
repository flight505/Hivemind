"""
Predictor 1494
Generated on: 2025-09-10 02:35:36
Accuracy: 52.69%
"""


# PREDICTOR 1494 - Accuracy: 52.69%
# Correct predictions: 5269/10000 (52.69%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 80) or
        (E < 5 and C > 35) or
        (A > 70 and B < 10 and C > 50) or
        (C > 60 and E < 40 and B < 40) or
        (C < 30 and E < 20 and A > 40 and D < 50 and B > 30)):
        return 4
    elif (B > 90 and E > 80):
        return 2
    elif ((A > 80 and D > 80 and E > 80) or
          (A > 80 and E < 15 and C > 30)):
        return 3
    else:
        return 1
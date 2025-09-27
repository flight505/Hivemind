"""
Predictor 1165
Generated on: 2025-09-10 01:39:40
Accuracy: 46.09%
"""


# PREDICTOR 1165 - Accuracy: 46.09%
# Correct predictions: 4609/10000 (46.09%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and D > 20) or
        (C < 10 and D > 90) or
        (A > 80 and D < 30 and E > 70) or
        (B < 5 and E > 70) or
        (A > 70 and B < 15 and C < 30) or
        (C > 80 and D < 25 and E < 15) or
        (A > 50 and B < 15 and E > 70)):
        return 4
    elif ((A > 90 and E < 10) or
          (B > 75 and C > 50)):
        return 2
    elif ((B > 70 and D < 10) or
          (A > 40 and B < 30 and D < 30) or
          (A > 40 and B < 10) or
          (A < 20 and B < 20 and D > 30)):
        return 3
    else:
        return 1
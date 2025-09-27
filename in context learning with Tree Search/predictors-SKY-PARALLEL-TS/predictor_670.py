"""
Predictor 670
Generated on: 2025-09-10 00:31:36
Accuracy: 52.93%
"""


# PREDICTOR 670 - Accuracy: 52.93%
# Correct predictions: 5293/10000 (52.93%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 20 and D > 80) or
        (D > 60 and E < 10) or
        (A > 80 and B < 30 and C > 60 and E > 80) or
        (A >= 60 and C > 50 and B < 40 and E < 40) or
        (C < 20 and D > 70)):
        return 4
    elif ((A > 80 and B < 15 and C < 30 and D < 25) or
          (B > 90 and C > 80 and D > 90 and E < 15) or
          (A > 70 and B < 20 and C < 10 and D > 60) or
          (D > 90 and E > 80 and A < 50)):
        return 3
    elif ((A < 25 and B > 70 and D < 20) or
          (A > 80 and B > 80 and E < 25)):
        return 2
    else:
        return 1
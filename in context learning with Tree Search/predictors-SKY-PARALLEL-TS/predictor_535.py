"""
Predictor 535
Generated on: 2025-09-10 00:14:11
Accuracy: 48.77%
"""


# PREDICTOR 535 - Accuracy: 48.77%
# Correct predictions: 4877/10000 (48.77%)

def predict_output(A, B, C, D, E):
    if ((B - A > 60 and C > 20 and E < 20) or
        (D - C > 80) or
        (B > 90 and E > 80) or
        (D < 10 and E > 60 and B > 55) or
        (C > 60 and D < 25 and E > 80) or
        (A < 25 and B < 20)):
        return 4
    elif ((A + B > 150 and C + D < 50) or
          (B > 90 and C < 15) or
          (A < 10 and D < 10 and E > 50) or
          (A > 90 and E < 50)):
        return 2
    elif ((B + E > 150 and A + D < 50) or
          (B < 10 and D > 80)):
        return 3
    else:
        return 1
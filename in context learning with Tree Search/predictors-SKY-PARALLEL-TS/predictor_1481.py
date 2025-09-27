"""
Predictor 1481
Generated on: 2025-09-10 02:33:36
Accuracy: 53.67%
"""


# PREDICTOR 1481 - Accuracy: 53.67%
# Correct predictions: 5367/10000 (53.67%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90 and E > 80 and B > 50) or
        (B > 80 and C < 20 and D > 80 and E < 20) or
        (A < 50 and B < 30 and C > 50 and D > 40 and E < 40) or
        (B > 80 and D < 25 and E > 85)):
        return 4
    elif (A > 60 and E < 15 and C > 30):
        return 2
    elif ((A > 50 and C < 50 and D > 70 and B > 40) or
          (A > 70 and B < 20 and D < 25)):
        return 3
    else:
        return 1
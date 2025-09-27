"""
Predictor 1012
Generated on: 2025-09-10 01:15:51
Accuracy: 51.57%
"""


# PREDICTOR 1012 - Accuracy: 51.57%
# Correct predictions: 5157/10000 (51.57%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or (C < 10 and D > 90) or
        (A > 50 and B < 20 and C > 60) or
        (A > 50 and B < 20 and E > 90) or
        (A < 15 and B > 50 and C > 40 and D < 30) or
        (A > 70 and B > 60 and C > 70 and D < 25 and E > 90)):
        return 4
    elif ((A > 90 and E < 10) or (B > 80 and C > 70 and D < 30)):
        return 2
    elif ((B < 10 and D > 80) or (A > 50 and B < 5 and C < 20 and D > 40)):
        return 3
    else:
        return 1
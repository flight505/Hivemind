"""
Predictor 1221
Generated on: 2025-09-10 01:46:44
Accuracy: 53.86%
"""


# PREDICTOR 1221 - Accuracy: 53.86%
# Correct predictions: 5386/10000 (53.86%)

def predict_output(A, B, C, D, E):
    if ((B > 70 and E < 20) or
        (C < 10 and D > 90) or
        (B > 70 and D < 20 and E > 90) or
        (A < 5 and B > 60 and D < 25 and C > 50)):
        return 4
    elif (A > 80 and D > 90 and C < 40):
        return 3
    elif (B > 85 and C > 80 and E < 50):
        return 2
    else:
        return 1
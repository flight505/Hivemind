"""
Predictor 1482
Generated on: 2025-09-10 02:33:36
Accuracy: 53.56%
"""


# PREDICTOR 1482 - Accuracy: 53.56%
# Correct predictions: 5356/10000 (53.56%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90 and B > 50 and E > 80) or
        (B > 80 and D > 85 and C < 20) or
        (B > 80 and E > 80) or
        (40 < A < 50 and B < 30 and C > 50 and D > 40)):
        return 4
    elif (A > 60 and E < 10) or (B > 90 and E < 15):
        return 2
    elif (A > 70 and B < 5) or (A > 50 and C < 50 and D > 70 and B > 40):
        return 3
    else:
        return 1
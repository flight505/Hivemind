"""
Predictor 1006
Generated on: 2025-09-10 01:15:51
Accuracy: 47.12%
"""


# PREDICTOR 1006 - Accuracy: 47.12%
# Correct predictions: 4712/10000 (47.12%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (C < 10 and D > 50) or (B < 5 and A > 80):
        return 4
    elif (B > 90 and D > 70) or (B > 70 and E < 25):
        return 2
    elif (D < 25 and C > 40 and E < 50) or (C > 90) or (E < 10 and D > 40) or (C < 10 and D < 10):
        return 3
    else:
        return 1
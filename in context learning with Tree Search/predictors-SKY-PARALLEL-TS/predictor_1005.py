"""
Predictor 1005
Generated on: 2025-09-10 01:15:51
Accuracy: 45.61%
"""


# PREDICTOR 1005 - Accuracy: 45.61%
# Correct predictions: 4561/10000 (45.61%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 50) or (B < 5 and A > 80):
        return 4
    elif (B > 90 and D > 70) or (B > 70 and E < 25):
        return 2
    elif (D < 25 and C > 40 and A > 10) or (C > 90) or (E < 10 and D > 40 and C < 20) or (C < 10 and D < 10):
        return 3
    else:
        return 1
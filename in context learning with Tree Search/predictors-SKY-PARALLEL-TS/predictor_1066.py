"""
Predictor 1066
Generated on: 2025-09-10 01:25:44
Accuracy: 43.50%
"""


# PREDICTOR 1066 - Accuracy: 43.50%
# Correct predictions: 4350/10000 (43.50%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (B > 80 and E > 90 and A > 20) or (C > 80) or (B < 5 and D > 50 and E < 20):
        return 4
    elif (A > 80 and B > 80 and D > 80):
        return 2
    elif (A < 5 and C < 10 and D < 10) or (A > 90 and B < 40):
        return 3
    else:
        return 1
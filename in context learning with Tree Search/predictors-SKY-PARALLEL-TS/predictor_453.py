"""
Predictor 453
Generated on: 2025-09-10 00:04:13
Accuracy: 50.09%
"""


# PREDICTOR 453 - Accuracy: 50.09%
# Correct predictions: 5009/10000 (50.09%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C > 30) or (D - C > 70) or (B > 90 and A > 50) or (C > 35 and D < 40 and E > 70) or (E > 85 and B > 75 and A > 80):
        return 4
    elif (B > 75 and C > 55) or (B > 70 and D < 20 and E > 40):
        return 2
    elif (C > 80 and D > 85 and E > 60) or (A > 50 and C < 50 and D > 70 and B > 40):
        return 3
    else:
        return 1
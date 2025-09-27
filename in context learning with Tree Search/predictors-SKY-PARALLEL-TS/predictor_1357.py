"""
Predictor 1357
Generated on: 2025-09-10 02:12:16
Accuracy: 42.75%
"""


# PREDICTOR 1357 - Accuracy: 42.75%
# Correct predictions: 4275/10000 (42.75%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C > 25) or
        (C < 10 and D > 70) or
        (B > 55 and C > 45 and D < 25) or
        (A > 75 and C < 10 and D > 70) or
        (B > 70 and E > 95) or
        (A < 35 and B < 20 and D > 40 and E < 40)):
        return 4
    elif A > 90 and E < 10:
        return 2
    elif (B < 25 and D > 40) or (C < 20 and D > 35 and A > 40):
        return 3
    else:
        return 1
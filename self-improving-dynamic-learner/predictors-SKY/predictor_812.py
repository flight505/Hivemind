"""
Predictor 812
Generated on: 2025-09-09 21:08:04
Accuracy: 43.65%
"""


# PREDICTOR 812 - Accuracy: 43.65%
# Correct predictions: 4365/10000 (43.65%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    elif B < 20 and E > 70:
        return 4
    elif E > 90:
        return 4
    elif B > 80 and D < 20:
        return 1
    elif D >= 90 and C < 25:
        return 1
    elif C > 50 and D > 75 and B < 60:
        return 1
    elif C > 80 and E > 45:
        return 3
    elif B > 60 and C > 60:
        return 2
    else:
        return 1
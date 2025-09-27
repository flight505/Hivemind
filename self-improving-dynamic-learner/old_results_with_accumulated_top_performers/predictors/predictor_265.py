"""
Predictor 265
Generated on: 2025-09-09 06:46:06
Accuracy: 54.94%
"""


# PREDICTOR 265 - Accuracy: 54.94%
# Correct predictions: 5494/10000 (54.94%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    elif B < 20 and C < 20:
        return 3
    elif A > 50 and B > 60 and C > 60:
        return 1
    elif B > 60 and C > 60:
        return 2
    elif B > 80 and D > 70 and A > 70:
        return 2
    elif A > 80 and B > 80 and E < 10:
        return 2
    elif B > 55 and C > 20 and A < 10 and D < 50:
        return 4
    elif B > 50 and C < 15 and D > 40:
        return 3
    elif B < 60 and E > 85 and D > 70:
        return 1
    elif E > 90:
        return 4
    else:
        return 1
"""
Predictor 430
Generated on: 2025-09-10 00:02:23
Accuracy: 50.05%
"""


# PREDICTOR 430 - Accuracy: 50.05%
# Correct predictions: 5005/10000 (50.05%)

def predict_output(A, B, C, D, E):
    if E > 80:
        if B > 50 and C < 40:
            return 4
        elif B < 20:
            return 1
        else:
            return 1
    elif C < 15 and D > 90:
        if A > 90:
            return 3
        else:
            return 4
    elif A < 10 and B > 70:
        return 4
    elif B > 70 and D < 25 and E < 30:
        return 3
    elif D > 70 and C > 50 and (A + B < 115):
        return 3
    elif A < 15 and B < 20 and C < 20 and D < 30 and E < 25:
        return 3
    elif B > 85 and C > 80 and A < 50:
        return 2
    elif A > 90 and E < 10:
        return 2
    else:
        return 1
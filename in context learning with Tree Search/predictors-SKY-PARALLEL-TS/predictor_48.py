"""
Predictor 48
Generated on: 2025-09-09 23:21:45
Accuracy: 44.71%
"""


# PREDICTOR 48 - Accuracy: 44.71%
# Correct predictions: 4471/10000 (44.71%)

def predict_output(A, B, C, D, E):
    if C < 5 and B > 50 and D > 50:
        return 3
    elif B < 10 and D > 80:
        return 3
    elif C > 90 and D > 90:
        return 3
    elif A < 5 and C < 10:
        return 3
    elif C > 90 and D < 10:
        return 2
    elif B > 70 and C > 80:
        return 2
    elif B > 90:
        return 2
    elif A > 90 and E < 10:
        return 2
    elif B < 10 and C > 90:
        if A > 60:
            return 4
        else:
            return 2
    elif A < 10 and B > 70:
        return 4
    elif C < 20 and D > 40:
        return 4
    elif E < 20 and D > 50 and B < 50:
        return 4
    elif B > 60 and E < 20:
        return 4
    elif C > 70 and B < 30:
        return 4
    else:
        return 1
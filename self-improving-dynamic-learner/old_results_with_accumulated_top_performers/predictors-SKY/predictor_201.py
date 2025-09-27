"""
Predictor 201
Generated on: 2025-09-09 08:08:30
Accuracy: 41.67%
"""


# PREDICTOR 201 - Accuracy: 41.67%
# Correct predictions: 4167/10000 (41.67%)

def predict_output(A, B, C, D, E):
    if E > 90:
        if C < 30:
            return 4
        else:
            return 1
    elif B > 60 and C > 70:
        return 2
    elif B > 60 and E > 70 and C < 40:
        return 2
    elif D > 80 and B > 50 and C > 50:
        return 3
    elif C > 70 and B < 50:
        return 4
    elif C > 50 and E < 25 and D < 60:
        return 4
    elif B < 20 and C < 20:
        if E > 50:
            return 2
        else:
            return 3
    elif D > 80 and E < 20 and A > 50:
        return 3
    elif B > 60 and C < 20:
        return 3
    else:
        return 1
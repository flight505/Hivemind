"""
Predictor 69
Generated on: 2025-09-09 23:24:50
Accuracy: 54.91%
"""


# PREDICTOR 69 - Accuracy: 54.91%
# Correct predictions: 5491/10000 (54.91%)

def predict_output(A, B, C, D, E):
    if A < 10 and B > 70:
        if C < 10:
            return 2
        else:
            return 4
    elif C < 25 and D > 80 and B > 20:
        return 4
    elif A > 70 and E > 80 and D < 40:
        return 4
    elif B > 85 and C > 80:
        return 2
    elif B > 70 and D <= 20 and C > 30:
        return 3
    elif B < 20 and C < 20 and D > 60:
        return 3
    elif A > 50 and C < 50 and D > 70 and B > 40:
        return 3
    elif D < 15 and C > 40 and B < 80:
        return 3
    elif C < 10 and E < 60:
        return 3
    else:
        return 1
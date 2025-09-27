"""
Predictor 223
Generated on: 2025-09-09 05:39:53
Accuracy: 36.28%
"""


# PREDICTOR 223 - Accuracy: 36.28%
# Correct predictions: 3628/10000 (36.28%)

def predict_output(A, B, C, D, E):
    if C > 60 and B > 70:
        return 1
    elif C < 25 and D > 70:
        if E > 80:
            return 4
        else:
            return 3
    elif B < 25 and C < 25:
        return 3
    elif C > 60:
        return 2
    else:
        if A < 30 and B > 60:
            return 2
        elif D < 20 and E > 80:
            return 4
        else:
            return 1
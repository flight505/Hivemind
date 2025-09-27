"""
Predictor 250
Generated on: 2025-09-09 06:25:10
Accuracy: 48.79%
"""


# PREDICTOR 250 - Accuracy: 48.79%
# Correct predictions: 4879/10000 (48.79%)

def predict_output(A, B, C, D, E):
    if B < 25 and C < 25:
        return 3
    elif C < 25 and E > 70:
        return 4
    elif B > 70:
        if E < 40:
            return 4
        elif C > 60:
            if E > 70:
                return 1
            else:
                return 2
        else:
            return 1
    elif B > 50 and C < 40 and E < 40:
        return 3
    elif B < 25:
        if E > 60:
            return 1
        else:
            return 4
    elif A > 70 and B > 30 and C > 25:
        return 1
    else:
        return 1
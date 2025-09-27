"""
Predictor 314
Generated on: 2025-09-09 08:00:48
Accuracy: 33.44%
"""


# PREDICTOR 314 - Accuracy: 33.44%
# Correct predictions: 3344/10000 (33.44%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    elif C > 60:
        if A > 70 and B > 70:
            return 1
        else:
            return 2
    elif C < 25:
        if D > 70:
            if B < 25:
                return 3
            else:
                return 1
        else:
            return 3
    else:
        return 1
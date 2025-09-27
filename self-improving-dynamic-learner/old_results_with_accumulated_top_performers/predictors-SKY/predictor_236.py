"""
Predictor 236
Generated on: 2025-09-09 10:04:28
Accuracy: 47.30%
"""


# PREDICTOR 236 - Accuracy: 47.30%
# Correct predictions: 4730/10000 (47.30%)

def predict_output(A, B, C, D, E):
    if E > 85:
        return 4
    elif C < 15:
        return 3
    elif C > 90:
        return 1
    elif C > 70:
        if A > 60:
            return 1
        else:
            return 2
    elif 40 < C < 70:
        if D > 75 and E > 75:
            return 3
        elif B > 90:
            return 2
        else:
            return 1
    else:
        return 1
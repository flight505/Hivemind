"""
Predictor 337
Generated on: 2025-09-09 08:44:29
Accuracy: 24.14%
"""


# PREDICTOR 337 - Accuracy: 24.14%
# Correct predictions: 2414/10000 (24.14%)

def predict_output(A, B, C, D, E):
    if B > 60:
        if D > 70:
            return 4
        else:
            return 2
    elif C > 60:
        if A > 70:
            return 1
        else:
            return 3
    else:
        if E > 80:
            return 4
        else:
            return 3
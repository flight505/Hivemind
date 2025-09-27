"""
Predictor 299
Generated on: 2025-09-09 15:14:14
Accuracy: 50.14%
"""


# PREDICTOR 299 - Accuracy: 50.14%
# Correct predictions: 5014/10000 (50.14%)

def predict_output(A, B, C, D, E):
    if E > 80:
        if C > 70:
            return 2
        elif C < 30:
            return 4
        else:
            return 1
    if B > 60 and C > 70 and E > 50:
        return 2
    if B < 20 and C < 20:
        return 3
    if B < 10 and C > 30 and E < 30:
        return 4
    if 40 < B < 60 and C < 60:
        return 3
    if E < 20 and C < 40 and B > 30:
        return 4
    return 1
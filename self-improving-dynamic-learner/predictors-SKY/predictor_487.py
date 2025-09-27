"""
Predictor 487
Generated on: 2025-09-09 17:14:26
Accuracy: 59.90%
"""


# PREDICTOR 487 - Accuracy: 59.90%
# Correct predictions: 5990/10000 (59.90%)

def predict_output(A, B, C, D, E):
    if A < 10 and B > 90 and 40 < C < 60 and E < 30:
        return 4
    if B < 20 and C < 20:
        if E > 50:
            return 4
        else:
            return 3
    if C < 40 and D > 80 and E > 70:
        return 3
    if B < 50 and C < 50 and E < 30 and D < 60 and A < 80:
        return 3
    if E > 90 and C < 25:
        return 4
    if B > 60 and C > 60 and A < 40:
        return 2
    return 1
"""
Predictor 241
Generated on: 2025-09-09 10:46:47
Accuracy: 51.03%
"""


# PREDICTOR 241 - Accuracy: 51.03%
# Correct predictions: 5103/10000 (51.03%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40 and C < 30:
        return 4
    if C >= 70:
        if A >= 50:
            return 1
        else:
            return 2
    if 40 <= C < 70:
        if D > 90:
            return 3
        elif E < 30 and A < 30:
            return 4
        else:
            return 1
    if C < 20 and B < 20:
        if A < 10:
            return 2
        else:
            return 3
    if C < 20 and B > 20 and E < 20:
        return 1
    return 1
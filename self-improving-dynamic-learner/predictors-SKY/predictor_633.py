"""
Predictor 633
Generated on: 2025-09-09 18:59:01
Accuracy: 51.03%
"""


# PREDICTOR 633 - Accuracy: 51.03%
# Correct predictions: 5103/10000 (51.03%)

def predict_output(A, B, C, D, E):
    if C > 80:
        if B > 80 and E < 60:
            return 1
        elif B > 60:
            return 2
        elif B < 20:
            return 3
        else:
            return 1
    if E > 90:
        return 4
    if E > 80 and C < 40:
        return 2
    if B > 60 and 40 < C < 60 and E < 30:
        return 2
    if B > 90 and E > 80:
        return 2
    if B > 80 and C < 30 and E > 60:
        return 4
    if C < 20 and E > 70:
        return 4
    if B < 30 and C < 30:
        if D > 80 and E < 20:
            return 1
        else:
            return 3
    if B < 10 and C < 35 and E > 30:
        return 4
    return 1
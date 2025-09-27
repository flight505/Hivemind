"""
Predictor 11
Generated on: 2025-09-09 03:45:37
Accuracy: 48.54%
"""


# PREDICTOR 11 - Accuracy: 48.54%
# Correct predictions: 4854/10000 (48.54%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40 and C < 25:
        return 4
    if B > 60 and C > 70:
        return 2
    if B > 60 and E > 70 and C < 40:
        return 2
    if A < 10 and B < 40 and C > 30 and E > 50:
        return 2
    if C < 15:
        if B < 20:
            if A < 20:
                return 2
            else:
                return 3
        elif B > 50:
            if A < 20 and D < 10:
                return 3
            else:
                return 1
        else:
            return 3
    if C > 55 and E < 30:
        return 4
    if C > 70 and B < 30 and D < 30:
        return 4
    if D > 90 and C > 50 and B > 60 and E > 80:
        return 3
    if D > 80 and C < 40 and E < 10 and B < 55:
        return 3
    return 1
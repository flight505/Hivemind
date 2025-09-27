"""
Predictor 101
Generated on: 2025-09-09 05:15:45
Accuracy: 48.13%
"""


# PREDICTOR 101 - Accuracy: 48.13%
# Correct predictions: 4813/10000 (48.13%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        if A < 50:
            return 4
        else:
            return 1
    if C > 70 and B > 60 and E >= 70:
        return 2
    if C > 70 and E > 50 and D < 30:
        return 4
    if B > 60 and E > 70 and C < 40:
        return 2
    if C < 15:
        if B < 20:
            if E > 50:
                return 2
            else:
                return 3
        elif B > 50:
            return 3
        else:
            return 1
    if D >= 90 and C > 50 and B > 50:
        return 3
    if C > 55 and E < 25 and A < 20:
        return 4
    if D > 70 and C > 30 and E < 10 and A > 80:
        return 3
    if E > 50 and 20 < C < 40 and B < 40:
        return 2
    if A > 80 and B < 20 and C > 40:
        return 3
    return 1
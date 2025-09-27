"""
Predictor 886
Generated on: 2025-09-09 21:45:18
Accuracy: 57.39%
"""


# PREDICTOR 886 - Accuracy: 57.39%
# Correct predictions: 5739/10000 (57.39%)

def predict_output(A, B, C, D, E):
    if B < 20 and C > 80:
        return 1
    if B > 70 and D > 90:
        return 3
    if B > 70 and C > 60 and E > 80:
        return 1
    if B > 60 and C < 25 and E > 60:
        return 4
    if B > 70 and 30 < C < 60:
        return 2
    if D > 80 and C < 25:
        if E < 20:
            if B > 25:
                return 1
            else:
                return 3
        elif B < 20:
            return 3
        else:
            return 4
    if B < 20 and E < 10:
        return 4
    if A < 50 and B > 60 and C > 70:
        return 2
    if B > 90 and 30 <= C < 50:
        return 2
    if D > 80 and C < 15:
        return 3
    if B < 30 and C < 20 and E < 30:
        return 3
    return 1
"""
Predictor 855
Generated on: 2025-09-09 21:29:54
Accuracy: 49.37%
"""


# PREDICTOR 855 - Accuracy: 49.37%
# Correct predictions: 4937/10000 (49.37%)

def predict_output(A, B, C, D, E):
    if B > 80 and 30 <= C < 60:
        return 2
    if B > 60 and C > 75:
        if E < 30:
            return 4
        elif C > 85:
            return 1
        elif D < 30:
            return 1
        elif A < 35:
            return 2
        else:
            return 1
    if C < 25 and E > 80:
        return 4
    if C < 10 and D > 80 and E > 60:
        return 4
    if B < 20 and C < 20:
        return 3
    if E < 15 and B < 60:
        if D > 80:
            return 1
        else:
            return 3
    if B < 40 and C < 30 and D > 70 and E > 40:
        return 3
    if B < 50 and C < 40 and D > 80 and E > 80:
        return 3
    if B < 50 and D < 20 and E > 70:
        return 2
    if B > 60 and C < 30 and E > 80:
        return 4
    if B < 30 and C > 70 and E < 20:
        return 4
    if 40 <= B < 60 and 40 <= C < 50 and E < 50:
        return 3
    if B < 20 and D > 90 and E > 80:
        return 1
    if B > 70 and C > 90 and E > 70:
        return 1
    if B > 45 and C < 10:
        return 3
    if B > 70 and C < 40 and E < 30:
        return 3
    if C < 20 and D > 70 and E > 50:
        return 4
    if B < 20 and C > 50 and E < 20:
        return 4
    if B > 90 and D < 10:
        return 1
    if B > 60 and C < 25 and D > 80:
        return 4
    if B < 20 and E < 20:
        return 3
    if B < 30 and C > 70:
        return 3
    return 1
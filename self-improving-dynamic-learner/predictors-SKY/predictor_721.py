"""
Predictor 721
Generated on: 2025-09-09 20:00:49
Accuracy: 54.56%
"""


# PREDICTOR 721 - Accuracy: 54.56%
# Correct predictions: 5456/10000 (54.56%)

def predict_output(A, B, C, D, E):
    if C > 90 and E > 90:
        if B < 30:
            return 4
        elif D < 10:
            return 4
        else:
            return 1
    if B > 90 and C > 90:
        return 2
    if B > 70 and C > 90:
        return 1
    if E > 90 and C < 40:
        return 4
    if B > 60 and C < 20 and E < 10:
        if D < 40:
            return 1
        else:
            return 3
    if B < 60 and C < 30 and E > 60:
        if D < 20:
            return 1
        else:
            return 4
    if B < 40 and C < 20 and E > 50:
        if D > 80:
            return 1
        else:
            return 4
    if C > 70 and E > 90:
        return 2
    if B > 90 and C < 40 and E < 5:
        return 3
    if D > 90 and E > 70 and C < 50:
        return 3
    if B < 30 and C > 50 and D > 80 and E < 20:
        return 1
    if C > 80 and B > 60 and E < 60:
        return 1
    if B > 70 and 30 < C < 50 and E < 20:
        return 2
    if E < 10 and B < 40:
        return 4
    if B > 50 and C > 40 and E < 10:
        return 3
    if C < 20 and E > 40 and B > 40 and D < 30:
        return 3
    if C < 20 and E > 40:
        return 4
    if B > 60 and C > 60:
        if E > 80 and D > 70:
            return 3
        else:
            return 2
    if C < 20 and B < 30:
        return 3
    if B > 80 and C < 30 and E > 60:
        return 4
    if B > 60 and C > 50 and E > 90:
        return 2
    return 1
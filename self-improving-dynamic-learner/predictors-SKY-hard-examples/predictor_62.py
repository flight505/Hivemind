"""
Predictor 62
Generated on: 2025-09-09 17:46:43
Accuracy: 58.59%
"""


# PREDICTOR 62 - Accuracy: 58.59%
# Correct predictions: 5859/10000 (58.59%)

def predict_output(A, B, C, D, E):
    if C < 30 and E > 50:
        if B < 45:
            return 4
        elif A < 10 and B > 80:
            return 1
        elif A < 10:
            return 2
        else:
            return 4
    if B < 35 and C < 25:
        if E < 20 and D > 80:
            return 1
        elif E < 50:
            return 3
        else:
            return 1
    if B > 60 and C > 75 and A < 60 and E > 20:
        if D > 30:
            return 2
        else:
            return 1
    if B > 80 and E > 70 and C < 70:
        return 2
    if B > 50 and C < 25 and E < 30:
        if D < 25:
            return 3
        else:
            return 4
    if A < 10 and B < 35 and 25 < C < 45 and E < 20:
        return 4
    if B > 80 and C > 80 and D > 90 and A < 60:
        return 3
    if B > 70 and C > 70 and E < 10:
        return 1
    if B > 70 and C > 50 and E < 10:
        return 2
    if B > 70 and E > 70 and C < 50 and A >= 50 and D > 10:
        return 1
    if B > 70 and C < 40 and E > 60:
        if A < 40:
            return 4
        else:
            return 2
    if E > 85 and B > 60:
        return 4
    if 40 < B < 55 and 35 < C < 45 and D > 70:
        return 3
    if B > 45 and C < 30 and D < 40:
        return 3
    if B < 5 and A > 70:
        return 4
    if A < 10 and E < 10 and B < 40 and C > 20:
        return 4
    if B > 60 and C > 60 and E < 10 and D < 40:
        return 4
    return 1
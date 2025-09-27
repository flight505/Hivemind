"""
Predictor 37
Generated on: 2025-09-09 17:32:56
Accuracy: 53.03%
"""


# PREDICTOR 37 - Accuracy: 53.03%
# Correct predictions: 5303/10000 (53.03%)

def predict_output(A, B, C, D, E):
    if A > 90 and B < 25 and C > 45:
        return 3
    if C < 30 and E > 50:
        if B < 45:
            if A < 60 and D < 40:
                return 4
            else:
                return 1
        elif A < 10 and B > 80:
            return 1
        elif A < 10:
            return 2
        else:
            return 4
    elif C < 30:
        if B < 20:
            if C < 15:
                return 3
            else:
                return 1
        elif D > 80 and E < 20:
            return 1
        else:
            return 3
    if A < 20 and B > 55 and E < 15:
        return 4
    if A < 10 and B < 40 and C > 40 and E < 40:
        return 3
    if B > 60 and E > 50 and A > 60 and C > 40:
        if C > 60:
            return 1
        else:
            return 2
    if A < 35 and B > 60 and C > 70:
        return 2
    if A < 35 and B > 40 and C > 40 and E > 50 and D < 30:
        return 2
    if 50 < B < 65 and C > 35 and E < 30 and D > 70:
        return 3
    if B < 40 and C > 50 and E < 25:
        return 3
    if D > 50 and B < 40 and C > 45:
        return 1
    if D > 50 and B < 40 and C < 45:
        return 3
    if B > 70 and C < 35 and E > 90:
        return 2
    if E > 80 and C > 35 and B > 60 and A < 50:
        return 4
    if B > 70 and C > 65 and E < 35:
        return 1
    if B < 20 and C > 40 and E > 70:
        return 1
    if C < 5 and E > 50 and D > 90:
        return 4
    if E > 90 and C > 45 and B > 45 and B < 55:
        return 3
    if B > 95 and C > 30 and A > 90:
        return 2
    return 1
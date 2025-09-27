"""
Predictor 93
Generated on: 2025-09-09 18:07:30
Accuracy: 57.59%
"""


# PREDICTOR 93 - Accuracy: 57.59%
# Correct predictions: 5759/10000 (57.59%)

def predict_output(A, B, C, D, E):
    if C < 30 and E > 50:
        if B < 45:
            if D > 80:
                return 1
            else:
                return 4
        elif A < 10 and B > 80:
            return 1
        elif A < 10:
            return 2
        else:
            if D > 70 and B < 60:
                return 1
            else:
                return 4
    if B < 35 and C < 25:
        if E < 20 and D > 80:
            return 1
        elif E < 50:
            if A > 70 and E < 40:
                return 3
            elif D > 80:
                return 4
            else:
                return 3
        else:
            return 1
    if B > 90 and C < 10 and D > 80:
        return 2
    if C > 90 and B < 20:
        return 4
    if B < 20 and C > 70:
        return 3
    if B > 50 and C < 40 and D > 80 and E < 20:
        return 3
    if B < 40 and C < 20 and D > 80 and E > 40:
        return 4
    if E > 80 and D < 20 and C > 60 and B > 50:
        return 4
    if B < 30 and 30 < C < 40 and E < 30:
        return 3
    if A < 10 and B > 90 and C < 40:
        return 2
    if B > 60 and C >= 75 and A < 60 and E > 60:
        return 2
    if B > 70 and C < 40 and E > 70:
        return 2
    if B > 70 and C > 50 and E < 10 and D > 20:
        return 2
    if B > 70 and C >= 70 and E > 60 and A > 50:
        return 1
    if B > 70 and E > 70 and C < 50 and A >= 50 and D > 10:
        if D > 80:
            return 3
        else:
            return 1
    if B > 80 and D < 15 and E > 80:
        return 1
    if B > 90 and C < 5 and E < 5 and D > 75:
        return 1
    if B > 70 and C < 40 and E > 60 and A < 40:
        return 4
    if E > 85 and B > 60 and C < 50:
        return 4
    if 40 < B < 55 and 35 < C < 45 and D > 70:
        return 3
    if C > 70 and B > 50 and A < 50 and E < 50:
        return 4
    if 50 < B < 70 and 30 < C < 40 and D > 80 and E < 20:
        return 3
    if A < 10 and B < 35 and 25 < C < 45 and E < 20:
        return 4
    if B > 80 and C > 80 and D > 90 and A < 60:
        return 3
    if B > 80 and C > 70 and D < 10:
        return 1
    if B > 80 and C > 60 and E > 70:
        return 2
    if B > 80 and C > 80 and E < 20:
        return 2
    if B > 95 and C > 80 and D > 80:
        return 2
    if C > 60 and D < 30 and B > 50 and E < 40:
        return 1
    if C > 80 and B < 40 and D < 30:
        return 1
    if B < 30 and C < 30 and D < 30 and E < 10:
        return 1
    return 1
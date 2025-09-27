"""
Predictor 68
Generated on: 2025-09-09 17:51:20
Accuracy: 59.42%
"""


# PREDICTOR 68 - Accuracy: 59.42%
# Correct predictions: 5942/10000 (59.42%)

def predict_output(A, B, C, D, E):
    if C < 30 and E > 50:
        if B < 45:
            if A > 80:
                return 3
            elif D > 80:
                return 1
            else:
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
    if B > 55 and C < 40 and D > 80:
        if E < 10:
            return 3
        else:
            return 3
    if B > 50 and C > 55 and E > 85:
        return 2
    if A > 85 and B < 25 and C < 20:
        return 1
    if A > 90 and B > 70 and C < 10 and E < 25:
        return 4
    if A < 5 and B < 20 and C > 45 and E < 30:
        return 4
    if B > 90 and C > 85 and D > 90 and E < 15:
        return 3
    if A < 35 and B < 40 and C > 80 and E < 35:
        return 4
    if B > 85 and C > 50 and E > 90:
        return 1
    if B > 80 and C > 90 and D > 95:
        return 3
    if B > 60 and C > 75 and A < 60 and E > 60:
        return 2
    if B > 80 and E > 70 and C < 70:
        return 2
    if B > 50 and C < 25 and E < 30 and D < 25:
        return 3
    if 50 < B < 70 and 30 < C < 40 and D > 80 and E < 20:
        return 3
    if A < 10 and B < 35 and 25 < C < 45 and E < 20:
        return 4
    if B > 80 and C > 80 and D > 90 and A < 60:
        return 3
    if B > 70 and C > 70 and E < 10:
        return 1
    if B > 70 and C > 70 and D > 70 and E < 30:
        return 3
    if B > 70 and C > 50 and E < 10:
        return 2
    if B > 70 and E > 70 and C < 50 and A >= 50 and D > 10:
        return 1
    if B > 70 and C < 40 and E > 60 and A < 40:
        return 4
    if E > 85 and B > 60 and C < 50:
        return 4
    if 40 < B < 55 and 35 < C < 45 and D > 70:
        return 3
    if C > 70 and B > 50 and A < 50 and E < 50:
        return 4
    return 1
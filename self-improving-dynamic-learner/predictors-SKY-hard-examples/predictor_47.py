"""
Predictor 47
Generated on: 2025-09-09 17:38:02
Accuracy: 47.98%
"""


# PREDICTOR 47 - Accuracy: 47.98%
# Correct predictions: 4798/10000 (47.98%)

def predict_output(A, B, C, D, E):
    if C > 80:
        return 4
    if C < 30 and E >= 50:
        if B < 45:
            return 4
        elif A < 10 and B > 80:
            return 1
        elif A < 10:
            return 2
        else:
            if A > 70 and D > 90:
                return 3
            elif A > 70:
                return 1
            else:
                return 4
    if B < 35 and C < 25:
        if E < 20 and D > 80:
            return 1
        elif E < 50:
            return 3
        else:
            return 1
    if A > 90 and C < 25 and E < 20 and D > 90:
        return 4
    if B > 75 and C > 55 and E < 25:
        return 2
    if B > 60 and C > 75 and A < 60 and E > 20:
        return 2
    if B > 80 and C > 60 and E < 35 and A < 40:
        return 2
    if B > 80 and E > 70 and C < 70:
        if A >= 60:
            return 4
        else:
            return 2
    if B > 50 and C < 25 and E < 30 and D < 25:
        return 3
    if A < 10 and B < 35 and 25 < C < 45 and E < 20:
        return 4
    if B > 80 and C > 80 and D > 90 and A < 60:
        return 3
    if B > 70 and C > 70 and E < 10:
        return 1
    if B > 70 and C > 50 and E < 10:
        return 2
    if B > 70 and C > 70 and A < 40:
        return 2
    if B > 70 and E > 70 and C < 50 and A >= 50 and D > 10:
        return 1
    if B > 70 and C < 40 and E > 60 and A < 40:
        if D > 90:
            return 3
        else:
            return 4
    if B > 60 and C > 55 and E < 15:
        if D < 20:
            return 1
        else:
            return 4
    if C > 80 and E < 20:
        return 4
    if A < 30 and B > 60 and 40 < C < 55 and 40 < E < 55:
        return 4
    if E > 85 and B > 60 and C < 50:
        return 4
    if 40 < B < 55 and 35 < C < 45 and D > 70:
        if E > 70:
            return 1
        else:
            return 3
    if 35 < B < 50 and C < 35 and E < 10:
        if A < 10:
            return 4
        else:
            return 3
    if B < 20 and C < 35 and E < 10:
        return 3
    return 1
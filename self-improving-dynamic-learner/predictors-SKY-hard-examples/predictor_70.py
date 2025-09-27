"""
Predictor 70
Generated on: 2025-09-09 17:53:39
Accuracy: 58.28%
"""


# PREDICTOR 70 - Accuracy: 58.28%
# Correct predictions: 5828/10000 (58.28%)

def predict_output(A, B, C, D, E):
    if C < 30 and E > 50:
        if B > 70:
            return 1
        if B < 45:
            if A > 90:
                return 3
            elif A < 50 and D > 50:
                return 1
            else:
                return 4
        else:
            return 4
    if B < 35 and C < 25:
        if E < 20 and D > 80:
            return 1
        elif E < 50:
            return 3
        else:
            return 1
    if A < 10 and B > 60 and C < 30 and E < 30:
        return 4
    if B > 80 and C > 60 and D < 10 and E < 10:
        return 1
    if B > 60 and E > 70 and C < 45:
        return 4
    if A > 80 and D > 80 and B < 60 and E > 70:
        return 3
    if B > 90 and C < 35 and E < 5 and D > 60:
        return 2
    if B > 60 and C > 75 and A < 60 and E > 60:
        return 2
    if B > 80 and E > 60 and C < 70:
        return 2
    if B > 50 and C < 25 and E < 30 and D < 25:
        return 3
    if 50 < B < 70 and 30 < C < 40 and D > 70 and E < 20:
        return 3
    if A < 10 and B < 35 and 25 < C < 45 and E < 20:
        return 4
    if B > 80 and C > 80 and D > 90 and A < 60:
        return 3
    if B > 70 and C > 70 and E < 10:
        return 1
    if B > 70 and C > 70 and D > 70 and E < 30:
        return 3
    if B > 70 and C > 50 and E < 10 and A > 30:
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
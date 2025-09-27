"""
Predictor 89
Generated on: 2025-09-09 18:04:49
Accuracy: 55.89%
"""


# PREDICTOR 89 - Accuracy: 55.89%
# Correct predictions: 5589/10000 (55.89%)

def predict_output(A, B, C, D, E):
    if C < 30 and E > 50:
        if B < 45:
            return 4
        elif A < 10 and B > 80:
            return 1
        elif A < 10:
            return 2
        else:
            if A > 50:
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
    if B < 20 and C > 70:
        return 3
    if 40 < B < 50 and C < 35 and E < 20:
        return 4
    if 60 < B < 75 and C > 75 and E > 70 and D < 10:
        return 2
    if B > 90 and C > 80 and E > 60 and A < 30 and D > 80:
        return 2
    if B > 70 and C >= 70 and E > 60:
        return 1
    if B > 80 and D < 15 and E > 80:
        return 1
    if B > 90 and C < 5 and E < 5 and D > 75:
        return 1
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
"""
Predictor 17
Generated on: 2025-09-09 17:17:44
Accuracy: 58.39%
"""


# PREDICTOR 17 - Accuracy: 58.39%
# Correct predictions: 5839/10000 (58.39%)

def predict_output(A, B, C, D, E):
    if E > 90 and C < 30:
        return 4
    if B < 25 and C < 25:
        if E < 50:
            if E < 10 and D > 50:
                return 1
            else:
                return 3
        else:
            return 1
    if B > 60 and C > 75 and A < 60 and E > 60:
        return 2
    if B > 70 and E > 70 and C < 50 and A >= 50:
        return 4
    if B > 70 and C < 40 and E > 60 and A < 40:
        return 4
    if B > 80 and E > 70 and C < 70:
        if D > 80:
            return 3
        elif D < 40:
            return 2
        else:
            return 4
    if B > 50 and C < 25 and E < 30 and D < 25:
        return 3
    if A < 10 and B < 35 and 25 < C < 45 and E < 20:
        return 4
    return 1
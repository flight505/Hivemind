"""
Predictor 268
Generated on: 2025-09-09 14:53:38
Accuracy: 53.33%
"""


# PREDICTOR 268 - Accuracy: 53.33%
# Correct predictions: 5333/10000 (53.33%)

def predict_output(A, B, C, D, E):
    if B > 90 and C > 90:
        return 2
    if D > 90 and B < 25 and C < 25 and E < 30:
        return 1
    if C > 90 and E > 90 and B < 30:
        return 4
    if B > 60 and C > 60:
        if A < 50:
            return 2
        else:
            return 1
    if C < 30 and E > 70:
        if B > 60:
            return 1
        else:
            return 4
    if C > 70 and B < 50:
        if E > 70:
            return 1
        else:
            return 4
    if B < 30 and 30 < C < 70 and E > 90:
        return 2
    if D > 90 and B < 25 and C < 25 and E < 30:
        return 1
    if B < 30 and C < 30 and E < 40:
        if A > 40:
            return 3
        else:
            return 1
    if B < 30 and 50 < C < 70 and D > 70:
        return 1
    if 30 < B < 50 and C < 25 and E < 10:
        return 3
    if D > 80 and 50 < B < 70 and 40 < C < 50 and E > 70:
        return 3
    if B > 80 and C < 30 and E > 60:
        return 4
    if B + C < 10 and E > 90:
        return 4
    if A > 90 and B < 10 and C < 5 and D > 90:
        return 4
    if B < 35 and C > 60 and E < 40 and D < 15:
        return 3
    if B < 5 and C < 45 and E > 60:
        return 4
    if B > 45 and C < 5 and E < 40:
        return 3
    if A > 70 and B > 40 and C < 40 and E < 30 and D > 40:
        return 1
    if A > 75 and B < 35 and C > 60 and E < 40:
        return 1
    if B > 60 and C < 25 and E < 30 and D > 80:
        return 1
    if B < 35 and C > 60 and E < 40 and D < 10 and A > 70:
        return 1
    if B > 80 and C > 60 and E > 80:
        return 1
    if B > 70 and C < 25 and E < 30:
        return 1
    if A > 90 and C > 90:
        return 1
    if B < 25 and C > 60 and E < 10:
        return 4
    if E > 90 and B < 60 and C < 40:
        return 4
    if B > 70 and C < 45 and E < 30 and D > 70:
        return 3
    if B < 40 and C < 40 and E > 90:
        return 3
    if B < 30 and C < 25 and E < 40:
        return 3
    if B > 60 and C < 25 and E < 20 and D < 50:
        return 3
    if B > 40 and C < 30 and E < 30 and B < 90 and A < 90:
        return 3
    if B < 25 and C < 25 and E < 40:
        return 3
    if B < 40 and C > 70 and E < 50 and D < 50:
        return 3
    if 40 < B < 50 and 35 < C < 45 and 35 < E < 45:
        return 3
    if E < 15 and B > 40 and 30 < C < 50:
        return 3
    if B > 70 and C > 70 and D > 90 and E > 80:
        return 3
    if B > 30 and C < 10 and E < 20:
        return 3
    if B < 50 and C < 50 and E < 30 and D < 60:
        return 3
    if 55 < B < 65 and 35 < C < 45 and E < 20 and D > 70:
        return 3
    return 1
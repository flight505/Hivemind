"""
Predictor 107
Generated on: 2025-09-09 18:15:29
Accuracy: 60.29%
"""


# PREDICTOR 107 - Accuracy: 60.29%
# Correct predictions: 6029/10000 (60.29%)

def predict_output(A, B, C, D, E):
    if C < 30 and E > 50:
        if B < 45:
            return 4
        elif A < 10 and B > 80:
            return 1
        elif A < 10:
            return 2
        elif B > 80 and C < 10:
            return 1
        else:
            return 4
    if B < 35 and C < 45:
        if E < 20 and D > 80:
            return 1
        elif E < 50:
            return 3
        else:
            return 1
    if B > 60 and 40 < C < 50 and E < 20 and D > 50:
        return 2
    if A < 10 and B < 20 and 40 < C < 50 and E < 30:
        return 4
    if B < 40 and C > 30 and D > 70:
        return 1
    if C > 50 and B < 40:
        return 1
    if C > 80:
        if B < 70 or D < 80:
            return 1
        else:
            return 2
    if B < 15 and D > 70 and E > 60:
        return 3
    if B > 60 and C < 35 and D > 70 and E < 30:
        return 3
    if B > 50 and C < 25 and E < 30 and D > 50:
        return 3
    if C > 45 and E < 15 and D < 15 and B < 30:
        return 3
    if C > 90 and E < 15 and B < 35:
        return 4
    if E < 5 and C > 40 and B < 20:
        return 4
    if E < 5 and C > 50 and A < 10:
        return 4
    if B > 80 and D < 15 and E > 80:
        return 1
    if B > 90 and C < 5 and E < 5 and D > 75:
        return 1
    if B > 60 and C >= 75 and A < 60 and E > 60:
        return 2
    if B > 80 and E > 70 and C < 70:
        return 2
    if 50 < B < 70 and 30 < C < 40 and D > 80 and E < 20:
        return 3
    if A < 10 and B < 35 and 25 < C < 45 and E < 20:
        return 4
    if B > 80 and C > 80 and D > 80:
        return 2
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
        if D > 70:
            return 1
        else:
            return 4
    if C > 90 and B > 60 and E < 30:
        if A < 5:
            return 1
        else:
            return 4
    if B > 50 and C > 50 and E < 30 and D > 70:
        return 1
    if B > 60 and C > 55 and E < 30 and A < 20:
        return 4
    if B < 40 and C < 20 and D < 50 and E < 30:
        return 1
    if A > 90 and B < 10 and C < 15 and D > 90:
        return 3
    if C > 90 and B < 10 and D > 90:
        return 1
    if B < 35 and C < 20 and D > 70 and E < 30:
        return 1
    if B > 90 and C > 85 and D < 15 and E < 20:
        return 3
    if B < 25 and C > 60 and D < 20 and E > 80:
        return 2
    if A > 80 and B < 30 and C < 20 and D < 20 and E > 70:
        return 1
    return 1
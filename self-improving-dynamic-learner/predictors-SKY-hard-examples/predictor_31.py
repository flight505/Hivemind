"""
Predictor 31
Generated on: 2025-09-09 17:28:55
Accuracy: 56.10%
"""


# PREDICTOR 31 - Accuracy: 56.10%
# Correct predictions: 5610/10000 (56.10%)

def predict_output(A, B, C, D, E):
    if B > 80 and C > 80 and D > 90:
        return 3
    if C < 30 and E > 50:
        if B + D > 80:
            return 1
        else:
            return 4
    if B < 25 and C < 25:
        if E < 50:
            if E < 10 and D > 50:
                return 1
            elif D < 20:
                return 1
            else:
                return 3
        else:
            return 1
    if B < 25 and C > 40 and E < 30:
        return 4
    if C > 90 and B < 35 and E < 15:
        return 4
    if B > 60 and C > 75 and A < 60:
        return 2
    if B > 80 and E > 70 and C < 70:
        return 2
    if B > 50 and C < 25 and E < 30 and D < 25:
        return 3
    if A < 10 and B < 35 and 25 < C < 45 and E < 20:
        return 4
    if B > 70 and C > 60 and E < 25:
        if D > 80:
            return 3
        elif E < 10:
            return 2
        else:
            return 4
    if B > 70 and E > 70 and C < 50 and A >= 50 and D > 10:
        return 1
    if B > 70 and C < 40 and E > 60 and A < 40:
        return 4
    return 1
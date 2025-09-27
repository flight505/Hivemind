"""
Predictor 21
Generated on: 2025-09-09 03:54:41
Accuracy: 47.78%
"""


# PREDICTOR 21 - Accuracy: 47.78%
# Correct predictions: 4778/10000 (47.78%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40 and C < 30:
        return 4
    if C < 20:
        if B < 20 and E < 50:
            return 3
        elif E > 60:
            return 2
        else:
            if D < 20:
                return 3
            else:
                return 1
    if C > 70 and B > 60:
        return 2
    if C > 55 and E < 30 and A < 80:
        return 4
    if C > 60 and D < 30 and B < 40:
        return 4
    if D < 10 and B < 20 and C > 40:
        return 4
    if B > 60 and C < 50 and E > 50 and A > 20:
        return 2
    if B > 60 and 50 < C < 70 and E > 70 and D < 50 and A < 60:
        return 2
    if B > 70 and C > 40 and E < 20:
        return 2
    if 30 < B < 50 and 30 < C < 50 and E > 50:
        return 2
    if B > 60 and C > 50 and D > 80 and E > 60:
        return 3
    if A > 80 and D > 70 and E < 40 and C > 30:
        return 3
    return 1
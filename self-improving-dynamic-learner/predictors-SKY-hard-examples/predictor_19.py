"""
Predictor 19
Generated on: 2025-09-09 17:18:42
Accuracy: 51.99%
"""


# PREDICTOR 19 - Accuracy: 51.99%
# Correct predictions: 5199/10000 (51.99%)

def predict_output(A, B, C, D, E):
    if C < 30 and E > 50:
        return 4
    if B < 10 and C > 60 and E < 10:
        return 4
    if B < 20 and C > 40 and E < 40:
        return 4
    if B > 70 and E > 85:
        return 4
    if B > 40 and B < 70 and C > 60 and E < 60:
        return 2
    if B > 80 and C > 40 and E < 70:
        return 2
    if B < 30 and C > 90 and E > 90:
        return 2
    if B < 25 and C < 25:
        if E < 50:
            return 3
        else:
            return 1
    if B > 60 and C > 75 and E > 60:
        return 2
    if B > 80 and E > 70 and C < 70:
        return 2
    if B > 50 and C < 25 and E < 30 and D < 25:
        return 3
    if B > 80 and C > 80 and D > 90:
        return 3
    if C < 35 and D > 90 and E > 30:
        return 3
    if B > 70 and C > 60 and E < 10:
        return 2
    if B > 70 and E > 70 and C < 50 and A >= 50 and D > 10:
        return 1
    if B > 70 and C < 40 and E > 60 and A < 40:
        return 4
    if A < 10 and B < 35 and 25 < C < 45 and E < 20:
        return 4
    return 1
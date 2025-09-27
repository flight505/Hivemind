"""
Predictor 829
Generated on: 2025-09-09 21:18:02
Accuracy: 55.76%
"""


# PREDICTOR 829 - Accuracy: 55.76%
# Correct predictions: 5576/10000 (55.76%)

def predict_output(A, B, C, D, E):
    if B > 65 and C > 75 and E > 75 and A > 80:
        return 1
    if C > 90 and E > 90:
        return 1
    if B < 30 and C > 60 and E > 70:
        return 1
    if B > 80 and 35 < C < 60:
        if A > 90:
            return 1
        elif D > 20:
            return 2
        else:
            return 1
    if 50 < B < 60 and 40 < C < 50 and E < 40:
        return 1
    if B > 60 and C < 20:
        return 4
    if B < 20 and C < 40 and E < 40:
        return 3
    if B < 20 and C > 40 and E < 40:
        return 4
    if 30 < B < 40 and 40 < C < 50 and E < 40:
        return 3
    if E > 70 and C < 25:
        return 4
    if B > 80 and 35 < C < 60:
        return 2
    if B >= 60 and C > 75:
        if E < 30 or D > 80:
            return 1
        else:
            return 2
    if C > 80 and 55 < B < 70 and D > 60:
        return 3
    if E > 80 and C < 60 and B > 55:
        return 3
    if 40 < B < 55 and 40 < C < 50 and E < 40 and D < 10:
        return 3
    if A > 80 and B > 65 and C < 30:
        return 4
    if C > 95 and E < 20:
        return 4
    if C > 85 and B < 40 and D < 20:
        return 4
    if B < 40 and C > 60 and E < 30:
        return 4
    if B > 70 and C > 70 and D > 80 and E < 30:
        return 1
    if B > 50 and C > 60 and E > 70 and A < 50:
        return 4
    else:
        return 1
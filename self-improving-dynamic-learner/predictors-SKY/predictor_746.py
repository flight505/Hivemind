"""
Predictor 746
Generated on: 2025-09-09 20:18:48
Accuracy: 52.66%
"""


# PREDICTOR 746 - Accuracy: 52.66%
# Correct predictions: 5266/10000 (52.66%)

def predict_output(A, B, C, D, E):
    if B > 80 and 60 < C < 70 and E < 20:
        return 1
    if C > 75 and B < 50 and E > 80:
        return 4
    if B > 80 and C > 90 and E > 80:
        return 2
    if B > 60 and C > 60 and E < 10 and D > 50:
        return 4
    if B > 70 and C > 70 and E > 80 and D > 50:
        return 1
    if A < 20 and B < 50 and C < 25 and E > 80:
        return 2
    if B > 90 and 30 < C < 40 and E < 50:
        return 1
    if B > 80 and 30 < C < 50 and E > 40 and D < 20:
        return 1
    if A > 90 and B > 70 and C > 80 and E < 20:
        return 1
    if B > 80 and C > 70 and E < 40 and D < 20:
        return 1
    if C < 20 and D > 80 and E < 30 and B < 60:
        return 4
    if C > 80 and E > 80 and B < 50:
        return 2
    if C > 80 and B < 50 and D > 80:
        return 1
    if B > 80 and 50 < C < 70 and E < 20:
        return 3
    if 40 < C < 50 and E < 20 and B < 30:
        return 4
    if B < 25 and C < 5 and D > 80 and E > 60:
        return 4
    if B > 90 and C < 10 and E > 70:
        return 4
    if E > 90 and C < 30 and B < 50:
        return 4
    if B > 80 and C > 70 and E > 80 and D < 20:
        return 4
    if B > 70 and C < 10 and E > 90:
        return 4
    if B > 50 and C < 20 and E < 50 and A > 70 and D < 20:
        return 1
    if B < 40 and C < 15 and D > 70 and E > 50:
        return 4
    if A > 90 and B > 70 and C < 20:
        return 4
    if B > 80 and C > 70 and E < 40:
        return 2
    if B > 80 and C > 90:
        return 1
    if C > 90 and E < 20 and B < 80:
        return 4
    if B > 60 and C > 75 and E >= 70:
        return 2
    if C > 90 and B > 70 and E < 70:
        return 3
    if B > 70 and E < 10 and C > 40:
        return 4
    if B > 80 and 40 < C < 50 and D > 80:
        return 3
    if B > 40 and C < 25 and E > 90 and B < 70:
        return 2
    if B > 60 and C < 30 and E > 80:
        return 4
    if B < 10 and E > 50 and D < 20:
        return 4
    if B < 20 and C < 15:
        return 3
    if B < 20 and C < 20 and E < 10:
        return 3
    if C > 70 and B < 20 and E < 20:
        return 1
    if B < 20 and C < 30 and E > 60:
        return 2
    if C < 10 and D > 70 and E > 70:
        return 4
    if B > 50 and C > 50 and E > 70 and D < 30:
        return 4
    if B > 60 and 40 < C < 50 and E < 30:
        return 2
    if C > 80 and B < 50 and E < 50:
        return 4
    if E >= 70 and C < 30 and B < 40 and D < 50:
        return 4
    if B > 60 and C < 30 and E > 50 and D < 70:
        return 4
    if B > 80 and 30 < C < 60 and E > 40:
        return 2
    if C > 70 and B < 60 and E < 60 and D < 70:
        return 3
    if E > 80 and B < 55 and C < 60 and D < 50:
        return 3
    if B + C < 100 and D < 20:
        return 3
    return 1
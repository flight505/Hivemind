"""
Predictor 830
Generated on: 2025-09-09 21:18:22
Accuracy: 55.62%
"""


# PREDICTOR 830 - Accuracy: 55.62%
# Correct predictions: 5562/10000 (55.62%)

def predict_output(A, B, C, D, E):
    if E > 90 and C < 40 and B > 40:
        return 4
    if B < 25 and 30 < C < 45 and E < 10:
        return 3
    if B > 95 and C > 80:
        return 1
    if C < 5 and D > 60:
        return 3
    if C < 5 and E > 65:
        return 4
    if B < 10 and E > 85:
        return 4
    if B > 50 and C < 35 and D > 60 and E < 10:
        return 4
    if B < 20 and C < 20 and E > 60:
        return 4
    if B > 60 and C < 50 and E > 90:
        return 2
    if C > 75 and B > 60 and A > 80:
        return 1
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
    return 1
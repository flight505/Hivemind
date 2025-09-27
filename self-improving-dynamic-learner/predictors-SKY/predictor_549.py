"""
Predictor 549
Generated on: 2025-09-09 17:55:43
Accuracy: 55.12%
"""


# PREDICTOR 549 - Accuracy: 55.12%
# Correct predictions: 5512/10000 (55.12%)

def predict_output(A, B, C, D, E):
    if B < 30 and C > 80:
        return 4
    if B < 30 and C > 70 and E < 20:
        return 1
    if B < 15 and C < 5 and E < 20:
        return 3
    if B > 90 and C > 70 and D > 70 and E > 30:
        return 2
    if B > 80 and C < 20 and D > 60 and E > 80:
        return 4
    if B > 60 and C > 60 and E > 65 and A < 50:
        return 2
    if B > 70 and C < 30 and E > 70 and D > 70:
        return 4
    if B < 20 and 40 < C < 50 and D < 20 and E > 60:
        return 4
    if A < 10 and B > 50 and C > 80 and E < 40:
        return 4
    if A > 60 and B > 30 and C < 20 and D > 60 and E > 50:
        return 4
    if A > 70 and B < 5 and C > 60 and E < 15:
        return 4
    if A > 90 and B < 25 and C > 80 and E < 15:
        return 1
    if A < 30 and B > 60 and C > 80 and E > 70:
        return 1
    if A < 10 and B < 10 and C < 30 and D < 30 and E < 10:
        return 3
    if B < 20 and C < 15 and E <= 40:
        return 3
    if B < 20 and C > 30 and E < 60:
        return 3
    if C > 70 and B < 20 and E < 50:
        return 3
    if 30 < B < 40 and C < 20 and E < 40:
        return 3
    if B >= 70 and D > 80 and 25 < C < 50:
        return 3
    if C < 20 and E < 20 and B < 20:
        return 3
    if 30 < A < 60 and 25 < B < 35 and C < 20 and E < 15 and D > 90:
        return 1
    if B > 80 and C < 30 and E > 60:
        return 4
    if E > 80 and C < 50 and B > 20 and D < 50:
        return 4
    if E > 60 and B < 30 and C < 40 and A < 60:
        return 4
    if B < 30 and C > 90 and E > 90:
        return 4
    if C < 20 and E < 20:
        return 4
    if B > 60 and C > 60 and E > 65 and A < 50:
        return 2
    if B > 80 and C < 30 and E <= 60:
        return 1
    if B > 80 and C > 60 and E > 70:
        return 1
    if C > 50 and D > 70 and E < 40 and B < 40:
        return 1
    return 1
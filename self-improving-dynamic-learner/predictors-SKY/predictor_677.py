"""
Predictor 677
Generated on: 2025-09-09 19:28:39
Accuracy: 55.75%
"""


# PREDICTOR 677 - Accuracy: 55.75%
# Correct predictions: 5575/10000 (55.75%)

def predict_output(A, B, C, D, E):
    if B + C < 30:
        if E < 40:
            return 3
        elif E > 60:
            return 1
    if B > 60 and C > 70 and A < 40:
        return 2
    if B < 10 and C > 60:
        return 3
    if B > 70 and C < 40 and D < 20:
        return 3
    if C < 25 and D > 80 and B > 50 and E < 40:
        return 4
    if E > 90 and C < 30:
        return 4
    if D < 10 and E > 80:
        return 1
    if C > 85 and B > 60:
        return 1
    if B > 90 and 30 <= C < 50 and E < 30:
        return 1
    if B > 60 and C > 40 and E > 80 and D < 25:
        return 4
    if B > 50 and C > 80 and D > 90 and E < 50:
        return 3
    if B > 80 and C < 30 and E > 60:
        return 4
    if C > 80 and B > 80 and E < 60:
        return 1
    if A > 80 and B > 70 and C < 50 and E < 50:
        return 1
    if B > 90 and C > 90:
        return 2
    if C > 90 and E > 90 and B < 30:
        return 4
    if A + B > 160 and C < 40 and E > 50:
        return 2
    return 1
"""
Predictor 680
Generated on: 2025-09-09 19:30:21
Accuracy: 58.42%
"""


# PREDICTOR 680 - Accuracy: 58.42%
# Correct predictions: 5842/10000 (58.42%)

def predict_output(A, B, C, D, E):
    if B < 30 and C < 30:
        if D > 80 and E < 20:
            return 1
        elif E > 50:
            return 4
        else:
            return 3
    if B > 70 and C < 25:
        return 1
    if C > 80 and E < 30 and B < 60:
        return 4
    if B > 80 and C > 60 and D > 90:
        return 3
    if D > 90 and E < 20 and A > 50:
        return 3
    if C > 80 and B > 60 and E < 50:
        return 1
    if A < 50 and B > 60 and C > 60 and E < 70:
        return 2
    if B > 90 and C < 40 and E < 40:
        return 1
    if B < 20 and C > 60 and E < 30:
        return 4
    if C > 95 and E > 85:
        return 2
    if B > 80 and C < 30 and E > 60:
        return 4
    if D < 10 and E > 80:
        return 1
    if C > 85 and B > 60:
        return 1
    if B > 60 and C > 40 and E > 80 and D < 25:
        return 4
    if B < 20 and C > 70 and E > 70 and A > 90:
        return 1
    if B < 15 and C > 70 and D < 20:
        return 1
    if B > 60 and C < 20 and E > 80:
        return 4
    if A > 50 and B > 90 and C > 70:
        return 1
    if B < 20 and C > 60 and D < 10 and E > 60:
        return 2
    if B > 80 and C > 90 and D > 80:
        return 3
    if A > 40 and B < 40 and C < 50 and E < 10:
        return 4
    if B > 50 and C > 40 and D > 80 and E < 20:
        return 1
    return 1
"""
Predictor 591
Generated on: 2025-09-09 18:26:43
Accuracy: 49.31%
"""


# PREDICTOR 591 - Accuracy: 49.31%
# Correct predictions: 4931/10000 (49.31%)

def predict_output(A, B, C, D, E):
    if D > 90 and B < 60 and C < 50:
        return 3
    if B < 40 and C < 10:
        return 3
    if C < 30 and E > 60 and B < 80:
        return 4
    if C > 90 and E > 90:
        return 4
    if B > 70 and C > 60 and E > 80:
        return 1
    if B > 90 and C > 50 and E > 80 and C < 70:
        return 2
    if D > 90:
        if B > 60 and C < 50:
            return 3
        if B < 40 and E > 80:
            return 3
    if C < 20 and E > 60:
        return 4
    if B < 30 and C < 30 and E > 50:
        return 4
    if C > 90 and E < 40:
        return 3
    if B > 60 and C > 40 and D > 60:
        return 2
    if B > 90 and C > 90:
        return 2
    if B < 10 and C < 40 and E < 10:
        return 3
    if B + C < 10 and E > 90:
        return 4
    if B < 40 and C > 50 and E < 50 and D < 20:
        return 3
    if B < 5 and C < 45 and E > 60:
        return 4
    if B > 70 and C < 25 and E < 30:
        return 1
    if A < 50 and B >= 60 and C > 60 and E < 70:
        return 2
    if B > 90 and 30 < C < 50:
        return 2
    if B < 20 and C < 20:
        return 3
    if C > 70 and E > 70:
        return 2
    if B > 90 and C > 50 and E > 80:
        return 2
    if D > 80 and B < 30 and C < 20:
        return 1
    if B > 70 and C > 60:
        return 1
    if C < 40 and E > 60:
        return 4
    if B > 80 and C < 30:
        return 4
    return 1
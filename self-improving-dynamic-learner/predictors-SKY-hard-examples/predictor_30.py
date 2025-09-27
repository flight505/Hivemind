"""
Predictor 30
Generated on: 2025-09-09 17:28:02
Accuracy: 56.21%
"""


# PREDICTOR 30 - Accuracy: 56.21%
# Correct predictions: 5621/10000 (56.21%)

def predict_output(A, B, C, D, E):
    if C > 65 and E < 10:
        return 4
    if B > 85 and C < 55 and E < 55:
        return 2
    if C < 30 and E > 50:
        return 4
    if B < 25 and C < 25:
        if E < 50:
            if E < 10 and D > 50:
                return 1
            else:
                return 3
        else:
            return 1
    if B > 60 and C > 75 and A < 60:
        return 2
    if B > 80 and E > 70 and C < 70:
        return 2
    if B > 50 and C < 25 and E < 30 and D < 25:
        return 3
    if A < 10 and B < 35 and 25 < C < 45 and E < 20:
        return 4
    if B > 80 and C > 80 and D > 90:
        return 3
    if B > 70 and C > 60 and E < 10:
        return 2
    if B > 70 and E > 70 and C < 50 and A >= 50 and D > 10:
        return 1
    if B > 70 and C < 40 and E > 60 and A < 40:
        return 4
    if B > 40 and C < 20 and E > 45 and D > 70:
        return 1
    if B < 30 and C < 20 and E > 80:
        return 1
    if B > 80 and C > 85 and E > 70:
        return 1
    if B > 40 and C < 35 and D > 75 and E > 55:
        return 1
    if B > 70 and C > 80 and E < 50:
        return 1
    if B < 45 and C < 35 and D > 75 and E > 55:
        return 3
    if B > 35 and C > 75 and E > 70:
        return 2
    return 1
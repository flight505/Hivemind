"""
Predictor 29
Generated on: 2025-09-09 12:22:54
Accuracy: 50.35%
"""


# PREDICTOR 29 - Accuracy: 50.35%
# Correct predictions: 5035/10000 (50.35%)

def predict_output(A, B, C, D, E):
    if C > 60 and E < 20:
        return 4
    if B < 20 and C > 70 and E < 35 and D < 30:
        return 4
    if C < 30 and E > 70 and B > 25:
        return 4
    if B > 80 and E > 80:
        if C < 30:
            return 4
        else:
            return 2
    if E > 70 and 30 < C < 60 and B < 30:
        return 2
    if B > 60 and C < 40 and E > 50:
        return 2
    if C > 80 and E < 40:
        return 3
    if B > 60 and C < 25 and E < 20:
        return 3
    if B > 40 and C < 30 and E < 40:
        return 3
    if B < 25 and C < 25 and E < 40:
        return 3
    if B < 40 and C > 70 and E < 50 and D < 50:
        return 3
    if 40 < B < 50 and 35 < C < 45 and 35 < E < 45:
        return 3
    if A < 40 and B > 60 and C > 70 and 65 < E < 80:
        return 2
    if A < 50 and B > 60 and C > 60 and E < 20:
        return 2
    if B > 90 and C < 50:
        return 2
    if A + B > 160 and C < 40 and E < 45:
        return 2
    return 1
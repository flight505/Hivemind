"""
Predictor 43
Generated on: 2025-09-09 12:30:53
Accuracy: 56.35%
"""


# PREDICTOR 43 - Accuracy: 56.35%
# Correct predictions: 5635/10000 (56.35%)

def predict_output(A, B, C, D, E):
    if B > 90 and C > 80 and E < 20:
        return 2
    if B > 90 and C > 80:
        return 2
    if C < 30 and E > 70 and B < 40:
        return 4
    if C < 20 and E >= 50:
        return 4
    if B > 80 and E > 80 and C < 30:
        return 4
    if B < 20 and C > 70 and E < 35 and D < 30:
        return 4
    if E < 10 and B < 40 and C < 50:
        return 4
    if B < 30 and C > 60 and E < 30:
        return 4
    if B > 60 and C < 25 and E < 20 and D < 50:
        return 3
    if B > 40 and C < 30 and E < 30 and B < 90:
        return 3
    if B < 25 and C < 25 and E < 40:
        return 3
    if B < 40 and C > 70 and E < 50 and D < 50:
        return 3
    if 40 < B < 50 and 35 < C < 45 and 35 < E < 45:
        return 3
    if E < 15 and B > 40 and 30 < C < 50:
        return 3
    if B > 60 and E > 90 and C < 50:
        return 3
    if B > 70 and C > 60 and E > 45:
        return 3
    if A < 40 and B > 60 and C > 70 and 65 < E < 80:
        return 2
    if A < 50 and B > 60 and C > 60 and E < 20:
        return 2
    if B > 90 and 30 < C < 50:
        return 2
    if A + B > 160 and C < 40 and E < 45:
        return 2
    if B > 70 and C > 70 and E > 40 and A > 30:
        return 2
    return 1
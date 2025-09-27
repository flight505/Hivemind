"""
Predictor 766
Generated on: 2025-09-09 20:31:43
Accuracy: 45.71%
"""


# PREDICTOR 766 - Accuracy: 45.71%
# Correct predictions: 4571/10000 (45.71%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B > 90 and C > 60 and E < 30:
        return 3
    if B > 90 and C < 5:
        return 1
    if C > 50 and B < 25:
        return 4
    if A < 50 and B > 65 and C > 55:
        return 2
    if B > 40 and C > 80 and E > 80:
        return 2
    if E > 90 or (C < 30 and E > 70):
        return 4
    if B > 60 and C > 70:
        return 2
    if B > 70 and C > 70 and D > 90:
        return 3
    if 40 < B < 60 and 40 < C < 50:
        return 3
    if D > 80 and B < 30 and C < 20:
        return 1
    if C > 85 and B > 60 and E > 40:
        return 1
    if B > 70 and C > 60 and E > 80:
        return 1
    return 1
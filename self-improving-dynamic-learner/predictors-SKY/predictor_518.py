"""
Predictor 518
Generated on: 2025-09-09 17:34:49
Accuracy: 47.05%
"""


# PREDICTOR 518 - Accuracy: 47.05%
# Correct predictions: 4705/10000 (47.05%)

def predict_output(A, B, C, D, E):
    if B > 60 and C > 75 and E >= 70:
        return 2
    if E > 90 and C < 25:
        return 4
    if C > 75 and E < 30:
        return 4
    if C > 75 and E > 70 and B < 60:
        return 4
    if B < 20 and C < 15:
        return 3
    if B < 20 and 15 < C < 40 and E > 60:
        return 4
    if B < 20 and C > 40 and E > 60:
        return 4
    if B < 20 and C > 40 and E < 20:
        return 4
    if B < 20 and 15 < C < 40 and E < 20:
        return 4
    if B < 30 and C > 60 and E < 40:
        return 4
    if C < 10 and D > 85:
        return 4
    if B > 60 and C < 40 and E < 10:
        return 3
    if A > 20 and B > 60 and C < 50 and D > 80:
        return 3
    if C < 20 and D < 50:
        return 3
    if B > 90:
        return 1
    if B > 60 and C < 75 and E > 70:
        return 1
    if B < 30 and D > 70:
        return 1
    if 30 < B < 50 and C < 20 and D > 70 and E > 50:
        return 1
    return 1
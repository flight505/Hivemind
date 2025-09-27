"""
Predictor 312
Generated on: 2025-09-09 15:22:21
Accuracy: 51.79%
"""


# PREDICTOR 312 - Accuracy: 51.79%
# Correct predictions: 5179/10000 (51.79%)

def predict_output(A, B, C, D, E):
    if B > 70 and C > 90:
        return 1
    if B > 80 and C > 80:
        return 2
    if 40 < B < 60 and C < 15:
        return 3
    if B > 60 and C > 50 and E > 70:
        return 2
    if B > 30 and C > 30 and E > 70 and B < 60:
        return 2
    if A > 90 and B > 60 and C < 50 and E < 40:
        return 3
    if A > 90 and C < 20 and E > 70:
        return 4
    if A > 90 and B > 60 and C < 40 and E > 60:
        return 4
    if A < 10 and B > 40 and C > 30 and E > 90:
        return 2
    if E > 90 and C < 40:
        return 4
    if B > 80 and C < 30 and E > 60:
        return 4
    if C < 30 and E > 70 and B > 10:
        return 4
    if B > 90 and C > 90:
        return 2
    if A + B > 160 and C < 40 and E > 50:
        return 2
    if A < 50 and B >= 60 and C > 60:
        return 2
    if B < 30 and C < 25 and E < 40:
        return 3
    if B > 60 and C < 25 and E < 20:
        return 3
    if B < 40 and C < 40 and E > 90:
        return 3
    if B > 70 and C < 25 and E < 30:
        return 1
    if B > 60 and C > 70 and E >= 70 and A >= 50:
        return 1
    return 1
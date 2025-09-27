"""
Predictor 283
Generated on: 2025-09-09 15:01:56
Accuracy: 61.01%
"""


# PREDICTOR 283 - Accuracy: 61.01%
# Correct predictions: 6101/10000 (61.01%)

def predict_output(A, B, C, D, E):
    if B > 80 and C < 30 and E > 60:
        return 4
    if E > 90 and C < 40:
        return 4
    if B < 30 and C > 60 and E < 40:
        return 4
    if C < 20 and E > 50:
        return 4
    if B > 70 and C < 45 and E < 30 and D > 70:
        return 3
    if B < 30 and C < 25 and E < 40:
        return 3
    if D > 90 and E < 30:
        return 3
    if B > 60 and C < 25 and E < 20:
        return 3
    if B > 70 and C > 80 and E < 50:
        return 1
    if A < 50 and B > 60 and C > 60 and E < 70:
        return 2
    if B > 90 and 30 < C < 50:
        return 2
    if A + B > 160 and C < 40 and E > 50:
        return 2
    if B > 70 and C < 25 and E < 30:
        return 1
    if A > 70 and B > 40 and C < 40 and E < 30:
        return 1
    return 1
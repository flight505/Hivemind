"""
Predictor 45
Generated on: 2025-09-09 12:34:09
Accuracy: 55.46%
"""


# PREDICTOR 45 - Accuracy: 55.46%
# Correct predictions: 5546/10000 (55.46%)

def predict_output(A, B, C, D, E):
    if C < 25 and E > 90 and A > 30:
        return 4
    if B < 20 and C > 70 and E > 50:
        return 4
    if B > 80 and C < 35 and E > 60:
        return 4
    if B < 20 and E < 20 and D > 50:
        return 4
    if B < 25 and C < 25:
        return 3
    if B < 20 and E < 30:
        return 3
    if B > 80 and C > 80 and E < 10:
        return 3
    if E > 90 and C < 25 and A < 30:
        return 2
    if B > 80 and E > 90 and C > 30:
        return 2
    if A < 50 and B > 60 and C > 60 and 60 < E < 85:
        return 2
    return 1
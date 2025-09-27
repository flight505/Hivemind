"""
Predictor 255
Generated on: 2025-09-09 14:43:23
Accuracy: 53.11%
"""


# PREDICTOR 255 - Accuracy: 53.11%
# Correct predictions: 5311/10000 (53.11%)

def predict_output(A, B, C, D, E):
    if A < 25 and B > 90 and C < 25 and E > 40:
        return 1
    if B > 90 and C > 90:
        return 2
    if B > 90 and 30 < C < 50:
        return 2
    if B > 60 and C > 70 and E > 70:
        return 2
    if B < 20 and C < 30 and E > 70:
        return 2
    if B < 20 and C < 15:
        return 3
    if B < 50 and C < 50 and D < 20:
        return 3
    if A > 80 and B > 50 and C < 40 and D > 90:
        return 3
    if B > 60 and C > 60 and E < 30:
        return 4
    if B > 60 and C < 30:
        return 4
    if C < 25 and E > 90:
        return 4
    if D > 90 and B < 25 and C < 25 and E < 30:
        return 1
    if C > 90 and E > 90 and B < 30:
        return 4
    if B + C < 10 and E > 90:
        return 4
    return 1
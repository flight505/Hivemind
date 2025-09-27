"""
Predictor 827
Generated on: 2025-09-09 21:16:46
Accuracy: 52.28%
"""


# PREDICTOR 827 - Accuracy: 52.28%
# Correct predictions: 5228/10000 (52.28%)

def predict_output(A, B, C, D, E):
    if B > 65 and C > 75 and E > 75:
        return 1
    if C > 90 and E > 90:
        return 4
    if B < 30 and C > 60 and E > 70:
        return 4
    if B > 80 and 35 < C < 60 and E < 40:
        return 1
    if B < 20 and C < 40 and E < 40:
        return 3
    if B < 20 and C > 40 and E < 40:
        return 4
    if 30 < B < 40 and 40 < C < 50 and E < 40:
        return 3
    if E > 70 and C < 25:
        return 4
    if B > 80 and 35 < C < 60:
        return 2
    if B >= 60 and C > 75:
        return 2
    if C > 80 and 55 < B < 70 and D > 60:
        return 3
    if E > 80 and C < 60 and B > 55:
        return 3
    if 40 < B < 55 and 40 < C < 50 and E < 40 and D < 10:
        return 3
    if A > 80 and B > 65 and C < 30:
        return 4
    if C > 95 and E < 20:
        return 4
    if C > 85 and B < 40 and D < 20:
        return 4
    return 1
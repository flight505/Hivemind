"""
Predictor 586
Generated on: 2025-09-09 18:23:55
Accuracy: 57.24%
"""


# PREDICTOR 586 - Accuracy: 57.24%
# Correct predictions: 5724/10000 (57.24%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 25 and E < 40:
        return 3
    if B < 20 and C < 25:
        return 1
    if B < 10 and C > 70:
        return 1
    if B < 20 and C > 90:
        return 1
    if B < 30 and C > 50 and D > 70:
        return 1
    if B > 90 and C > 60 and D < 20:
        return 1
    if B > 80 and C < 25 and D > 80:
        return 1
    if C < 25 and E > 90:
        return 4
    if B > 80 and C < 25:
        return 4
    if B < 40 and C < 10:
        return 4
    if C < 5 and D > 80:
        return 4
    if C > 70 and D < 20 and E > 70:
        return 2
    if B > 90 and C > 70:
        return 2
    if B > 40 and C > 80 and D < 20 and E < 30:
        return 3
    if C > 70 and E < 30 and D < 20:
        return 3
    if 20 < B < 30 and C < 20 and D > 90:
        return 1
    if B > 70 and C > 60 and E > 70:
        return 1
    return 1
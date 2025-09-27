"""
Predictor 670
Generated on: 2025-09-09 19:24:02
Accuracy: 50.96%
"""


# PREDICTOR 670 - Accuracy: 50.96%
# Correct predictions: 5096/10000 (50.96%)

def predict_output(A, B, C, D, E):
    if B > 70 and C < 20:
        return 1
    if B > 90 and C > 90:
        return 2
    if B > 60 and C > 70 and E > 70:
        return 2
    if A > 70 and B > 40 and C < 10:
        return 1
    if B < 40 and D > 60 and E > 70:
        return 3
    if B < 20 and C < 20:
        return 3
    if C >= 70 and D < 20 and B < 60:
        return 3
    if B > 60 and C > 40 and E > 80:
        return 4
    if B < 30 and C > 80 and E < 40:
        return 1
    if B > 50 and C < 30 and E > 70:
        return 4
    if D < 10 and E > 80:
        return 1
    if C > 85 and B > 60 and E > 40:
        return 1
    if E > 90:
        return 4
    if B > 80 and C < 30 and E > 60:
        return 4
    if (C < 25 or A > 90) and E > 70:
        return 4
    return 1
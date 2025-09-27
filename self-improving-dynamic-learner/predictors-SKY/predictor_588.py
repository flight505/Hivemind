"""
Predictor 588
Generated on: 2025-09-09 18:25:16
Accuracy: 50.51%
"""


# PREDICTOR 588 - Accuracy: 50.51%
# Correct predictions: 5051/10000 (50.51%)

def predict_output(A, B, C, D, E):
    if B > 90 and D > 90:
        return 2
    if C > 70 and D > 90:
        return 1
    if C > 70 and E < 10:
        return 4
    if A > 90 and B < 10 and C < 10:
        return 1
    if B < 10 and C > 90:
        return 1
    if B < 10 and C > 90 and D < 10:
        return 2
    if B < 20 and C > 80:
        return 1
    if B > 30 and C < 10:
        return 3
    if B > 60 and C > 40 and E > 50:
        return 2
    if C > 90 and D < 10:
        return 2
    if C < 40 and E > 60:
        return 4
    if B < 20 and C > 70:
        return 4
    if B < 20 and C < 20:
        return 3
    if C > 70 and E >= 70:
        return 2
    if B > 90 and C > 50 and E > 80:
        return 2
    if D > 80 and B < 30 and C < 20:
        return 1
    if B > 70 and C > 60:
        return 1
    return 1
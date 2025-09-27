"""
Predictor 739
Generated on: 2025-09-09 20:14:41
Accuracy: 50.51%
"""


# PREDICTOR 739 - Accuracy: 50.51%
# Correct predictions: 5051/10000 (50.51%)

def predict_output(A, B, C, D, E):
    if B > 80 and C > 90:
        return 1
    if C > 90 and E < 20 and B < 80:
        return 4
    if B > 60 and C > 75 and E >= 70:
        return 2
    if B > 70 and E < 10 and C > 40:
        return 4
    if B > 80 and 40 < C < 50 and D > 80:
        return 3
    if B > 40 and C < 25 and E > 90:
        return 2
    if B > 60 and C < 30 and E > 80:
        return 4
    if B < 10 and E > 50 and D < 20:
        return 4
    if B < 20 and C < 15:
        return 3
    if C > 80 and B < 50 and E < 50:
        return 4
    if E >= 70 and C < 30 and B < 40:
        return 4
    if B > 60 and C < 30 and E > 50 and D < 70:
        return 4
    if B > 80 and 30 < C < 60 and E > 40:
        return 2
    if C > 70 and B < 60 and E < 60:
        return 3
    if E > 80 and B < 55 and C < 60:
        return 3
    if B + C < 100 and D < 20:
        return 3
    return 1
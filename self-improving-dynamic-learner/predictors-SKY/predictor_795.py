"""
Predictor 795
Generated on: 2025-09-09 20:55:26
Accuracy: 44.19%
"""


# PREDICTOR 795 - Accuracy: 44.19%
# Correct predictions: 4419/10000 (44.19%)

def predict_output(A, B, C, D, E):
    if B + C < 25:
        return 3
    if E > 70 and C < 40:
        return 4
    if B < 25 and C > 70 and D > 90:
        return 1
    if B < 40 and C > 90 and D > 90:
        return 1
    if B < 40 and C > 60 and E > 80:
        return 4
    if B > 55 and C > 50 and D > 75 and E > 75:
        return 3
    if B > 90 and C > 90 and D < 30:
        return 1
    if B > 90 and C < 40 and E > 90:
        return 2
    if B < 40 and C < 30 and E > 60:
        return 4
    if B < 30 and C < 20 and D < 20:
        return 3
    if B > 70 and C > 90 and D > 90 and E > 80:
        return 3
    if B > 60 and C > 70:
        return 2
    if B > 80 and 35 < C < 55:
        return 2
    if B < 50 and C > 70:
        return 3
    if B > 70 and C < 50 and E < 25 and D > 80:
        return 3
    if E > 90 and B < 60 and C < 30:
        return 4
    if B > 80 and C < 30 and E > 60:
        return 4
    if 40 < B < 60 and 40 < C < 60 and 30 < E < 50:
        return 3
    if D < 10 and E > 80:
        return 1
    if C > 85 and B > 60 and E > 40:
        return 1
    if C > 80 and B > 80 and E < 60:
        return 1
    if D > 80 and B < 30 and C < 20:
        return 1
    return 1
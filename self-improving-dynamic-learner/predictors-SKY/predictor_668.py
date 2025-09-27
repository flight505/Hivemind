"""
Predictor 668
Generated on: 2025-09-09 19:23:25
Accuracy: 51.02%
"""


# PREDICTOR 668 - Accuracy: 51.02%
# Correct predictions: 5102/10000 (51.02%)

def predict_output(A, B, C, D, E):
    if B < 10 and C > 70:
        return 1
    if B > 90 and C > 90:
        return 2
    if B >= 80 and E > 90:
        return 2
    if B > 85 and E < 10 and C < 45:
        return 2
    if C > 80 and E > 90:
        return 2
    if B > 60 and C > 70 and E > 70:
        return 2
    if B > 80 and C > 60 and D < 20:
        return 1
    if E > 90:
        return 4
    if B > 80 and C < 30 and E > 60:
        return 4
    if C > 40 and B < 40 and D <= 30:
        return 4
    if B >= 80 and C < 20 and E < 20:
        return 4
    if B < 10 and C < 10 and E > 40:
        return 4
    if B < 20 and C < 20:
        return 3
    if B < 20 and D > 90:
        return 3
    if D > 90 and B < 50 and C < 40 and E > 60:
        return 3
    if D > 90 and C < 30 and B > 60:
        return 3
    if B > 90 and E < 10:
        return 3
    if C < 25 and E < 30 and B > 40:
        return 3
    if A < 30 and C > 70 and E < 40:
        return 3
    if B < 35 and C < 10 and E < 10:
        return 3
    if D < 10 and E > 80:
        return 1
    if C > 85 and B > 60 and E > 40:
        return 1
    if B > 70 and C < 20:
        return 1
    return 1
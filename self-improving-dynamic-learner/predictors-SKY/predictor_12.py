"""
Predictor 12
Generated on: 2025-09-09 12:12:20
Accuracy: 57.24%
"""


# PREDICTOR 12 - Accuracy: 57.24%
# Correct predictions: 5724/10000 (57.24%)

def predict_output(A, B, C, D, E):
    if C < 30 and E > 90:
        return 4
    if C > 70 and E < 30 and B > 40 and D > 50:
        return 4
    if C < 15 and E > 40 and D > 60:
        return 4
    if B > 65 and E < 20 and C < 35:
        return 4
    if E > 90 and D < 20:
        return 4
    if B < 20 and C < 20:
        return 3
    if B < 20 and C < 45 and A > 70:
        return 3
    if C < 20 and B > 30 and D > 60 and E < 50:
        return 3
    if C < 30 and B > 60 and D > 70 and E < 50:
        return 3
    if A < 40 and B > 60 and C > 60 and E > 60:
        return 2
    if A < 40 and B > 70 and E < 25:
        return 2
    if A < 20 and B < 20 and C > 40 and D < 10:
        return 2
    return 1
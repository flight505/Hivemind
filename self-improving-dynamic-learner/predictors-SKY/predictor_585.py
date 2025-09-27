"""
Predictor 585
Generated on: 2025-09-09 18:23:18
Accuracy: 50.25%
"""


# PREDICTOR 585 - Accuracy: 50.25%
# Correct predictions: 5025/10000 (50.25%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if C < 25 and E > 70:
        return 4
    if C > 90 and D < 20:
        return 1
    if B < 50 and C > 70 and E > 80:
        return 4
    if B >= 80 and C < 50 and D < 50:
        return 4
    if B > 40 and C < 30 and E > 60:
        return 2
    if B > 70 and E > 90:
        return 2
    if B > 60 and C > 75 and E > 60:
        return 2
    if B < 20 and C > 60:
        return 4
    if B > 80 and C < 30:
        return 1
    if D > 80 and C < 20:
        return 1
    if B > 70 and C > 60 and E > 70:
        return 1
    return 1
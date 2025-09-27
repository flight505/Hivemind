"""
Predictor 598
Generated on: 2025-09-09 18:32:12
Accuracy: 49.34%
"""


# PREDICTOR 598 - Accuracy: 49.34%
# Correct predictions: 4934/10000 (49.34%)

def predict_output(A, B, C, D, E):
    if B > 80 and C < 30 and E < 20:
        return 1
    if B > 80 and E < 10:
        return 1
    if C > 70 and E < 5:
        return 1
    if B > 90 and C > 65:
        return 1
    if C < 5 and B > 50:
        return 1
    if B < 30 and C < 20 and D < 20:
        return 1
    if B > 80 and C < 15 and E < 5:
        return 1
    if B < 35 and C < 25 and D > 90:
        return 1
    if B < 35 and C > 50 and D > 70:
        return 1
    if B > 90 and C < 25:
        return 1
    if C > 75 and E > 65:
        return 2
    if C > 50 and E > 60 and B < 50:
        return 2
    if B < 20 and C < 15:
        return 3
    if B > 70 and C < 45 and D > 80 and E < 15:
        return 3
    if C < 25 and E > 90:
        return 4
    if C < 35 and E < 10 and D > 60:
        return 4
    if E < 10 and C > 50:
        return 4
    if B > 60 and C < 25:
        return 4
    return 1
"""
Predictor 663
Generated on: 2025-09-09 19:18:40
Accuracy: 55.65%
"""


# PREDICTOR 663 - Accuracy: 55.65%
# Correct predictions: 5565/10000 (55.65%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20 and E < 50:
        return 3
    if B < 20 and C < 20 and E > 80:
        return 2
    if B < 20 and C > 50 and E < 30:
        return 4
    if E > 90:
        return 4
    if E > 70 and B < 40 and C < 40:
        return 4
    if B >= 70 and C < 20:
        return 1
    if B > 60 and C > 75 and E > 65 and D < 10:
        return 2
    if B > 80 and C > 75 and E > 65:
        return 2
    if B < 40 and C > 60 and E > 80 and D < 10:
        return 2
    if D < 10 and E > 80:
        return 1
    if C > 85 and B > 60 and E > 40:
        return 1
    if C > 80 and B > 80 and E < 60:
        return 1
    if B > 80 and C < 30 and E > 60:
        return 4
    if B > 60 and C > 40 and E > 80 and D < 25:
        return 4
    return 1
"""
Predictor 25
Generated on: 2025-09-09 23:19:12
Accuracy: 47.14%
"""


# PREDICTOR 25 - Accuracy: 47.14%
# Correct predictions: 4714/10000 (47.14%)

def predict_output(A, B, C, D, E):
    if C > 90 and D > 90:
        return 3
    if C < 10 and D < 50:
        return 3
    if A < 10 and B > 70 and E < 20:
        return 4
    if C < 10 and D > 90:
        return 4
    if B < 10 and C > 90:
        if A > 80:
            return 4
        else:
            return 2
    if C > 70 and B < 30 and E < 40:
        return 4
    if B < 15 and E < 20:
        return 4
    if E > 80:
        return 4
    if B > 90:
        return 2
    if A > 90 and E < 10:
        return 2
    if B < 10 and D > 80:
        return 3
    else:
        return 1
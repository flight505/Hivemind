"""
Predictor 26
Generated on: 2025-09-09 23:19:12
Accuracy: 53.45%
"""


# PREDICTOR 26 - Accuracy: 53.45%
# Correct predictions: 5345/10000 (53.45%)

def predict_output(A, B, C, D, E):
    if C < 10 and D > 90:
        return 4
    if A < 10 and B > 70 and E < 20:
        return 4
    if B < 10 and E < 20:
        return 4
    if C > 90 and D < 30 and A > 80:
        return 4
    if C > 70 and D < 30 and B > 15:
        return 4
    if E > 80 and D < 40:
        return 4
    if E > 90 and C < 20:
        return 4
    if C > 90 and D > 90:
        return 3
    if C < 10 and A < 10:
        return 3
    if B > 90:
        return 2
    if B < 10 and C > 90 and A < 80:
        return 2
    if A > 90 and E < 10:
        return 2
    return 1
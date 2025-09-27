"""
Predictor 510
Generated on: 2025-09-09 17:29:55
Accuracy: 53.94%
"""


# PREDICTOR 510 - Accuracy: 53.94%
# Correct predictions: 5394/10000 (53.94%)

def predict_output(A, B, C, D, E):
    if B > 60 and C > 60 and A > 50:
        return 1
    if B > 60 and C > 60:
        return 2
    if A < 20 and B > 60 and E > 70:
        return 2
    if B > 80 and C < 30 and D > 80 and E < 40:
        return 4
    if E > 80 and B < 40:
        return 4
    if E < 20 and B > 50 and C > 40:
        return 4
    if B < 20 and C < 20:
        return 3
    if C < 10 and D > 50:
        return 3
    if B > 60 and C < 40 and D > 70 and A > 20:
        return 3
    if B > 60 and D > 70 and E > 60:
        return 3
    if B < 50 and C < 25 and E < 20 and D < 50:
        return 3
    return 1
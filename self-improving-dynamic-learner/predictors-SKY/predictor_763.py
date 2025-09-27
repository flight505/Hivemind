"""
Predictor 763
Generated on: 2025-09-09 20:29:59
Accuracy: 45.89%
"""


# PREDICTOR 763 - Accuracy: 45.89%
# Correct predictions: 4589/10000 (45.89%)

def predict_output(A, B, C, D, E):
    if B > 60 and C > 70 and A < 35:
        return 2
    if B > 90 and C > 30 and A < 40:
        return 2
    if E > 90:
        return 4
    if B > 50 and C < 30 and E > 80:
        return 4
    if C > 50 and E < 10:
        return 4
    if B < 30 and C > 50 and D < 50 and E < 25:
        return 4
    if B < 10 and E > 70:
        return 1
    if min(B, C) < 20 and not (D > 90 and E < 20):
        return 3
    if B > 50 and C > 70 and D < 20:
        return 3
    return 1
"""
Predictor 277
Generated on: 2025-09-09 14:58:47
Accuracy: 55.28%
"""


# PREDICTOR 277 - Accuracy: 55.28%
# Correct predictions: 5528/10000 (55.28%)

def predict_output(A, B, C, D, E):
    if E > 90 and C < 30:
        return 4
    if C > 60 and B < 15 and E < 30:
        return 4
    if B > 50 and C < 45 and E < 20 and D > 30:
        return 4
    if B < 25 and C < 40 and E < 30 and A > 50 and D > 40:
        return 4
    if B > 70 and C < 45 and E < 30 and D > 70:
        return 3
    if B < 25 and C < 25 and E < 40:
        return 3
    if A < 60 and B > 55 and C > 45 and (E < 95 or B > 80):
        return 2
    return 1
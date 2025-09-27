"""
Predictor 1381
Generated on: 2025-09-10 02:16:28
Accuracy: 49.63%
"""


# PREDICTOR 1381 - Accuracy: 49.63%
# Correct predictions: 4963/10000 (49.63%)

def predict_output(A, B, C, D, E):
    if A > 70 and B > 80 and C < 20:
        return 4
    if E < 5 and D > 50:
        return 4
    if B > 90 and A > 80:
        return 2
    if A < 10 and B > 70:
        return 4
    if C < 15 and D > 80:
        return 4
    if E > 90 and B < 20:
        return 4
    if D > 90 and C < 10:
        return 4
    if B > 85 and C > 80:
        return 2
    if A < 30 and B > 90:
        return 2
    if A < 20 and B > 95:
        return 2
    if D > 70 and C < 35:
        return 3
    if A > 80 and E > 75:
        return 3
    if A < 5 and D > 30 and E < 30:
        return 3
    if A > 40 and B > 60 and D > 70:
        return 3
    else:
        return 1
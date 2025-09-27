"""
Predictor 507
Generated on: 2025-09-09 17:26:39
Accuracy: 45.17%
"""


# PREDICTOR 507 - Accuracy: 45.17%
# Correct predictions: 4517/10000 (45.17%)

def predict_output(A, B, C, D, E):
    if B + C < 30:
        return 3
    if C < 10 and B > 50:
        return 3
    if C < 20 and D < 50:
        return 3
    if E < 5 and D > 90:
        return 3
    if B > 70 and D > 80 and C < 50 and A > 20 and E > 30:
        return 3
    if E > 90:
        return 4
    if E > 70 and C < 30 and A > 60:
        return 4
    if C >= 70 and E > 60 and B < 30:
        return 4
    if C > 65 and E < 40:
        return 4
    if B > 80 and C < 25 and E < 20:
        return 4
    if A < 50 and B > 45 and C > 45 and E >= 70:
        return 2
    return 1
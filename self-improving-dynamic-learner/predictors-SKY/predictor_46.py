"""
Predictor 46
Generated on: 2025-09-09 12:35:16
Accuracy: 52.39%
"""


# PREDICTOR 46 - Accuracy: 52.39%
# Correct predictions: 5239/10000 (52.39%)

def predict_output(A, B, C, D, E):
    if C < 25 and E > 90 and A > 30:
        return 4
    if B < 20 and C > 70:
        return 4
    if B > 80 and C < 35 and E > 60:
        return 4
    if B < 20 and E < 20 and D > 50:
        return 4
    if C <= 20 and E >= 50 and B < 20:
        return 4
    if B > 70 and C > 80:
        return 4
    if C < 10:
        return 3
    if B > 40 and C > 80 and E < 30:
        return 3
    if E > 90 and B > 50 and C < 50:
        return 3
    if B < 25 and C < 25 and (A > 30 or E < 30):
        return 3
    if B < 20 and E < 30:
        return 3
    if B > 80 and C > 80 and E < 10:
        return 3
    if A < 50 and B > 60 and C > 70 and (B > 85 or D < 20):
        return 2
    if A < 50 and B > 60 and C > 45 and E > 60 and (B / C > 1.3):
        return 2
    if E > 90 and C < 25 and A < 30:
        return 2
    if B > 80 and E > 90 and C > 30:
        return 2
    return 1
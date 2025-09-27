"""
Predictor 771
Generated on: 2025-09-09 20:39:43
Accuracy: 46.83%
"""


# PREDICTOR 771 - Accuracy: 46.83%
# Correct predictions: 4683/10000 (46.83%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    if E >= 80 and C < 30:
        return 4
    if A > 80 and B > 65 and C < 30:
        return 4
    if C > 80 and D < 20:
        return 4
    if C > 90 and E < 20 and B < 50:
        return 4
    if 50 < B < 65 and C > 80:
        return 3
    if B < 65 and C > 50 and D > 80:
        return 3
    if 40 < B < 55 and 40 < C < 55 and D < 10:
        return 3
    if B > 80 and 30 < C < 55:
        return 2
    if B > 60 and C > 75:
        return 2
    return 1
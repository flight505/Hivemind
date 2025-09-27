"""
Predictor 575
Generated on: 2025-09-09 18:17:07
Accuracy: 56.39%
"""


# PREDICTOR 575 - Accuracy: 56.39%
# Correct predictions: 5639/10000 (56.39%)

def predict_output(A, B, C, D, E):
    if B < 30 and C > 70 and E < 30:
        return 4
    if C < 25 and E > 70:
        return 4
    if B < 20 and C < 20 and D > 60:
        return 4
    if B > 70 and C < 35 and E > 50:
        return 4
    if B > 80 and C < 40 and D > 60:
        return 2
    if B > 80 and C > 60:
        return 2
    if A > 80 and B < 15:
        return 3
    if D > 80 and E > 80 and C < 50:
        return 3
    if B < 15 and C < 15:
        return 3
    if B > 60 and C > 70 and E > 70:
        return 2
    if B + C + E < 60:
        return 3
    return 1
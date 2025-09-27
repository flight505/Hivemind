"""
Predictor 331
Generated on: 2025-09-09 15:32:14
Accuracy: 52.39%
"""


# PREDICTOR 331 - Accuracy: 52.39%
# Correct predictions: 5239/10000 (52.39%)

def predict_output(A, B, C, D, E):
    if B > 60 and C > 70:
        return 2
    if E > 90 and C < 25:
        return 4
    if B < 30 and C < 20 and A > 40:
        return 3
    if B < 30 and C < 20:
        return 1
    if B > 90:
        return 1
    if B < 35 and C > 50 and D > 70:
        return 1
    return 1
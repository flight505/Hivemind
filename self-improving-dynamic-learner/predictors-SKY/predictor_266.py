"""
Predictor 266
Generated on: 2025-09-09 14:50:57
Accuracy: 52.72%
"""


# PREDICTOR 266 - Accuracy: 52.72%
# Correct predictions: 5272/10000 (52.72%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    if B > 80 and C < 30 and E > 60:
        return 4
    if E > 90:
        return 4
    if B < 20 and 30 < C < 60:
        return 3
    if B < 30 and 40 < C < 60:
        return 3
    if B > 60 and C < 50 and D > 70 and A > 80:
        return 3
    if A < 25 and B > 45 and C < 30 and E > 60:
        return 2
    if A < 50 and B > 60 and C > 70 and E > 65:
        return 2
    return 1
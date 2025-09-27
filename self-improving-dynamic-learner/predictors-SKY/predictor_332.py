"""
Predictor 332
Generated on: 2025-09-09 15:33:04
Accuracy: 52.06%
"""


# PREDICTOR 332 - Accuracy: 52.06%
# Correct predictions: 5206/10000 (52.06%)

def predict_output(A, B, C, D, E):
    if A + B + C > 210:
        return 1
    if B > 60 and C > 50:
        return 2
    if B > 30 and C > 30 and A < 20:
        return 2
    if E > 90 and C < 25:
        return 4
    if B < 30 and C < 20 and D > 90 and E > 40:
        return 4
    if B < 30 and C < 20 and D > 90 and E < 20:
        return 1
    if B < 35 and C < 20 and A > 20:
        return 3
    if B > 50 and C < 35 and E < 10:
        return 3
    if 40 < B < 60 and C < 15 and D > 50:
        return 3
    if B < 35 and C > 50 and D > 70:
        return 1
    return 1
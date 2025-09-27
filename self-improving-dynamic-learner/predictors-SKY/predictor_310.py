"""
Predictor 310
Generated on: 2025-09-09 15:20:45
Accuracy: 48.16%
"""


# PREDICTOR 310 - Accuracy: 48.16%
# Correct predictions: 4816/10000 (48.16%)

def predict_output(A, B, C, D, E):
    if B > 70 and C > 60 and E > 80:
        return 1
    if B > 60 and C > 70:
        return 2
    if B < 30 and C > 55 and E > 55:
        return 2
    if B < 20 and C < 15:
        return 3
    if B > 70 and C < 50 and E < 30 and D > 70:
        return 3
    if B < 60 and C < 25 and E >= 50:
        return 4
    if B > 70 and C < 15 and D > 70 and E < 20:
        return 4
    if B > 30 and C < 40 and D > 60 and E < 20:
        return 4
    return 1
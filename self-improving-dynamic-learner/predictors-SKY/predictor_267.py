"""
Predictor 267
Generated on: 2025-09-09 14:52:29
Accuracy: 48.48%
"""


# PREDICTOR 267 - Accuracy: 48.48%
# Correct predictions: 4848/10000 (48.48%)

def predict_output(A, B, C, D, E):
    if A < 50 and B > 60 and C > 70:
        return 2
    if B > 80 and C < 40 and E > 60 and D > 50:
        return 4
    if B > 50 and C < 35 and E > 70:
        return 4
    if E >= 80 and B > 30:
        return 4
    if B < 20 and C < 15 and D > 70 and E > 50:
        return 1
    if B < 20 and C < 15:
        return 3
    if B < 20 and 30 < C < 60 and D > 80:
        return 1
    if B < 20 and 30 < C < 60:
        return 3
    if B + C < 40 and D > 45 and A < 30:
        return 4
    if B + C < 40:
        return 3
    if B < 30 and C < 30 and E < 40:
        return 3
    if B < 30 and C > 70:
        return 3
    if B > 60 and C < 50 and D > 70 and A > 80:
        return 3
    return 1
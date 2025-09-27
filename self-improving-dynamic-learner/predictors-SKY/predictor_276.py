"""
Predictor 276
Generated on: 2025-09-09 14:57:46
Accuracy: 55.15%
"""


# PREDICTOR 276 - Accuracy: 55.15%
# Correct predictions: 5515/10000 (55.15%)

def predict_output(A, B, C, D, E):
    if E >= 90:
        return 4
    if B > 85 and C < 35 and E > 60:
        return 4
    if C > 80 and B < 60 and E < 20:
        return 4
    if B < 20 and C > 20 and C < 25 and E < 20:
        return 4
    if B < 15 and C > 60 and D < 15 and E > 50:
        return 4
    if B > 50 and C > 60 and E < 5 and D > 60:
        return 4
    if A < 35 and 60 < B < 70 and C > 75 and E > 70:
        return 2
    if A < 40 and B > 75 and C > 50 and D > 60 and E > 60:
        return 2
    if B < 20 and C < 20 and E < 40:
        return 3
    return 1
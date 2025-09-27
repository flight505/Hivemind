"""
Predictor 24
Generated on: 2025-09-09 12:20:05
Accuracy: 51.13%
"""


# PREDICTOR 24 - Accuracy: 51.13%
# Correct predictions: 5113/10000 (51.13%)

def predict_output(A, B, C, D, E):
    if abs(E - C) > 50:
        return 4
    if B < 20 and C > 70 and E < 35 and D < 30:
        return 4
    if B > 30 and C < 30 and E < 10:
        return 4
    if B < 20 and C < 25 and E < 40:
        return 3
    if B > 40 and C < 25 and E < 50:
        return 3
    if B < 40 and C > 70 and E < 50:
        return 3
    if B > 60 and C < 25 and E < 20:
        return 3
    if 40 < B < 60 and 35 < C < 45 and 35 < E < 45:
        return 3
    if B > 60 and C > 70 and E > 60:
        return 2
    if A < 50 and B > 60 and C > 60 and E < 20:
        return 2
    if A + B > 160 and C < 40 and E < 45:
        return 2
    if B > 40 and E > 85 and C >= 30:
        return 2
    return 1
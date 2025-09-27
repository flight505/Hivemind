"""
Predictor 794
Generated on: 2025-09-09 20:55:06
Accuracy: 42.97%
"""


# PREDICTOR 794 - Accuracy: 42.97%
# Correct predictions: 4297/10000 (42.97%)

def predict_output(A, B, C, D, E):
    if B + C < 30:
        return 3
    if B < 20:
        return 4
    if C < 10 and E > 50:
        return 4
    if C > 70 and E < 20:
        return 4
    if B > 60 and C > 70 and E > 60:
        return 2
    if B > 80 and 40 < C < 60 and E > 30:
        return 2
    if B < 50 and C > 70:
        return 3
    if B > 70 and C < 50 and E < 25 and D > 80:
        return 3
    if E > 90 and B < 60 and C < 30:
        return 4
    if B > 80 and C < 30 and E > 60:
        return 4
    if 40 < B < 60 and 40 < C < 60 and 30 < E < 50:
        return 3
    return 1
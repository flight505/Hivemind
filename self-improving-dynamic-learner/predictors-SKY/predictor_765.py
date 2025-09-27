"""
Predictor 765
Generated on: 2025-09-09 20:31:24
Accuracy: 51.97%
"""


# PREDICTOR 765 - Accuracy: 51.97%
# Correct predictions: 5197/10000 (51.97%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if A < 40 and B > 60 and C > 70:
        return 2
    if B > 70 and C > 70 and D > 90:
        return 3
    if 40 < B < 60 and 40 < C < 50 and E < 30:
        return 3
    if B > 60 and C < 30:
        return 3
    if E > 90 and C < 30:
        return 4
    if B > 80 and C < 30 and E > 60:
        return 4
    if B < 20 and C > 70:
        return 1
    if C > 80 and E > 80 and B < 40:
        return 1
    if B > 80 and C > 90:
        return 2
    if B < 15 and C > 60 and E < 20:
        return 4
    if B > 50 and C > 90 and D < 20:
        return 4
    if D > 80 and B < 30 and C < 20:
        return 1
    if C > 85 and B > 60 and E > 40:
        return 1
    if B > 70 and C > 60 and E > 80:
        return 1
    return 1
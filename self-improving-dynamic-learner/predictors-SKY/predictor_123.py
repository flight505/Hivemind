"""
Predictor 123
Generated on: 2025-09-09 13:24:16
Accuracy: 49.15%
"""


# PREDICTOR 123 - Accuracy: 49.15%
# Correct predictions: 4915/10000 (49.15%)

def predict_output(A, B, C, D, E):
    if B > 70 and C > 70 and E > 80:
        return 1
    if B > 90 and C > 60:
        return 1
    if D > 95 and B > 80:
        return 3
    if A < 50 and B > 70 and C > 60:
        return 2
    if B > 90 and C < 40 and E > 50:
        return 2
    if B < 30 and C > 50 and E > 50:
        return 2
    if A < 30 and B > 60 and C > 70:
        return 2
    if C < 30 and E > 70:
        return 4
    if C > 85 and E > 90:
        return 4
    if B < 15 and C > 40 and E < 15:
        return 4
    if B < 10 and C < 20:
        return 3
    if C < 35 and E < 25 and B > 50:
        return 3
    if B > 60 and C < 25 and E < 20:
        return 3
    if B < 25 and C < 25 and E < 40:
        return 3
    if B > 40 and C < 30 and E < 30:
        return 3
    if B < 40 and C > 70 and E < 50:
        return 3
    return 1
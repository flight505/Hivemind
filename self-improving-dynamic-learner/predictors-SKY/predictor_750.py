"""
Predictor 750
Generated on: 2025-09-09 20:21:42
Accuracy: 57.85%
"""


# PREDICTOR 750 - Accuracy: 57.85%
# Correct predictions: 5785/10000 (57.85%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B > 80 and C > 70 and E < 30 and D > 30:
        return 4
    if A > 70 and B < 50 and C < 25 and D > 90 and E < 20:
        return 4
    if B < 30 and C > 50 and E < 20 and D < 30:
        return 4
    if B < 40 and C < 30 and E > 70:
        return 4
    if C > 90 and B < 40 and E < 20:
        return 4
    if C > 80 and B < 50 and D < 20:
        return 4
    if B > 60 and C < 30 and E > 60:
        return 4
    if B > 60 and C > 75 and E < 60:
        return 1
    if A < 10 and B > 60 and C > 75:
        return 1
    if B > 60 and C > 85 and E > 60:
        return 1
    if B > 90 and C > 50 and D > 20:
        return 2
    if B > 60 and C > 75:
        return 2
    return 1
"""
Predictor 764
Generated on: 2025-09-09 20:30:59
Accuracy: 45.43%
"""


# PREDICTOR 764 - Accuracy: 45.43%
# Correct predictions: 4543/10000 (45.43%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if A < 40 and B > 60 and C > 70 and E > 65:
        return 2
    if B > 70 and C > 70 and D > 90:
        return 3
    if B < 30 and C > 50 and E < 20:
        return 3
    if E > 90:
        return 4
    if B > 60 and C < 30 and E > 70:
        return 4
    if B < 50 and C > 50 and E > 40:
        return 4
    if D > 80 and B < 30 and C < 20:
        return 1
    if C > 85 and B > 60 and E > 40:
        return 1
    if B > 70 and C > 60 and E > 80:
        return 1
    return 1
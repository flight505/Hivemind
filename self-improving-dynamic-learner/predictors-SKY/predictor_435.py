"""
Predictor 435
Generated on: 2025-09-09 16:37:38
Accuracy: 45.62%
"""


# PREDICTOR 435 - Accuracy: 45.62%
# Correct predictions: 4562/10000 (45.62%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if E < 20 and B > 60 and C < 40 and A < 30:
        return 4
    if C > 55 and E < 50 and B > 50:
        return 4
    if B > 50 and C < 40 and E > 70:
        return 2
    if C > 90 and E < 20:
        return 4
    if E < 10 and B > 80 and D > 80:
        return 3
    if A > 80 and B < 15 and C < 30:
        return 3
    if B < 20 and C < 20:
        return 3
    if B > 60 and C > 70:
        return 2
    return 1
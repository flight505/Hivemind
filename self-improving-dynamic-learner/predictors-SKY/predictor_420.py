"""
Predictor 420
Generated on: 2025-09-09 16:26:39
Accuracy: 56.62%
"""


# PREDICTOR 420 - Accuracy: 56.62%
# Correct predictions: 5662/10000 (56.62%)

def predict_output(A, B, C, D, E):
    if E > 80 and C < 30:
        return 4
    if C > 75 and E < 20:
        return 4
    if B > 70 and D > 90:
        return 3
    if B > 70 and C > 65 and E < 30:
        return 3
    if B < 20 and C < 15:
        return 3
    if B > 60 and C > 60 and A < 40:
        return 2
    return 1
"""
Predictor 632
Generated on: 2025-09-09 18:58:07
Accuracy: 49.30%
"""


# PREDICTOR 632 - Accuracy: 49.30%
# Correct predictions: 4930/10000 (49.30%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if B > 80 and C < 30 and E > 60:
        return 4
    if C < 20 and E > 70:
        return 4
    if C > 65 and E < 50:
        return 4
    if E < 10 and D > 70:
        return 4
    if C > 75 and B > 60 and E >= 70:
        return 2
    if C < 5 or (C < 15 and B < 35):
        return 3
    return 1
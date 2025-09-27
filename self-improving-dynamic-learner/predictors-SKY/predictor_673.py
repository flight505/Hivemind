"""
Predictor 673
Generated on: 2025-09-09 19:25:03
Accuracy: 40.71%
"""


# PREDICTOR 673 - Accuracy: 40.71%
# Correct predictions: 4071/10000 (40.71%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B > 30 and C < 20:
        return 3
    if B < 20 and E > 60 and C < 50:
        return 2
    if B > 60 and C > 75 and E > 65:
        return 2
    if C > 60 and E < 30:
        return 3
    if B < 40 and C > 50 and E < 30:
        return 4
    if B > 50 and C > 80:
        return 4
    if E > 90:
        return 4
    return 1
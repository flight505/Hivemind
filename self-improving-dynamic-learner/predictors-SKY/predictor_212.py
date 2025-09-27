"""
Predictor 212
Generated on: 2025-09-09 14:16:49
Accuracy: 56.42%
"""


# PREDICTOR 212 - Accuracy: 56.42%
# Correct predictions: 5642/10000 (56.42%)

def predict_output(A, B, C, D, E):
    if E > 90 and B < 10:
        return 2
    if B > 60 and C >= 60 and E < 60:
        return 1
    if B < 20 and C < 20:
        return 3
    if B > 60 and C > 70 and E >= 70:
        return 2
    if A + B > 160 and C < 40 and E > 50:
        return 2
    if C < 30 and E > 80:
        return 4
    if B > 70 and C < 25 and E < 30:
        return 1
    if A > 90 and B > 60 and C < 40 and E < 30:
        return 1
    if B > 80 and C > 60 and E > 80:
        return 1
    return 1
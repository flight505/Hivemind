"""
Predictor 278
Generated on: 2025-09-09 14:59:27
Accuracy: 55.32%
"""


# PREDICTOR 278 - Accuracy: 55.32%
# Correct predictions: 5532/10000 (55.32%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if C < 25 and E > 90:
        return 4
    if B > 70 and C < 25 and A >= 10:
        return 4
    if B > 70 and C > 65 and D > 90:
        return 3
    if C < 30 and D > 80 and E > 80:
        return 3
    if B > 60 and C > 75 and E > 50:
        return 2
    return 1
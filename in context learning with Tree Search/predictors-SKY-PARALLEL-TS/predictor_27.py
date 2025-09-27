"""
Predictor 27
Generated on: 2025-09-09 23:19:12
Accuracy: 54.05%
"""


# PREDICTOR 27 - Accuracy: 54.05%
# Correct predictions: 5405/10000 (54.05%)

def predict_output(A, B, C, D, E):
    if C > 90 and D > 90:
        return 3
    if A < 5 and C < 10:
        return 3
    if B > 90:
        return 2
    if B < 10 and C > 90 and A < 60:
        return 2
    if A > 90 and E < 10:
        return 2
    if A < 10 and B > 70 and E < 20:
        return 4
    if C < 20 and D > 50:
        return 4
    if C > 70 and A < 20 and B < 30:
        return 4
    if B < 15 and E < 20:
        return 4
    if E > 80 and D < 40:
        return 4
    if A > 80 and B < 10:
        return 4
    else:
        return 1
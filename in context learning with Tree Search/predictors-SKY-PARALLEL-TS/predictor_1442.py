"""
Predictor 1442
Generated on: 2025-09-10 02:27:48
Accuracy: 54.05%
"""


# PREDICTOR 1442 - Accuracy: 54.05%
# Correct predictions: 5405/10000 (54.05%)

def predict_output(A, B, C, D, E):
    if B > 80 and C > 60 and A < 50:
        return 2
    if A < 20 and B > 60 and E < 30:
        return 4
    if B < 20 and C > 45:
        return 4
    if C < 20 and E > 80:
        return 4
    if A > 70 and B < 30 and C > 90:
        return 4
    if A > 90 and E > 80:
        return 4
    if A > 80 and B < 20 and D < 80:
        return 3
    else:
        return 1
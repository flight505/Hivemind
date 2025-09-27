"""
Predictor 769
Generated on: 2025-09-09 20:37:31
Accuracy: 47.05%
"""


# PREDICTOR 769 - Accuracy: 47.05%
# Correct predictions: 4705/10000 (47.05%)

def predict_output(A, B, C, D, E):
    if B < 5 and C < 20 and E < 40:
        return 3
    if B < 10 and C > 80:
        return 1
    if A > 85 and B < 20 and C < 15:
        return 1
    if E > 90 and B < 20 and C < 15:
        return 1
    if B < 20 and C < 15:
        return 3
    if B > 50 and C < 5:
        return 3
    if B > 40 and C > 35 and E < 30:
        return 3
    if B < 15 and C > 45:
        return 3
    if A < 50 and B > 60 and C > 70:
        return 2
    if E > 90 and B > 30:
        return 4
    else:
        return 1
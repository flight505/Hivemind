"""
Predictor 727
Generated on: 2025-09-09 20:05:08
Accuracy: 52.53%
"""


# PREDICTOR 727 - Accuracy: 52.53%
# Correct predictions: 5253/10000 (52.53%)

def predict_output(A, B, C, D, E):
    if C < 25 and E > 75:
        return 4
    if C > 80 and B < 40:
        return 4
    if B > 65 and C < 30 and A > 50:
        return 4
    if B < 20 and C < 15:
        return 3
    if C > 80 and 55 < B < 65 and E < 55:
        return 3
    if 40 < B < 55 and 40 < C < 50 and D < 10:
        return 3
    if D > 80 and E > 90 and B > 55 and C > 50:
        return 3
    if A < 40 and B > 60 and C > 30:
        return 2
    return 1
"""
Predictor 883
Generated on: 2025-09-09 21:43:58
Accuracy: 55.70%
"""


# PREDICTOR 883 - Accuracy: 55.70%
# Correct predictions: 5570/10000 (55.70%)

def predict_output(A, B, C, D, E):
    if D > 80 and B > 50 and E > 80 and C < 40:
        return 3
    if D > 80 and C < 15:
        return 3
    if B < 40 and C < 20 and E < 30 and D < 60:
        return 3
    if E > 90 and C < 40:
        return 4
    if B > 60 and C < 10 and E > 70:
        return 4
    if B < 40 and C > 80 and E < 25:
        return 4
    if A > 70 and B < 15 and E > 50:
        return 4
    if B > 80 and C < 30:
        return 4
    if A < 50 and B > 60 and C > 70:
        return 2
    if B > 80 and 35 <= C < 50:
        return 2
    if B < 20 and C > 70 and E > 60:
        return 2
    return 1
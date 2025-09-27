"""
Predictor 882
Generated on: 2025-09-09 21:43:15
Accuracy: 58.58%
"""


# PREDICTOR 882 - Accuracy: 58.58%
# Correct predictions: 5858/10000 (58.58%)

def predict_output(A, B, C, D, E):
    if E > 90 and C < 40:
        return 4
    if B > 90 and C < 50 and E > 50 and D < 50:
        return 4
    if B > 80 and C < 30:
        return 4
    if D > 90 and B > 80 and C >= 10:
        return 3
    if D > 90 and C < 10:
        return 3
    if B < 40 and C > 50 and E < 50 and D < 20:
        return 3
    if B < 25 and E < 15:
        return 3
    if B < 10 and C < 10:
        return 3
    if A < 50 and B > 60 and C > 70:
        return 2
    if A < 50 and B > 60 and C < 50 and E > 50 and D < 30:
        return 2
    return 1
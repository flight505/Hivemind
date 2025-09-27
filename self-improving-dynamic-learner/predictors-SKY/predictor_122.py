"""
Predictor 122
Generated on: 2025-09-09 13:23:53
Accuracy: 56.56%
"""


# PREDICTOR 122 - Accuracy: 56.56%
# Correct predictions: 5656/10000 (56.56%)

def predict_output(A, B, C, D, E):
    if A < 40 and B > 60 and C > 70 and E > 60:
        return 2
    if E > 80 and B > 60 and C > 40:
        return 2
    if C < 25 and E > 90:
        return 4
    if B <= 30 and C > 60 and E < 40:
        return 4
    if B < 35 and C < 15:
        return 3
    if D < 20 and A < 40 and B > 50 and C < 50 and E < 50:
        return 3
    if 40 < B < 50 and 40 < C < 50:
        return 3
    if A > 90 and abs(B - E) < 20 and C < 40:
        return 3
    if B > 80 and C > 60 and E > 70:
        return 1
    if B > 90:
        return 1
    if C > 55:
        return 1
    return 1
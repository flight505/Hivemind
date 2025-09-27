"""
Predictor 21
Generated on: 2025-09-09 12:17:41
Accuracy: 56.94%
"""


# PREDICTOR 21 - Accuracy: 56.94%
# Correct predictions: 5694/10000 (56.94%)

def predict_output(A, B, C, D, E):
    if C < 30 and E > 60:
        return 4
    if B < 20 and C > 70 and E < 50:
        return 4
    if C > 70 and E < 20:
        return 4
    if B > 70 and C < 35 and E > 50:
        return 4
    if B > 50 and C > 70 and E < 20:
        return 3
    if B > 40 and C < 30 and E > 40:
        return 3
    if B < 25 and C < 25:
        return 3
    if 40 < B < 60 and 35 < C < 55 and 35 < E < 55:
        return 3
    if B > 80 and C > 80 and E < 30:
        return 2
    if B > 60 and C > 70 and 65 < E < 80 and A < 40:
        return 2
    if B > 60 and C > 90:
        return 3
    return 1
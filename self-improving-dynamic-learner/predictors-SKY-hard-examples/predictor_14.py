"""
Predictor 14
Generated on: 2025-09-09 17:14:13
Accuracy: 56.83%
"""


# PREDICTOR 14 - Accuracy: 56.83%
# Correct predictions: 5683/10000 (56.83%)

def predict_output(A, B, C, D, E):
    if E > 85 and C < 30:
        return 4
    if C < 25 and D > 70 and E < 10:
        return 4
    if A < 25 and B > 65 and C > 40 and E > 40:
        return 4
    if B > 70 and D > 90 and C < 60:
        return 3
    if B < 20 and D > 90 and C < 35:
        return 3
    if B < 25 and C < 25:
        if E < 50:
            return 3
        else:
            return 1
    if B > 60 and C > 75 and A < 60:
        return 2
    if B > 80 and E > 70 and C < 70:
        return 2
    if B > 50 and C < 25 and E < 30 and D < 25:
        return 3
    if A < 10 and B < 35 and 25 < C < 45 and E < 20:
        return 4
    return 1
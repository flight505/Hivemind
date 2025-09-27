"""
Predictor 6
Generated on: 2025-09-09 12:07:06
Accuracy: 51.17%
"""


# PREDICTOR 6 - Accuracy: 51.17%
# Correct predictions: 5117/10000 (51.17%)

def predict_output(A, B, C, D, E):
    if B < 20:
        if E > 80 or C > 70:
            return 4
        elif E > 50:
            return 1
        else:
            return 3
    if E > 90 and C < 60:
        return 4
    if D >= 90 and C < 20 and B > 50:
        return 4
    if A < 15 and C > 65 and B < 35:
        return 4
    if E > 65 and C < 10 and B > 40:
        return 4
    if B > 50 and C < 45 and E > 60:
        return 3
    if B > 50 and C < 25 and E < 30 and A < 50:
        return 3
    if B > 50 and C > 45 and A < 55:
        return 2
    return 1
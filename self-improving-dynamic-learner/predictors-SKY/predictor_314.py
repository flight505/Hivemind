"""
Predictor 314
Generated on: 2025-09-09 15:23:21
Accuracy: 50.85%
"""


# PREDICTOR 314 - Accuracy: 50.85%
# Correct predictions: 5085/10000 (50.85%)

def predict_output(A, B, C, D, E):
    if C > 80 and B < 30:
        return 4
    if B > 80 and C < 20:
        return 4
    if B > 60 and C > 60:
        if A < 15 or A > 80:
            return 1
        else:
            return 2
    if E > 90:
        return 4
    if B > 90 and C > 25 and E >= 70:
        return 2
    if B < 20 and C < 20:
        if E > 70:
            return 4
        else:
            return 3
    if B < 15 and C > 25 and E < 50:
        return 4
    if C < 10 and B < 50:
        return 3
    if E > 80 and C < 45:
        return 4
    if B > 80 and C < 30 and E > 60:
        return 4
    if D > 90 and B < 25 and C < 25 and E < 30:
        return 1
    if C > 90 and E > 90 and B < 30:
        return 4
    if B > 70 and C < 25 and E < 30:
        return 1
    if B < 30 and C < 25 and E < 40:
        return 3
    if B > 60 and C < 25 and E < 20:
        return 3
    return 1
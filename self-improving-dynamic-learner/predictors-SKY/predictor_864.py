"""
Predictor 864
Generated on: 2025-09-09 21:34:31
Accuracy: 42.71%
"""


# PREDICTOR 864 - Accuracy: 42.71%
# Correct predictions: 4271/10000 (42.71%)

def predict_output(A, B, C, D, E):
    if C <= 20 and E > 70:
        if B > 20:
            return 4
        else:
            return 1
    if C <= 20 and E < 70 and B < 20:
        return 3
    if C <= 20 and E < 70:
        return 1
    if C > 90 and D > 90:
        return 1
    if B < 20 and C > 70:
        return 4
    if 30 < B < 50 and 30 < C < 50 and E < 20:
        return 4
    if 30 < B < 50 and 30 < C < 50:
        return 3
    if 50 < B < 60 and C < 50 and E < 30:
        return 3
    if B > 60 and C > 60 and D > 20:
        return 2
    if B > 80 and C > 40 and D > 20:
        return 2
    if B > 80 and C > 40:
        return 1
    if B + C > 120:
        return 2
    if B > 60 and C < 60 and E < 40:
        return 3
    if B > 50 and C < 40:
        return 1
    return 1
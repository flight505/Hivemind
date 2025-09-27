"""
Predictor 718
Generated on: 2025-09-09 19:58:48
Accuracy: 52.53%
"""


# PREDICTOR 718 - Accuracy: 52.53%
# Correct predictions: 5253/10000 (52.53%)

def predict_output(A, B, C, D, E):
    if E > 90 and C < 30:
        return 4
    if B > 90 and C > 90:
        return 2
    if B > 70 and C > 90:
        return 1
    if B > 60 and C < 10 and E < 10:
        return 1
    if B > 60 and C < 20 and E < 10 and D < 40:
        return 1
    if B > 60 and C < 20 and E < 10:
        return 3
    if B < 60 and C < 30 and E > 60:
        if D < 20:
            return 1
        else:
            return 4
    if B < 40 and C < 20 and E > 50:
        if D > 80:
            return 1
        else:
            return 4
    if C > 70 and E > 90:
        return 2
    if B > 90 and C < 40 and E < 5:
        return 3
    if D > 90 and E > 70 and C < 50:
        return 3
    if B < 30 and C > 50 and D > 80 and E < 20:
        return 1
    if B > 60 and C > 60:
        return 2
    if C < 20 and B < 30:
        return 3
    return 1
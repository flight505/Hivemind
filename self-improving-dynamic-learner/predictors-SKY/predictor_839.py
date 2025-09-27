"""
Predictor 839
Generated on: 2025-09-09 21:22:38
Accuracy: 47.89%
"""


# PREDICTOR 839 - Accuracy: 47.89%
# Correct predictions: 4789/10000 (47.89%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        if E < 50:
            return 3
        else:
            return 4
    if B < 20 and C < 30 and E > 80:
        return 4
    if B > 50 and C < 40 and E < 20:
        return 4
    if B < 30 and C > 50:
        return 4
    if B > 60 and 30 < C < 70 and D > 70:
        return 1
    if B > 60 and 30 < C < 70 and D < 30:
        return 1
    if A > 70 and B > 60 and C > 70:
        return 1
    if B > 60 and C > 70 and E < 20:
        if D > 80:
            return 1
        else:
            return 4
    if B > 60 and 30 < C < 70 and E < 10:
        return 3
    if B > 60 and C > 60 and D < 30:
        return 4
    if A > 80 and B > 60 and 30 < C < 70:
        return 1
    if B > 60 and C > 60 and D < 10:
        return 1
    if B > 60 and C > 70:
        return 2
    if B > 40 and C > 50 and D < 10:
        return 2
    if B > 60 and 30 < C < 70:
        return 2
    if E > 90 and C < 30:
        return 4
    return 1
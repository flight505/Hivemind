"""
Predictor 69
Generated on: 2025-09-09 12:51:33
Accuracy: 55.71%
"""


# PREDICTOR 69 - Accuracy: 55.71%
# Correct predictions: 5571/10000 (55.71%)

def predict_output(A, B, C, D, E):
    if C < 20 and E >= 50:
        return 4
    if C <= 25 and E > 60 and B < 60:
        return 4
    if B > 80 and E > 80 and C < 30:
        return 4
    if B < 20 and C > 70 and E < 35 and D < 30:
        return 4
    if B > 60 and C > 50 and E < 30:
        return 4
    if 40 < B < 50 and 25 < C < 35 and 40 < E < 50 and D > 50:
        return 4
    if C < 30 and E > 70 and B < 20 and D < 60:
        return 4
    if B > 60 and C < 25 and E < 20:
        return 3
    if B > 40 and C < 30 and E < 25:
        return 3
    if B < 25 and C < 25 and E < 40:
        return 3
    if B < 40 and C > 70 and E < 50 and D < 50:
        return 3
    if 40 < B < 50 and 35 < C < 45 and 35 < E < 45:
        return 3
    if 30 < B < 40 and C < 20 and E < 10:
        return 3
    if A > 80 and B > 60 and C < 30 and E < 60:
        return 3
    if A < 40 and B > 60 and C > 70 and 65 < E < 80:
        return 2
    if A < 50 and B > 60 and C > 60 and E < 20:
        return 2
    if B > 90 and 30 < C < 50:
        return 2
    if A + B > 160 and C < 40 and E < 45:
        return 2
    if B > 50 and 30 < C < 40 and E > 60:
        return 2
    if B < 30 and 35 < C < 45 and E > 50:
        return 2
    return 1
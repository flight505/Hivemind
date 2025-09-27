"""
Predictor 27
Generated on: 2025-09-09 12:21:24
Accuracy: 49.69%
"""


# PREDICTOR 27 - Accuracy: 49.69%
# Correct predictions: 4969/10000 (49.69%)

def predict_output(A, B, C, D, E):
    if (E - C) > 50:
        return 4
    if C > 60 and E > 80:
        return 4
    if C < 30 and E > 70:
        return 4
    if B > 80 and E > 80 and C < 50:
        return 4
    if B < 20 and C > 70 and E < 35 and D < 30:
        return 4
    if C > 50 and E < 10:
        return 4
    if B > 80 and C < 30 and E > 65:
        return 4
    if B > 80 and C < 30:
        return 2
    if B + C < 40 and E < 40:
        return 3
    if B < 40 and C > 70 and E < 50 and D < 50:
        return 3
    if 40 < B < 50 and 35 < C < 45 and 35 < E < 45:
        return 3
    if A < 40 and B > 60 and C > 70 and 65 < E < 80:
        return 2
    if A < 50 and B > 60 and C > 60 and E < 20:
        return 2
    if B > 90 and C < 50:
        return 2
    if A + B > 160 and C < 40 and E < 45:
        return 2
    if B > 60 and C < 35 and E > 45:
        return 2
    if B > 50 and C > 40 and E > 60:
        return 2
    if B > 70 and C > 50 and E > 60:
        return 2
    return 1
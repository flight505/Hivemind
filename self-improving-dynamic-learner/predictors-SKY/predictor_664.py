"""
Predictor 664
Generated on: 2025-09-09 19:19:42
Accuracy: 51.46%
"""


# PREDICTOR 664 - Accuracy: 51.46%
# Correct predictions: 5146/10000 (51.46%)

def predict_output(A, B, C, D, E):
    if E > 90:
        if B > 70:
            return 3
        if B < 30:
            return 1
        return 4
    if B < 20 and C < 20 and E < 40:
        if D > 50 and A < 70:
            return 1
        return 3
    if A < 50 and B > 60 and C >= 70 and E >= 70:
        return 2
    if B > 90 and 40 <= C < 60:
        return 2
    if B < 40 and C > 60 and E < 20:
        if D < 10:
            return 3
        return 4
    if B < 25 and C > 50:
        return 4
    if B < 35 and C > 35 and E < 35:
        return 4
    if B < 25 and C < 10 and E > 60:
        return 4
    if B > 80 and C < 30 and E > 60:
        return 4
    if D < 10 and E > 80:
        return 1
    if C > 85 and B > 60 and E > 40:
        return 1
    if B > 70 and C < 20:
        return 1
    return 1
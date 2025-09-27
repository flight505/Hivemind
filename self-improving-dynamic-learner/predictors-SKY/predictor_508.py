"""
Predictor 508
Generated on: 2025-09-09 17:27:55
Accuracy: 49.73%
"""


# PREDICTOR 508 - Accuracy: 49.73%
# Correct predictions: 4973/10000 (49.73%)

def predict_output(A, B, C, D, E):
    if B < 40 and E > 80:
        return 4
    if B > 60 and C < 30 and 50 < E < 80:
        return 4
    if C < 30 and E > 80:
        return 4
    if B < 30 and C < 20 and E > 60:
        return 4
    if C < 5 and E > 45:
        return 4
    if D > 90 and C < 20 and E < 10:
        return 4
    if B > 60 and C < 30 and E < 30:
        return 4
    if A < 40 and B > 45 and C > 45 and E > 70:
        return 2
    if B > 60 and C > 70:
        return 2
    if D > 80 and C < 20 and B > 50:
        return 3
    if B > 60 and D > 80 and C < 40 and E < 20:
        return 3
    if D > 80 and E > 80 and B > 60 and C < 40:
        return 3
    if B < 35 and C < 25:
        if D > 80 and E < 20:
            return 1
        else:
            return 3
    return 1
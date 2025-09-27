"""
Predictor 885
Generated on: 2025-09-09 21:44:47
Accuracy: 45.10%
"""


# PREDICTOR 885 - Accuracy: 45.10%
# Correct predictions: 4510/10000 (45.10%)

def predict_output(A, B, C, D, E):
    if B > 70 and C > 50 and E > 50:
        return 2
    if B > 70 and C > 50:
        return 4
    if C > 80 and B < 40:
        return 4
    if B > 70 and C < 20 and D < 50:
        return 1
    if B > 70 and C < 20:
        return 4
    if D > 90 and E < 20:
        if B < 30:
            return 3
        else:
            return 1
    if D > 90 and E > 80:
        return 3
    if A < 50 and B > 60 and C > 70:
        return 2
    if B > 90 and 30 <= C < 50:
        return 2
    if D > 80 and C < 15:
        return 3
    if B < 30 and C < 20 and E < 30:
        return 3
    return 1
"""
Predictor 674
Generated on: 2025-09-09 19:26:21
Accuracy: 54.10%
"""


# PREDICTOR 674 - Accuracy: 54.10%
# Correct predictions: 5410/10000 (54.10%)

def predict_output(A, B, C, D, E):
    if B < 30 and C < 25:
        if D > 80 and E < 20 and A > 30:
            return 1
        else:
            return 3
    if B > 80 and C < 10:
        return 4
    if B > 70 and C < 25:
        return 1
    if C > 80 and E < 30 and B < 60:
        return 4
    if B > 80 and C > 60 and D > 90:
        return 3
    if D > 90 and E < 20 and A > 50:
        return 3
    if C > 80 and B > 60:
        return 1
    if A < 35 and B > 60 and C > 70 and E >= 70:
        return 2
    if E > 90:
        return 4
    if D < 10 and E > 80:
        return 1
    if C > 85 and B > 60:
        return 1
    if B > 60 and C > 40 and E > 80 and D < 25:
        return 4
    return 1
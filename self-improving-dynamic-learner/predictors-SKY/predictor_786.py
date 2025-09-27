"""
Predictor 786
Generated on: 2025-09-09 20:49:43
Accuracy: 55.10%
"""


# PREDICTOR 786 - Accuracy: 55.10%
# Correct predictions: 5510/10000 (55.10%)

def predict_output(A, B, C, D, E):
    if B < 25 and C < 25:
        return 3
    if D > 80 and E >= 90:
        return 3
    if B > 50 and C < 35 and D > 80 and E > 70:
        return 3
    if C < 25 and E > 70:
        return 4
    if C < 35 and D > 80 and E < 20:
        return 3
    if E > 90:
        return 4
    if B > 80 and C > 40 and E < 20:
        return 2
    if B > 60 and C > 60:
        if A < 50:
            return 2
        else:
            return 1
    return 1
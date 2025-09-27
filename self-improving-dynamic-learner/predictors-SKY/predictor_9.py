"""
Predictor 9
Generated on: 2025-09-09 12:10:17
Accuracy: 54.00%
"""


# PREDICTOR 9 - Accuracy: 54.00%
# Correct predictions: 5400/10000 (54.00%)

def predict_output(A, B, C, D, E):
    if C > 70 and E < 30:
        if B > 50:
            return 4
        else:
            return 1
    if C < 25 and E > 70:
        if D > 80:
            return 3
        else:
            return 4
    if E > 90 and C < 30:
        return 4
    if B > 80 and C < 20 and E > 45:
        return 4
    if B > 60 and C > 90 and E < 50:
        return 3
    if B > 60 and C > 70 and E > 65:
        return 2
    if B > 80 and C > 45 and E < 45:
        return 2
    if B > 60 and C < 40 and E > 60:
        if D < 20:
            return 2
        else:
            return 3
    if B < 16 and C < 16:
        return 3
    return 1
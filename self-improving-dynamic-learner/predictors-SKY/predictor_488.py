"""
Predictor 488
Generated on: 2025-09-09 17:14:49
Accuracy: 59.38%
"""


# PREDICTOR 488 - Accuracy: 59.38%
# Correct predictions: 5938/10000 (59.38%)

def predict_output(A, B, C, D, E):
    if E > 75 and C < 20:
        return 4
    if B > 80 and C < 35 and E > 55:
        return 4
    if B < 20 and C < 20:
        if D > 90 and E > 90:
            return 1
        if E > 50:
            return 4
        else:
            return 3
    if C < 40 and D > 80 and E > 70:
        return 3
    if B < 50 and C < 50 and E < 30 and D < 60 and A < 80:
        return 3
    if E > 90 and C < 25:
        return 4
    if B > 90 and C > 70 and E < 10:
        return 1
    if C > 70 and E > 90:
        return 2
    if C > 80 and D < 10:
        return 3
    if D > 90 and C > 75 and E > 70:
        return 3
    if B > 60 and C > 60 and A < 40:
        return 2
    return 1
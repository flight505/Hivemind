"""
Predictor 838
Generated on: 2025-09-09 21:22:16
Accuracy: 51.79%
"""


# PREDICTOR 838 - Accuracy: 51.79%
# Correct predictions: 5179/10000 (51.79%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        if E < 50:
            return 3
        else:
            return 4
    if B < 30 and C < 40 and E > 90:
        return 4
    if A > 90 and E > 90:
        return 4
    if C > 80 and B < 30 and D < 20:
        return 4
    if B > 60 and C < 10 and D > 90:
        return 4
    if A > 80 and B > 60 and C > 70:
        return 1
    if B > 60 and C > 70 and E < 20 and D > 80:
        return 1
    if B > 60 and C > 70 and E < 20:
        return 4
    if B > 60 and C > 70:
        return 2
    if B > 40 and C > 50 and D < 10:
        return 2
    if B > 60 and 30 < C < 70:
        return 2
    if E > 90 and C < 30:
        return 4
    return 1
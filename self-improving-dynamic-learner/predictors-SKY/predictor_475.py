"""
Predictor 475
Generated on: 2025-09-09 17:04:42
Accuracy: 50.83%
"""


# PREDICTOR 475 - Accuracy: 50.83%
# Correct predictions: 5083/10000 (50.83%)

def predict_output(A, B, C, D, E):
    if B > 60 and C > 60:
        if A > 80:
            return 1
        else:
            return 2
    if B < 20 and C < 20:
        return 3
    if B > 60 and C < 40 and D > 90:
        return 3
    if C < 10 and D > 80 and B < 60:
        return 3
    if C < 30 and E > 70:
        return 4
    if B > 60 and C < 40 and D < 60:
        return 4
    if 40 < C < 55 and D < 40:
        return 4
    return 1
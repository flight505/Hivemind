"""
Predictor 20
Generated on: 2025-09-09 17:19:27
Accuracy: 39.47%
"""


# PREDICTOR 20 - Accuracy: 39.47%
# Correct predictions: 3947/10000 (39.47%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if C < 15 and D > 70:
        return 3
    if B < 20 and C > 30:
        if D < 10:
            return 3
        else:
            return 4
    if C < 25 and D > 90 and B > 50:
        return 4
    if B < 25 and E > 80:
        return 4
    if D > 70 and E > 90 and B < 40:
        return 3
    if E > 90:
        return 4
    if 20 < B < 30 and C > 70:
        return 4
    if B > 40 and C > 80:
        return 4
    if (B > 60 and C > 70) or (B > 50 and C > 50 and D < 10):
        return 2
    return 1
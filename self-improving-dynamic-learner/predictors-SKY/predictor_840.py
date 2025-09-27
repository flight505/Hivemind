"""
Predictor 840
Generated on: 2025-09-09 21:23:44
Accuracy: 55.28%
"""


# PREDICTOR 840 - Accuracy: 55.28%
# Correct predictions: 5528/10000 (55.28%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    if B > 60 and C >= 70:
        if C > 95 or E > 75:
            return 1
        else:
            return 2
    if E > 90 and C < 30:
        return 4
    if C < 5 and B > 20:
        if D > 50:
            return 4
        else:
            return 3
    if C < 10 and B > 20 and D < 50 and E > 70:
        return 4
    if B < 15 and C < 30 and E > 70:
        return 4
    if B > 80 and E > 90:
        return 4
    if B > 70 and C < 60 and E > 70:
        return 4
    return 1
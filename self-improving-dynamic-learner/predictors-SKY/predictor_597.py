"""
Predictor 597
Generated on: 2025-09-09 18:31:41
Accuracy: 47.43%
"""


# PREDICTOR 597 - Accuracy: 47.43%
# Correct predictions: 4743/10000 (47.43%)

def predict_output(A, B, C, D, E):
    if B > 90 and C >= 70 and D < 20:
        return 1
    if B > 90 and C >= 70:
        return 2
    if C >= 70 and E >= 70 and B > 60:
        return 2
    if C >= 70 and E >= 70:
        return 1
    if B < 30 and C < 30 and E < 20 and D > 80:
        return 1
    if B < 30 and C < 30:
        return 3
    if C < 30 and E > 70:
        return 4
    if D > 85 and B > 85 and C < 25:
        return 1
    if B > 60 and C < 25:
        return 4
    if B > 50 and D < 30 and E < 30:
        return 4
    if B > 70 and E < 20:
        return 4
    if B > 50 and D > 80 and E < 20:
        return 3
    if C > 80 and E < 30:
        return 2
    if C < 15 and E > 50:
        return 2
    if E > 60 and C > 40 and B < 25:
        return 2
    if (A + B) > 160 and C < 40 and E > 50:
        return 2
    return 1
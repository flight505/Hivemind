"""
Predictor 596
Generated on: 2025-09-09 18:30:34
Accuracy: 56.62%
"""


# PREDICTOR 596 - Accuracy: 56.62%
# Correct predictions: 5662/10000 (56.62%)

def predict_output(A, B, C, D, E):
    if C < 20 and E > 90:
        return 4
    if B < 30 and C < 30:
        return 3
    if C > 70 and E > 70 and B > 60:
        return 2
    if C > 70 and E > 70:
        return 1
    if E > 80 and D < 10:
        return 2
    if B < 25 and C > 45 and E < 20:
        return 4
    if B < 20 and C < 25 and E < 25:
        return 3
    if C < 25 and (B + D) < 50:
        return 3
    if B > 85 and C < 25:
        return 1
    if C > 55 and B > 60 and D > 80:
        return 1
    if E < 15 and C > 70 and B < 35:
        return 1
    if B < 40 and C < 25 and E > 80:
        return 4
    if (A + B) > 150 and C < 40:
        return 2
    if D > 90 and B < 30 and C < 25:
        return 1
    if B > 90 and C > 70:
        return 1
    if C < 30 and E > 70:
        return 4
    return 1
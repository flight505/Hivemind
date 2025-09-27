"""
Predictor 595
Generated on: 2025-09-09 18:30:10
Accuracy: 48.28%
"""


# PREDICTOR 595 - Accuracy: 48.28%
# Correct predictions: 4828/10000 (48.28%)

def predict_output(A, B, C, D, E):
    if C < 15 and B < 65:
        return 3
    if C > 75 and E > 65:
        return 2
    if C > 75 and E < 30:
        return 4
    if D < 5 and E > 70:
        return 4
    if B < 30 and C > 50 and E < 30:
        return 4
    if B > 70 and C < 40 and E > 80 and D > 70:
        return 2
    if 60 < B < 75 and C < 30 and E > 70 and D < 50:
        return 1
    if C < 40 and E >= 70 and (B + D > 50):
        return 4
    if B < 30 and 35 < C < 55 and E > 60:
        return 2
    return 1
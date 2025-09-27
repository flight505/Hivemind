"""
Predictor 631
Generated on: 2025-09-09 18:57:06
Accuracy: 46.19%
"""


# PREDICTOR 631 - Accuracy: 46.19%
# Correct predictions: 4619/10000 (46.19%)

def predict_output(A, B, C, D, E):
    if B < 20 and E > 90:
        return 1
    if C < 10 and D > 90:
        return 3
    if B > 60 and C > 75:
        return 2
    if B > 80 and E > 80:
        return 2
    if E > 90:
        return 4
    if B > 90 and C > 40 and E < 30:
        return 4
    if B < 25 and C > 60:
        return 4
    if B > 60 and 50 < C < 60 and D > 90 and E > 70:
        return 3
    if B + C < 30:
        return 3
    if B < 20 and C < 40 and (E < 60 or D < 50):
        return 3
    return 1
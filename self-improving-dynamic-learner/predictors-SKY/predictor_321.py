"""
Predictor 321
Generated on: 2025-09-09 15:27:38
Accuracy: 46.71%
"""


# PREDICTOR 321 - Accuracy: 46.71%
# Correct predictions: 4671/10000 (46.71%)

def predict_output(A, B, C, D, E):
    if B > 60 and C > 70 and E < 80:
        return 2
    if C < 25 and E > 70:
        return 4
    if B < 20 and C < 20:
        return 3
    if B < 20 and C > 50:
        return 4
    if B > 80 and C > 40 and E < 60:
        return 2
    if B > 60 and 50 < C < 60 and E > 90:
        return 3
    if C < 15 and B > 50:
        return 3
    if A > 50 and C < 40 and B > 50:
        return 3
    if E < 10:
        return 4
    return 1
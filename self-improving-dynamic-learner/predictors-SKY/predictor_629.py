"""
Predictor 629
Generated on: 2025-09-09 18:54:27
Accuracy: 50.31%
"""


# PREDICTOR 629 - Accuracy: 50.31%
# Correct predictions: 5031/10000 (50.31%)

def predict_output(A, B, C, D, E):
    if C > 80 and E > 90:
        return 1
    if B > 30 and C > 70 and E >= 70:
        return 2
    if B < 30 and C > 60 and E >= 70:
        return 4
    if B > 50 and C < 30 and E > 60:
        return 4
    if B < 30 and C < 30 and E > 50:
        return 4
    if E > 90:
        return 4
    if B < 50 and C > 70 and E < 60:
        return 3
    if A > 20 and B > 60 and C < 40 and D > 80 and E < 70:
        return 3
    if B + C < 30:
        return 3
    return 1
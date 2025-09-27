"""
Predictor 343
Generated on: 2025-09-09 15:38:33
Accuracy: 52.88%
"""


# PREDICTOR 343 - Accuracy: 52.88%
# Correct predictions: 5288/10000 (52.88%)

def predict_output(A, B, C, D, E):
    if D >= 90 and E > 90:
        return 1
    if E > 90:
        return 4
    if B > 80 and C > 80 and D > 80 and E < 20:
        return 3
    if B > 60 and C > 75 and E > 60:
        return 2
    if B < 20 and C < 15:
        return 3
    if B < 40 and C < 35 and D > 90 and E > 20:
        return 3
    if C > 75 and 40 < B < 60:
        return 4
    if B > 70 and C < 20 and E > 70:
        return 4
    if C < 25 and E > 30 and 30 < B < 75:
        return 4
    return 1
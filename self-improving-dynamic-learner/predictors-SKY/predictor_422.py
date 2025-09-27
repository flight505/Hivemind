"""
Predictor 422
Generated on: 2025-09-09 16:27:52
Accuracy: 48.28%
"""


# PREDICTOR 422 - Accuracy: 48.28%
# Correct predictions: 4828/10000 (48.28%)

def predict_output(A, B, C, D, E):
    if C < 10 and D > 80:
        return 4
    if E < 15 and D > 50:
        return 4
    if B < 20 and C < 10 and D > 80 and E > 50:
        return 4
    if B < 40 and C < 5:
        return 4
    if B > 50 and C > 50 and E < 30:
        return 4
    if B > 60 and C < 25 and E < 20:
        return 3
    if B < 30 and C < 40 and E < 30:
        return 3
    if B < 25 and C < 25 and E < 40:
        return 3
    if B > 80 and C < 40 and E < 30:
        return 2
    if B > 60 and C > 70:
        return 2
    if B > 60 and C > 85 and E > 60:
        return 1
    if B > 70 and C > 65 and E > 70:
        return 1
    if B > 90 and C > 60:
        return 1
    return 1
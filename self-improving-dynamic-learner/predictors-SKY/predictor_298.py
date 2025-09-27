"""
Predictor 298
Generated on: 2025-09-09 15:13:27
Accuracy: 46.34%
"""


# PREDICTOR 298 - Accuracy: 46.34%
# Correct predictions: 4634/10000 (46.34%)

def predict_output(A, B, C, D, E):
    if E >= 90:
        return 4
    if B > 80 and C < 40 and E > 60:
        return 4
    if B > 80 and C < 15 and E > 40:
        return 4
    if B < 20 and C > 50:
        return 4
    if C > 70 and E < 20:
        return 4
    if D > 60 and E < 10:
        return 4
    if B < 20 and 15 < C < 25 and E < 20 and D > 40:
        return 4
    if B > 60 and C > 75:
        return 2
    if B > 60 and C > 55 and A < 50:
        return 2
    if B < 20 and C < 20 and E < 40:
        return 3
    return 1
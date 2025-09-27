"""
Predictor 772
Generated on: 2025-09-09 20:40:50
Accuracy: 51.86%
"""


# PREDICTOR 772 - Accuracy: 51.86%
# Correct predictions: 5186/10000 (51.86%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    if E >= 80 and C < 30:
        return 4
    if C > 80 and E < 30:
        return 1
    if B > 60 and C > 80 and E > 80:
        return 1
    if 55 < B < 70 and C > 80 and E > 70:
        return 1
    if A > 90 and B < 10 and C < 30:
        return 4
    if B > 90 and C < 5:
        return 4
    if B < 60 and C < 30 and D > 70 and E > 30:
        return 4
    if C > 80 and E < 20:
        return 4
    if B > 80 and 30 <= C < 55 and E < 10:
        return 1
    if B > 80 and C < 40 and E < 30:
        return 1
    if 50 < B <= 65 and C >= 60 and D < 10:
        return 2
    if B > 80 and C > 75:
        return 2
    if B < 65 and C > 50 and D > 80:
        return 3
    if B > 80 and 30 < C < 55:
        return 2
    return 1
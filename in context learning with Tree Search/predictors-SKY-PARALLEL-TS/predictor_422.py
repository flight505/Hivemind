"""
Predictor 422
Generated on: 2025-09-10 00:02:23
Accuracy: 50.21%
"""


# PREDICTOR 422 - Accuracy: 50.21%
# Correct predictions: 5021/10000 (50.21%)

def predict_output(A, B, C, D, E):
    if A < 10 and B > 70 and E < 25:
        return 4
    if C < 15 and D > 70 and E > 70:
        return 4
    if C < 15 and D > 70 and 50 < E <= 70 and B > 50:
        return 2
    if B < 20 and C > 40:
        return 4
    if A > 60 and B < 20 and E < 20:
        return 4
    if D < 10 and E > 30:
        return 4
    if C > 80 and D < 20 and E > 80:
        return 4
    if D > 90 and E > 90 and C < 25:
        return 3
    if C > 70 and B < 10 and E < 10:
        return 3
    if A > 80 and C < 30 and D > 80:
        return 3
    else:
        return 1
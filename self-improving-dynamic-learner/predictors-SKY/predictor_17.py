"""
Predictor 17
Generated on: 2025-09-09 12:15:40
Accuracy: 53.61%
"""


# PREDICTOR 17 - Accuracy: 53.61%
# Correct predictions: 5361/10000 (53.61%)

def predict_output(A, B, C, D, E):
    if C < 25 and E > 70 and B < 50:
        return 4
    if C < 10 and E > 40:
        return 4
    if B > 80 and E > 80 and C < 50:
        return 4
    if B < 10 and C > 70 and E < 50:
        return 4
    if B > 70 and C < 25 and E > 70:
        return 2
    if B < 20 and C < 20:
        return 3
    if 40 < B < 50 and 35 < C < 45 and 35 < E < 45:
        return 3
    if B > 60 and C > 70 and E < 50:
        return 2
    if B > 60 and C > 90:
        return 3
    if B < 30 and C < 25 and E < 25:
        return 3
    if B > 40 and C < 30 and E > 45:
        return 3
    if B > 80 and C > 40 and E < 40:
        return 2
    if A + B > 150 and C > 40 and E > 70:
        return 2
    return 1
"""
Predictor 738
Generated on: 2025-09-09 20:13:49
Accuracy: 49.31%
"""


# PREDICTOR 738 - Accuracy: 49.31%
# Correct predictions: 4931/10000 (49.31%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    if C > 90 and E < 20:
        return 4
    if C > 80 and B < 50 and E < 50:
        return 4
    if E >= 70 and C < 30 and B < 40:
        return 4
    if B > 60 and C < 30 and E > 50 and D < 70:
        return 4
    if B > 60 and C > 75:
        return 2
    if B > 80 and 30 < C < 60 and E > 40:
        return 2
    if C > 70 and B < 60 and E < 60:
        return 3
    if E > 80 and B >= 55 and C < 60:
        return 3
    if B + C < 100 and D < 20:
        return 3
    return 1
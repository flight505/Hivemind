"""
Predictor 793
Generated on: 2025-09-09 20:54:07
Accuracy: 50.56%
"""


# PREDICTOR 793 - Accuracy: 50.56%
# Correct predictions: 5056/10000 (50.56%)

def predict_output(A, B, C, D, E):
    if B + C < 30:
        return 3
    if B < 15 and E > 75:
        return 4
    if C > 95 and E < 20:
        return 4
    if C > 85 and B < 40 and E < 40:
        return 4
    if B > 65 and C < 30 and E > 60:
        return 4
    if E > 90 and B < 50 and C < 30:
        return 4
    if B > 60 and C > 75:
        return 2
    if B > 80 and 35 < C < 55 and E < 55:
        return 2
    if C > 80 and B > 50:
        return 3
    if 40 < B < 55 and 40 < C < 50 and 30 < E < 45:
        return 3
    if B >= 60 and 50 < C < 60 and E > 90:
        return 3
    return 1
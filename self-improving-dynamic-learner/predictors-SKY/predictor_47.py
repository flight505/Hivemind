"""
Predictor 47
Generated on: 2025-09-09 12:36:11
Accuracy: 51.44%
"""


# PREDICTOR 47 - Accuracy: 51.44%
# Correct predictions: 5144/10000 (51.44%)

def predict_output(A, B, C, D, E):
    if B > 75 and E > 85 and C < 60:
        return 4
    if C < 5 and B > 80:
        return 4
    if B > 60 and C < 35 and E < 25:
        return 4
    if A > 10 and C < 30 and E > 40:
        return 4
    if C < 20 and E >= 50:
        return 4
    if B < 20 and C > 70 and E < 35 and D < 30:
        return 4
    if C > 75 and B > 60:
        return 2
    if A < 25 and C > 30 and E > 55:
        return 2
    if A < 40 and B > 60 and C > 70 and 65 < E < 80:
        return 2
    if A < 50 and B > 60 and C > 60 and E < 20:
        return 2
    if B < 20 and C < 20:
        return 3
    if B > 70 and C > 55 and E > 70 and A < 50:
        return 3
    if B > 40 and C < 30 and E < 30:
        return 3
    if B < 25 and C < 25 and E < 40:
        return 3
    if 40 < B < 50 and 35 < C < 45 and 35 < E < 45:
        return 3
    return 1
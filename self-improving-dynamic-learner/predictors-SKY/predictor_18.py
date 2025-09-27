"""
Predictor 18
Generated on: 2025-09-09 12:16:11
Accuracy: 53.56%
"""


# PREDICTOR 18 - Accuracy: 53.56%
# Correct predictions: 5356/10000 (53.56%)

def predict_output(A, B, C, D, E):
    if C < 25 and E > 70:
        return 4
    if B < 15 and C > 90 and E < 50:
        return 4
    if C < 20 and D > 90 and B > 60 and E < 30:
        return 4
    if B < 10 and E < 20 and D > 60:
        return 4
    if E < 15 and C > 40:
        return 4
    if B > 50 and C > 80 and E > 70 and D < 20:
        return 4
    if B < 50 and C > 80 and E > 70 and D < 20:
        return 2
    if B > 80 and C > 40 and E > 80:
        return 2
    if B > 80 and 40 < C < 70:
        return 2
    if B > 80 and C < 40 and E < 50:
        return 2
    if A < 40 and B > 60 and C > 70 and 65 < E < 80:
        return 2
    if B < 20 and C < 20:
        return 3
    if 40 < B < 50 and 35 < C < 45 and 35 < E < 45:
        return 3
    if B > 60 and C > 90:
        return 3
    return 1
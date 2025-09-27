"""
Predictor 19
Generated on: 2025-09-09 12:17:11
Accuracy: 50.64%
"""


# PREDICTOR 19 - Accuracy: 50.64%
# Correct predictions: 5064/10000 (50.64%)

def predict_output(A, B, C, D, E):
    if 20 < B < 50 and E < 20 and C > 30:
        return 3
    if (E > 90 and C < 30) or (C < 25 and E > 70):
        return 4
    if C < 10 and (E > 40 or B > 90):
        return 4
    if C > 75 and E < 30 and D < 20 and B < 20:
        return 4
    if E < 30 and C > 40 and B < 50:
        return 4
    if B < 10 and C > 40:
        return 4
    if B > 80 and C < 30 and D < 70:
        return 4
    if B > 80 and E < 30 and C > 40:
        return 4
    if E < 15 and C > 40:
        return 4
    if B < 20 and C < 20:
        return 3
    if 40 < B < 50 and 35 < C < 45 and 35 < E < 45:
        return 3
    if B > 60 and C > 90 and E < 50:
        return 3
    if B > 60 and C > 70 and 65 < E < 80 and A < 40:
        return 2
    if B > 70 and C < 60 and D < 80:
        return 2
    return 1
"""
Predictor 16
Generated on: 2025-09-09 12:15:24
Accuracy: 57.26%
"""


# PREDICTOR 16 - Accuracy: 57.26%
# Correct predictions: 5726/10000 (57.26%)

def predict_output(A, B, C, D, E):
    if (E > 90 and C < 30) or (C < 25 and E > 70):
        return 4
    if C < 10 and (E > 40 or B > 90):
        return 4
    if C > 75 and E < 30 and D < 20:
        return 4
    if B < 20 and C > 65 and E < 50 and A < 20:
        return 3
    if B < 20 and C > 65 and E < 50:
        return 4
    if B > 20 and C > 60 and E < 20:
        return 4
    if B > 80 and E > 80 and D < 20:
        return 4
    if B > 80 and E > 80:
        return 2
    if B < 20 and C < 20:
        return 3
    if 40 < B < 50 and 35 < C < 45 and 35 < E < 45:
        return 3
    if B > 60 and C > 70 and 65 < E < 80 and A < 40:
        return 2
    if B > 60 and C > 90:
        return 3
    if 20 < B < 40 and C < 15 and E < 20:
        return 3
    return 1
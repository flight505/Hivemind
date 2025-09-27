"""
Predictor 2
Generated on: 2025-09-09 17:02:10
Accuracy: 39.41%
"""


# PREDICTOR 2 - Accuracy: 39.41%
# Correct predictions: 3941/10000 (39.41%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if C >= 75:
        if A > 60:
            return 1
        else:
            return 2
    if D < 10:
        return 3
    if A < 20 and D > 50 and B < 60:
        return 4
    if B >= 60 and E >= 70 and C <= 60:
        return 2
    if B >= 50 and E < 40 and C <= 50:
        return 2
    if B >= 60 and E >= 70 and A < 20:
        return 4
    if B < 30 and C > 30 and D < 50:
        return 4
    if B < 20:
        if C > 60:
            return 1
        if B < 10 and E > 50:
            return 4
        if E > 40:
            return 2
        return 3
    return 1
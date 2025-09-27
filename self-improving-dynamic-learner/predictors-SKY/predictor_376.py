"""
Predictor 376
Generated on: 2025-09-09 16:00:06
Accuracy: 54.91%
"""


# PREDICTOR 376 - Accuracy: 54.91%
# Correct predictions: 5491/10000 (54.91%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        if E < 40:
            return 3
        else:
            return 4
    if C > 70 and E < 20:
        return 4
    if B > 80 and C < 40 and E > 80:
        return 4
    if B > 60 and D < 20 and (C < 60 or E < 60):
        return 4
    if C < 25 and E > 90:
        return 4
    if C > 70 and E >= 70 and B >= 60 and A < 50:
        return 2
    if A > 90 and B > 80 and C < 40 and E > 60:
        return 2
    if B > 50 and C < 40 and E < 20 and D > 70:
        return 3
    if C < 20 and E < 30 and B < 50 and D < 30:
        return 3
    return 1
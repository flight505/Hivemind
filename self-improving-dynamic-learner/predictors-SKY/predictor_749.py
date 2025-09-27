"""
Predictor 749
Generated on: 2025-09-09 20:20:38
Accuracy: 49.55%
"""


# PREDICTOR 749 - Accuracy: 49.55%
# Correct predictions: 4955/10000 (49.55%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if C > 80 and B > 50 and E < 60 and D > 70:
        return 3
    if 40 < B < 60 and 40 < C < 60 and E < 40:
        return 3
    if E > 80 and B > 50 and C < 60:
        return 3
    if B > 60 and C > 70:
        return 2
    if B > 80 and C > 30 and E < 60:
        return 2
    if B < 40 and C < 30 and E > 70:
        return 4
    if C > 90 and B < 40 and E < 20:
        return 4
    if C > 80 and B < 50 and D < 20:
        return 4
    if B > 60 and C < 30 and E > 60:
        return 4
    return 1
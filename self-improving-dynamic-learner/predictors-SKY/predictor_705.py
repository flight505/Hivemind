"""
Predictor 705
Generated on: 2025-09-09 19:49:48
Accuracy: 57.84%
"""


# PREDICTOR 705 - Accuracy: 57.84%
# Correct predictions: 5784/10000 (57.84%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if A < 40 and B >= 65 and C > 25:
        return 2
    if C > 80 and B > 50 and D > 70 and E > 40:
        return 3
    if A < 10 and B > 40 and C > 40 and D < 10 and E > 30:
        return 3
    if B >= 60 and C > 50 and D > 80 and E > 90:
        return 3
    if C < 30 and E > 60:
        return 4
    if C > 85 and ((E < 20 and B < 50) or D < 20):
        return 4
    return 1
"""
Predictor 861
Generated on: 2025-09-09 21:32:37
Accuracy: 48.60%
"""


# PREDICTOR 861 - Accuracy: 48.60%
# Correct predictions: 4860/10000 (48.60%)

def predict_output(A, B, C, D, E):
    if B > 80 and C < 30 and E < 50:
        return 4
    if C < 25 and E > 90:
        return 4
    if C > 80 and E < 25:
        return 4
    if B > 50 and C > 50 and D < 40:
        return 4
    if B > 70 and C < 30 and E > 60:
        return 2
    if B > 80 and C > 60:
        return 2
    if B > 70 and C < 30 and 30 < E < 60:
        return 3
    if B > 70 and C > 80 and E < 30:
        return 3
    if B < 25 and C < 15:
        return 3
    if B > 60 and C > 70:
        return 2
    if C <= 20 and E > 70:
        return 4
    return 1
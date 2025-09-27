"""
Predictor 210
Generated on: 2025-09-09 14:15:51
Accuracy: 57.97%
"""


# PREDICTOR 210 - Accuracy: 57.97%
# Correct predictions: 5797/10000 (57.97%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15 and E < 40:
        return 3
    if A < 40 and B > 60 and C > 65 and E > 65:
        return 2
    if A < 10 and B > 70 and C > 50 and E < 45:
        return 4
    if B < 40 and C > 50 and E < 20:
        return 4
    if B < 30 and C > 30 and 40 < E < 60:
        return 4
    if B < 30 and C > 70 and E > 90:
        return 4
    if C < 30 and E > 60:
        return 4
    if E > 90 and B > 60 and C > 45:
        return 4
    if B > 80 and C < 10 and E < 10:
        return 4
    return 1
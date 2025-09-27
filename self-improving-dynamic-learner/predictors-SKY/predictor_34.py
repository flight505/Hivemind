"""
Predictor 34
Generated on: 2025-09-09 12:26:17
Accuracy: 49.16%
"""


# PREDICTOR 34 - Accuracy: 49.16%
# Correct predictions: 4916/10000 (49.16%)

def predict_output(A, B, C, D, E):
    if A < 5 and C < 20 and E > 90:
        return 2
    if (C < 30 and C > 18 and E > 65 and D > 10) or (B < 20 and C > 70 and E > 50) or (B < 20 and E < 20 and D > 50):
        return 4
    if B < 20:
        return 3
    if C > 80 and E < 10:
        return 3
    if B > 60 and C > 60 and A < 50:
        return 2
    if B > 80 and E > 90 and C > 40:
        return 2
    return 1
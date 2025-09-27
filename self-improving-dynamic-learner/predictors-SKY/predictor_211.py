"""
Predictor 211
Generated on: 2025-09-09 14:16:05
Accuracy: 21.74%
"""


# PREDICTOR 211 - Accuracy: 21.74%
# Correct predictions: 2174/10000 (21.74%)

def predict_output(A, B, C, D, E):
    if B < 50 and C < 55 and E < 90:
        return 3
    if B > 60 and C > 45 and E < 50:
        return 3
    if C < 15 and B < 40 and E > 50:
        return 4
    if A > 90 and B < 15 and C < 20 and E > 50:
        return 4
    if B < 20 and C < 15 and E > 60:
        return 4
    if A < 50 and B > 60 and C > 70:
        return 2
    if B > 80 and C > 75 and E < 50:
        return 2
    if B > 70 and C < 30 and E > 80 and A > 60:
        return 1
    if B < 30 and C < 5 and E > 80 and A > 80:
        return 1
    if A + B > 150 and C < 30 and E > 80:
        return 1
    return 4
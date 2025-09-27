"""
Predictor 888
Generated on: 2025-09-09 21:45:47
Accuracy: 43.99%
"""


# PREDICTOR 888 - Accuracy: 43.99%
# Correct predictions: 4399/10000 (43.99%)

def predict_output(A, B, C, D, E):
    if C < 25 and E > 70:
        return 4
    if B > 90 and C < 50:
        return 1
    if D > 90 and E < 30:
        return 1
    if B > 60 and C > 70:
        return 2
    if B < 40 and D > 50:
        return 3
    if B > 80 and C > 40 and E < 30:
        return 1
    if A < 50 and B > 60 and C > 60:
        return 2
    if D > 80 and C < 20:
        return 3
    if B < 30 and C < 25 and E < 40:
        return 3
    return 1
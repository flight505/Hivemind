"""
Predictor 872
Generated on: 2025-09-09 21:39:16
Accuracy: 49.38%
"""


# PREDICTOR 872 - Accuracy: 49.38%
# Correct predictions: 4938/10000 (49.38%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B > 30 and B < 50 and C < 15:
        return 3
    if B > 60 and C < 30:
        return 4
    if E > 90:
        return 4
    if B < 40 and C > 80:
        return 4
    if B < 40 and C < 50 and E < 5 and D > 50:
        return 4
    if B > 70 and 40 < C < 50:
        return 2
    if B > 90 and C > 80:
        return 2
    if A < 40 and B > 60 and C > 70 and E > 70:
        return 2
    if B > 60 and C < 35 and D > 80 and E < 30:
        return 3
    return 1
"""
Predictor 887
Generated on: 2025-09-09 21:45:30
Accuracy: 48.32%
"""


# PREDICTOR 887 - Accuracy: 48.32%
# Correct predictions: 4832/10000 (48.32%)

def predict_output(A, B, C, D, E):
    if B < 20 and C > 80:
        return 4
    if E > 80 and C < 30:
        return 4
    if B < 20 and E > 70:
        return 4
    if B > 70 and D > 80 and C < 40 and E > 80:
        return 3
    if D > 90 and B > 70:
        return 3
    if B > 80 and C < 30:
        return 4
    if A < 50 and B > 60 and C > 60:
        return 2
    if B > 90 and 30 <= C < 50:
        return 2
    if D > 80 and C < 20:
        return 3
    if B < 30 and C < 25 and E < 40:
        return 3
    if B > 70 and C > 50:
        return 2
    return 1
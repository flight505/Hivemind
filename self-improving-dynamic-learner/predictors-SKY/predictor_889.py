"""
Predictor 889
Generated on: 2025-09-09 21:46:08
Accuracy: 57.13%
"""


# PREDICTOR 889 - Accuracy: 57.13%
# Correct predictions: 5713/10000 (57.13%)

def predict_output(A, B, C, D, E):
    if B < 20 and C > 80:
        return 2
    if B > 80 and C > 80 and D > 80 and E > 70:
        return 1
    if B > 60 and C < 25 and E > 70:
        return 4
    if B < 20 and C < 30 and D > 50 and E < 20:
        return 4
    if B > 70 and D > 90 and C < 40:
        return 3
    if A < 50 and B > 60 and C > 60:
        return 2
    if D > 80 and C < 20:
        return 3
    if B < 30 and C < 25 and E < 40:
        return 3
    if E > 90 and C < 40:
        return 4
    if B > 90 and 30 <= C < 50:
        return 2
    return 1
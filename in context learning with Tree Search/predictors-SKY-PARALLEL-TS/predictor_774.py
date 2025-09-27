"""
Predictor 774
Generated on: 2025-09-10 00:46:57
Accuracy: 52.21%
"""


# PREDICTOR 774 - Accuracy: 52.21%
# Correct predictions: 5221/10000 (52.21%)

def predict_output(A, B, C, D, E):
    if B > 90 and E < 5:
        return 3
    if D > 90 and E < 25 and B > 90:
        return 3
    if B < 10 and D > 80:
        return 3
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (40 < A < 50 and B > 40 and C < 35 and D < 25 and E > 50):
        return 4
    if A > 90 and E < 10:
        return 2
    if A >= 40 and C > 80 and B > 60 and E < 40:
        return 2
    else:
        return 1
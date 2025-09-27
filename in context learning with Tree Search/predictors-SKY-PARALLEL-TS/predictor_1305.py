"""
Predictor 1305
Generated on: 2025-09-10 02:02:09
Accuracy: 47.78%
"""


# PREDICTOR 1305 - Accuracy: 47.78%
# Correct predictions: 4778/10000 (47.78%)

def predict_output(A, B, C, D, E):
    if A < 10 and B > 70:
        return 4
    if C < 10 and D > 90:
        return 4
    if B > 70 and E > 80:
        return 4
    if C > 50 and D < 20 and E > 50:
        return 4
    if A > 80 and B < 20 and D < 20 and E > 60:
        return 4
    if B > 70 and C < 90:
        return 2
    if A > 50 and B < 10 and C < 20 and E < 10:
        return 3
    else:
        return 1
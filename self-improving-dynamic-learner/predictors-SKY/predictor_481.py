"""
Predictor 481
Generated on: 2025-09-09 17:10:17
Accuracy: 45.53%
"""


# PREDICTOR 481 - Accuracy: 45.53%
# Correct predictions: 4553/10000 (45.53%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if C > 70 and E < 20:
        return 4
    if A > 80 and B > 60 and C > 60:
        return 1
    if B > 60 and C > 50:
        return 2
    if C < 20 and (B > 50 or B < 25):
        return 3
    if A < 80 and B > 70 and E > 70:
        return 2
    return 1
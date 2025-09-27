"""
Predictor 666
Generated on: 2025-09-09 19:21:05
Accuracy: 57.47%
"""


# PREDICTOR 666 - Accuracy: 57.47%
# Correct predictions: 5747/10000 (57.47%)

def predict_output(A, B, C, D, E):
    if B > 90 and C >= 70 and D < 15:
        return 1
    if B > 90 and C > 90:
        return 2
    if B > 60 and C > 70 and E > 70:
        return 2
    if B < 20 and C < 20:
        return 3
    if C >= 70 and D < 20 and B < 60:
        return 3
    if (C < 25 or A > 90) and E > 70:
        return 4
    if D < 10 and E > 80:
        return 1
    if C > 85 and B > 60 and E > 40:
        return 1
    if B > 80 and C < 30 and E > 60:
        return 4
    return 1
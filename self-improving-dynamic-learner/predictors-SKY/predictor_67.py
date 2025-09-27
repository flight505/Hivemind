"""
Predictor 67
Generated on: 2025-09-09 12:50:04
Accuracy: 52.28%
"""


# PREDICTOR 67 - Accuracy: 52.28%
# Correct predictions: 5228/10000 (52.28%)

def predict_output(A, B, C, D, E):
    if B > 80 and C < 30 and E > 60:
        return 4
    if B < 20 and C > 70 and E > 50:
        return 4
    if C < 30 and E > 70 and B < 40 and 10 < D < 50:
        return 4
    if B < 20 and C < 50 and E < 50:
        return 3
    if C < 25 and B >= 20 and B < 40 and E < 50 and D < 50:
        return 3
    if B > 60 and C > 70 and E < 20:
        return 3
    if B > 60 and C > 70 and E > 60:
        return 2
    if B > 80 and E > 70 and C < 70:
        return 2
    if C < 30 and E > 70 and (D > 50 or B > 40):
        return 2
    return 1
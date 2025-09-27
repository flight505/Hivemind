"""
Predictor 895
Generated on: 2025-09-09 21:48:34
Accuracy: 55.93%
"""


# PREDICTOR 895 - Accuracy: 55.93%
# Correct predictions: 5593/10000 (55.93%)

def predict_output(A, B, C, D, E):
    if C > 85 and B > 60 and E > 40:
        return 1
    if B > 60 and C > 75:
        return 2
    if B > 80 and C > 40 and A > 90:
        return 2
    if E > 90:
        return 4
    if C <= 20 and E > 60:
        return 4
    if B > 70 and C < 50 and E > 60:
        return 4
    if B < 20 and C < 15:
        return 3
    if D < 80 and B < 30 and C < 15:
        return 3
    if 40 < B < 55 and C < 20 and E < 30:
        return 3
    if D > 80 and 50 < B < 80 and C < 50:
        return 3
    return 1
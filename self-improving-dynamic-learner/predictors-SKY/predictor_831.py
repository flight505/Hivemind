"""
Predictor 831
Generated on: 2025-09-09 21:19:12
Accuracy: 47.97%
"""


# PREDICTOR 831 - Accuracy: 47.97%
# Correct predictions: 4797/10000 (47.97%)

def predict_output(A, B, C, D, E):
    if B > 80 and C < 10:
        return 4
    if B > 80 and C < 30 and D < 50:
        return 2
    if B > 80 and C < 30 and D > 80:
        return 1
    if C < 35 and D > 50 and E > 40 and B < 50:
        return 4
    if B < 10 and C < 15 and D > 70 and 40 < E < 90:
        return 4
    if B < 10 and E > 90:
        return 1
    if C > 70 and E > 80:
        return 2
    if C > 90 and D > 90 and E > 80:
        return 3
    if B < 20 and C > 50 and E < 20:
        return 1
    if B > 50 and C > 70:
        return 2
    if C < 25 and E > 70:
        return 4
    if B < 20 and C < 15 and E < 40:
        return 3
    return 1
"""
Predictor 751
Generated on: 2025-09-09 20:21:59
Accuracy: 57.49%
"""


# PREDICTOR 751 - Accuracy: 57.49%
# Correct predictions: 5749/10000 (57.49%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if C > 80 and B > 30 and E < 10 and D < 20:
        return 3
    if B > 45 and B < 55 and C < 20 and D > 80 and E > 80:
        return 4
    if B < 35 and C > 40 and C < 50 and E < 20:
        return 3
    if B > 55 and C > 60 and D > 90 and E > 70:
        return 3
    if B < 50 and C < 50 and D < 10 and E > 80:
        return 4
    if B > 50 and C < 20 and D < 20 and E < 50:
        return 3
    if A > 90 and B > 90 and C < 70 and E < 30:
        return 1
    if B > 80 and C <= 30 and E > 60:
        return 4
    if B > 60 and C < 35 and E > 80:
        return 4
    if B < 50 and C < 20 and D > 70 and E > 65:
        return 4
    if B > 60 and C > 75 and E < 60:
        return 1
    if A < 10 and B > 60 and C > 75:
        return 1
    if B > 60 and C > 85 and E > 60:
        return 1
    if B > 90 and C > 50 and D > 20 and E > 30:
        return 2
    if B > 60 and C > 75:
        return 2
    return 1
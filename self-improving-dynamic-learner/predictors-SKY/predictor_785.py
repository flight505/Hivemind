"""
Predictor 785
Generated on: 2025-09-09 20:48:58
Accuracy: 49.88%
"""


# PREDICTOR 785 - Accuracy: 49.88%
# Correct predictions: 4988/10000 (49.88%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if C < 10 and D > 60 and E < 30:
        return 3
    if C < 10 and D > 60 and E > 65:
        return 4
    if B < 40 and C < 10 and E > 70:
        return 4
    if C < 20 and E > 75:
        return 4
    if B < 20 and C > 50:
        return 4
    if B > 80 and C > 75 and D < 15 and E > 90:
        return 4
    if B > 80 and C > 80 and E < 30:
        return 1
    if B > 70 and C > 90 and D > 80 and E > 70:
        return 3
    if B > 80 and C > 85 and D < 5:
        return 1
    if B > 60 and C > 60 and D < 20:
        return 1
    if B > 60 and C > 60:
        return 2
    return 1
"""
Predictor 865
Generated on: 2025-09-09 21:35:08
Accuracy: 43.08%
"""


# PREDICTOR 865 - Accuracy: 43.08%
# Correct predictions: 4308/10000 (43.08%)

def predict_output(A, B, C, D, E):
    if B < 25 and C < 40 and E < 30 and D > 40:
        return 4
    if B > 90 and C > 40 and E < 25:
        return 4
    if B > 80 and C > 80 and D < 30 and E > 80:
        return 1
    if B > 70 and C < 25 and E > 70:
        return 1
    if B < 20 and C > 40 and D > 60 and E > 50:
        return 3
    if B < 20 and C > 40 and E > 60:
        return 2
    if B < 30 and C > 50 and E > 60:
        return 2
    if B < 20 and C < 25:
        return 3
    if C < 25 and E > 80:
        return 4
    if B > 60 and C > 60:
        return 2
    if B > 60 and C < 40:
        return 1
    if B < 30 and C < 40 and E < 30:
        return 3
    if B + C > 150:
        return 1
    if D > 80 and E < 30:
        return 1
    if C > 70 and E < 30 and B < 40:
        return 3
    return 1
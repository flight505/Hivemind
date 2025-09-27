"""
Predictor 573
Generated on: 2025-09-09 18:15:46
Accuracy: 50.81%
"""


# PREDICTOR 573 - Accuracy: 50.81%
# Correct predictions: 5081/10000 (50.81%)

def predict_output(A, B, C, D, E):
    if B > 80 and E > 80 and C < 50 and D < 50:
        return 4
    if C < 25 and E >= 70 and B < 60 and D > 20:
        return 4
    if B < 20 and E > 70:
        return 4
    if C > 70 and E < 30:
        return 4
    if B < 20 and C > 50 and E < 20:
        return 4
    if B <= 60 and C < 15:
        return 3
    if B > 60 and C > 70 and E >= 70:
        return 2
    if A < 10 and E > 60:
        return 2
    if B > 70 and E > 80 and C < 40:
        return 2
    if C > 70 and E > 70 and B < 30:
        return 2
    return 1
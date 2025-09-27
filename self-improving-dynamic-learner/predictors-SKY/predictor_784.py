"""
Predictor 784
Generated on: 2025-09-09 20:48:38
Accuracy: 52.94%
"""


# PREDICTOR 784 - Accuracy: 52.94%
# Correct predictions: 5294/10000 (52.94%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B > 60 and C > 60 and E < 20:
        if D < 30 or D > 60:
            return 1
        else:
            return 4
    if C < 20 and D > 80 and E > 30:
        return 4
    if C < 30 and E > 80 and B > 80:
        return 1
    if C < 30 and E > 80 and B < 80:
        return 4
    if B > 25 and C > 85 and E < 20:
        return 3
    if B > 60 and C > 65 and E > 60 and D < 10:
        return 2
    if B > 60 and C > 65 and E > 60 and D > 80:
        return 2
    if B > 60 and C > 65 and E > 60:
        return 1
    if B + C < 90 and D > 70 and E > 60:
        return 3
    if B > 60 and C > 65:
        return 2
    return 1
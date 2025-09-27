"""
Predictor 354
Generated on: 2025-09-09 15:45:23
Accuracy: 55.77%
"""


# PREDICTOR 354 - Accuracy: 55.77%
# Correct predictions: 5577/10000 (55.77%)

def predict_output(A, B, C, D, E):
    if B > 70 and C < 30 and D < 20:
        return 3
    if B > 80 and C < 20:
        return 4
    if B > 80 and C < 30 and E > 70:
        return 4
    if C > 70 and E < 20:
        return 4
    if C < 40 and E > 80 and B < 70 and D > 20:
        return 4
    if A < 40 and B > 60 and C > 70 and E > 65 and E < 80:
        return 2
    if B > 70 and C < 40 and E > 80:
        return 2
    if C < 40 and E > 80 and D < 20:
        return 2
    if B < 30 and C < 20 and D > 40 and E > 30:
        return 3
    if B < 10 and C < 10:
        return 3
    if C < 15 and D > 40 and E < 20 and B < 50:
        return 3
    return 1
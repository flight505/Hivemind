"""
Predictor 486
Generated on: 2025-09-09 17:13:30
Accuracy: 46.91%
"""


# PREDICTOR 486 - Accuracy: 46.91%
# Correct predictions: 4691/10000 (46.91%)

def predict_output(A, B, C, D, E):
    if D > 80 and B < 15 and C < 20 and E < 10:
        return 4
    if C < 35 and E > 60:
        return 4
    if B > 80 and C > 60 and E > 75 and D < 20:
        return 1
    if B > 60 and C > 40:
        return 2
    if C < 35:
        if A < 35 and B > 25 and C < 25:
            return 1
        else:
            return 3
    return 1
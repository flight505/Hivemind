"""
Predictor 871
Generated on: 2025-09-09 21:38:32
Accuracy: 57.54%
"""


# PREDICTOR 871 - Accuracy: 57.54%
# Correct predictions: 5754/10000 (57.54%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B > 60 and C > 70 and E > 75 and D < 30:
        return 4
    if C < 30 and E > 70 and B > 10 and D < 50:
        return 4
    if B > 70 and C < 10 and D > 80 and E < 30:
        return 4
    if A < 20 and B > 40 and C > 35 and E < 20:
        return 4
    if B > 60 and C < 35 and D > 80 and E < 30:
        return 3
    if D > 95 and B < 45 and E > 65:
        return 3
    if B > 60 and C > 60 and A < 40:
        return 2
    return 1
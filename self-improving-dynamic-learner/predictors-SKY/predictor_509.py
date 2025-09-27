"""
Predictor 509
Generated on: 2025-09-09 17:28:52
Accuracy: 56.61%
"""


# PREDICTOR 509 - Accuracy: 56.61%
# Correct predictions: 5661/10000 (56.61%)

def predict_output(A, B, C, D, E):
    if B > 70 and C < 35 and E < 20 and D > 20:
        return 4
    if B < 40 and C < 25 and E > 80:
        return 4
    if E > 50 and B < 50 and C < 40:
        return 4
    if B > 60 and C < 10 and E < 50:
        return 3
    if B < 30 and C > 40 and E < 20:
        return 3
    if B > 80 and C < 40 and E < 15 and D < 20:
        return 3
    if B + C < 30:
        return 3
    if B > 60 and C > 60 and A < 50 and E > 60:
        return 2
    return 1
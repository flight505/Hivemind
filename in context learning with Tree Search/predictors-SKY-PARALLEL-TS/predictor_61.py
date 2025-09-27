"""
Predictor 61
Generated on: 2025-09-09 23:24:50
Accuracy: 53.67%
"""


# PREDICTOR 61 - Accuracy: 53.67%
# Correct predictions: 5367/10000 (53.67%)

def predict_output(A, B, C, D, E):
    if B + C > 155 and E < 20:
        return 2
    if C - (D + E) > 30:
        return 3
    if A < 10 and B > 70:
        return 4
    if C < 15 and D > 55:
        return 4
    if B > 80 and D < 25 and E > 80:
        return 4
    if A > 90 and B > 90:
        return 4
    if E < 20 and (C + D) > 100:
        return 4
    if A > 90 and E < 10:
        return 2
    else:
        return 1
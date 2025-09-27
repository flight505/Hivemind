"""
Predictor 2
Generated on: 2025-09-09 12:04:46
Accuracy: 56.51%
"""


# PREDICTOR 2 - Accuracy: 56.51%
# Correct predictions: 5651/10000 (56.51%)

def predict_output(A, B, C, D, E):
    if E >= 94:
        return 4
    if B >= 95:
        return 1
    if C <= 12 and A + B >= 170:
        return 1
    if C <= 12 and E >= 55:
        return 4
    if C <= 12:
        return 3
    if A <= 10 and E >= 80:
        return 1
    if A <= 35 and B >= 65 and C >= 65:
        return 2
    if C < 30 and A >= 80 and E <= 30:
        return 3
    if A <= 20 and 60 <= B <= 75 and 50 <= C <= 65 and E <= 20:
        return 4
    if D <= 30 and E >= 70:
        return 4
    return 1
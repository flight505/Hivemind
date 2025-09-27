"""
Predictor 716
Generated on: 2025-09-09 19:57:30
Accuracy: 52.00%
"""


# PREDICTOR 716 - Accuracy: 52.00%
# Correct predictions: 5200/10000 (52.00%)

def predict_output(A, B, C, D, E):
    if B + C < 30:
        return 3
    if E > 60 and C < 30:
        return 4
    if C > 90 and E < 20:
        return 4
    if C > 80 and E < 40 and B < 40:
        return 4
    if C > 80 and B < 65 and D > 70 and E < 55:
        return 3
    if 40 < B < 55 and 40 < C < 55 and E < 45:
        return 3
    if B >= 60 and 50 < C < 60 and D > 80 and E > 90:
        return 3
    if B > 80 and C > 35 and E < 60:
        return 2
    if B > 60 and C > 70:
        return 2
    return 1
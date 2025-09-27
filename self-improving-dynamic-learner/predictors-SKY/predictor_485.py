"""
Predictor 485
Generated on: 2025-09-09 17:12:34
Accuracy: 57.17%
"""


# PREDICTOR 485 - Accuracy: 57.17%
# Correct predictions: 5717/10000 (57.17%)

def predict_output(A, B, C, D, E):
    if E > 90 and C < 30:
        return 4
    if C > 75 and B > 60 and E > 65:
        return 2
    if B < 20 and C < 20 and E < 40:
        return 3
    return 1
"""
Predictor 661
Generated on: 2025-09-09 19:16:27
Accuracy: 54.19%
"""


# PREDICTOR 661 - Accuracy: 54.19%
# Correct predictions: 5419/10000 (54.19%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15 and E < 40:
        return 3
    if C > 75 and B > 60 and E > 65:
        return 2
    if E > 90:
        return 4
    return 1
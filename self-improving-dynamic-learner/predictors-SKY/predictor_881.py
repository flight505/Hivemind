"""
Predictor 881
Generated on: 2025-09-09 21:42:22
Accuracy: 58.40%
"""


# PREDICTOR 881 - Accuracy: 58.40%
# Correct predictions: 5840/10000 (58.40%)

def predict_output(A, B, C, D, E):
    if E > 90 and C < 25:
        return 4
    if B < 20 and C < 15:
        return 3
    if A < 50 and B > 60 and C > 70 and E > 65:
        return 2
    return 1
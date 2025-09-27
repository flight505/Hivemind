"""
Predictor 1
Generated on: 2025-09-09 03:34:54
Accuracy: 37.54%
"""


# PREDICTOR 1 - Accuracy: 37.54%
# Correct predictions: 3754/10000 (37.54%)

def predict_output(A, B, C, D, E):
    if B <= 15:
        return 3
    elif E >= 90:
        return 4
    elif C > 75:
        return 2
    else:
        return 1
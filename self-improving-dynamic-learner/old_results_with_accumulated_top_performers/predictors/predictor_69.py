"""
Predictor 69
Generated on: 2025-09-09 03:26:43
Accuracy: 29.54%
"""


# PREDICTOR 69 - Accuracy: 29.54%
# Correct predictions: 2954/10000 (29.54%)

def predict_output(A, B, C, D, E):
    s = B + C
    if s < 30:
        return 3
    elif s < 60:
        return 4
    elif s < 100:
        return 1
    else:
        return 2
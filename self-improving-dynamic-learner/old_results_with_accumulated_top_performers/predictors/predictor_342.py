"""
Predictor 342
Generated on: 2025-09-09 08:52:49
Accuracy: 34.56%
"""


# PREDICTOR 342 - Accuracy: 34.56%
# Correct predictions: 3456/10000 (34.56%)

def predict_output(A, B, C, D, E):
    if B < 20:
        return 3
    elif C > 70:
        return 2
    elif E > 90:
        return 4
    else:
        return 1
"""
Predictor 362
Generated on: 2025-09-09 09:49:04
Accuracy: 50.91%
"""


# PREDICTOR 362 - Accuracy: 50.91%
# Correct predictions: 5091/10000 (50.91%)

def predict_output(A, B, C, D, E):
    if E > 90 and C < 30:
        return 4
    elif C < 15 and B < 30:
        return 3
    elif C > 50:
        if A < 40:
            return 2
        else:
            return 1
    else:
        return 1
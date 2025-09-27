"""
Predictor 1
Generated on: 2025-09-09 17:00:32
Accuracy: 36.78%
"""


# PREDICTOR 1 - Accuracy: 36.78%
# Correct predictions: 3678/10000 (36.78%)

def predict_output(A, B, C, D, E):
    if B < 20:
        return 3
    elif C > 75:
        return 2
    elif E > 90:
        return 4
    else:
        return 1
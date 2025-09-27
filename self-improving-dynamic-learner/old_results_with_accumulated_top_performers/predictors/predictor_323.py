"""
Predictor 323
Generated on: 2025-09-09 08:22:54
Accuracy: 36.47%
"""


# PREDICTOR 323 - Accuracy: 36.47%
# Correct predictions: 3647/10000 (36.47%)

def predict_output(A, B, C, D, E):
    if E == max(A, B, C, D, E):
        return 4
    elif C < 15:
        return 3
    elif C > 70:
        return 2
    else:
        return 1
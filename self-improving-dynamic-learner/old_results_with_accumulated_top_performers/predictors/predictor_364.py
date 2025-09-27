"""
Predictor 364
Generated on: 2025-09-09 09:54:20
Accuracy: 30.99%
"""


# PREDICTOR 364 - Accuracy: 30.99%
# Correct predictions: 3099/10000 (30.99%)

def predict_output(A, B, C, D, E):
    if A == max(A, B, C, D, E):
        return 3
    elif B == max(A, B, C, D, E):
        if C > 80:
            return 2
        else:
            return 1
    elif C == max(A, B, C, D, E):
        return 2
    elif D == max(A, B, C, D, E):
        if B < 20:
            return 3
        else:
            return 1
    else:
        return 4
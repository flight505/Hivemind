"""
Predictor 10
Generated on: 2025-09-09 23:16:45
Accuracy: 36.47%
"""


# PREDICTOR 10 - Accuracy: 36.47%
# Correct predictions: 3647/10000 (36.47%)

def predict_output(A, B, C, D, E):
    if A + E > 160:
        return 2
    elif C * D > 4500:
        return 3
    elif B - C > 40:
        return 4
    else:
        return 1
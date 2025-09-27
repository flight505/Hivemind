"""
Predictor 1
Generated on: 2025-09-09 23:16:45
Accuracy: 45.74%
"""


# PREDICTOR 1 - Accuracy: 45.74%
# Correct predictions: 4574/10000 (45.74%)

def predict_output(A, B, C, D, E):
    if min(A, C) < 10 and max(B, D) > 70:
        return 4
    elif A > 90:
        return 2
    elif B < 10:
        return 3
    else:
        return 1
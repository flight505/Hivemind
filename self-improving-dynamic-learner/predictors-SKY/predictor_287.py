"""
Predictor 287
Generated on: 2025-09-09 15:03:10
Accuracy: 49.91%
"""


# PREDICTOR 287 - Accuracy: 49.91%
# Correct predictions: 4991/10000 (49.91%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    elif B > 60 and C > 70:
        return 2
    elif E > 90:
        return 4
    else:
        return 1
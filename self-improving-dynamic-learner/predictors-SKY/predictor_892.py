"""
Predictor 892
Generated on: 2025-09-09 21:47:08
Accuracy: 56.65%
"""


# PREDICTOR 892 - Accuracy: 56.65%
# Correct predictions: 5665/10000 (56.65%)

def predict_output(A, B, C, D, E):
    if B > 60 and C > 75 and E > 65:
        return 2
    elif B < 20 and C < 15:
        return 3
    elif E > 90 and C < 25:
        return 4
    else:
        return 1
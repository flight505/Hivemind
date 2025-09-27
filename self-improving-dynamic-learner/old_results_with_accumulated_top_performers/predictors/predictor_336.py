"""
Predictor 336
Generated on: 2025-09-09 08:42:20
Accuracy: 55.72%
"""


# PREDICTOR 336 - Accuracy: 55.72%
# Correct predictions: 5572/10000 (55.72%)

def predict_output(A, B, C, D, E):
    if B > A + C + D + E:
        return 2
    elif D > A + B + C + E:
        return 4
    elif C < A + B + D + E:
        return 1
    else:
        return 3
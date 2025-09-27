"""
Predictor 672
Generated on: 2025-09-09 19:24:31
Accuracy: 53.84%
"""


# PREDICTOR 672 - Accuracy: 53.84%
# Correct predictions: 5384/10000 (53.84%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    elif E > 90:
        return 4
    elif B > 60 and C > 75 and E > 65:
        return 2
    else:
        return 1
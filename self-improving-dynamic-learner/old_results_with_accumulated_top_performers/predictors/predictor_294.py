"""
Predictor 294
Generated on: 2025-09-09 07:26:05
Accuracy: 47.01%
"""


# PREDICTOR 294 - Accuracy: 47.01%
# Correct predictions: 4701/10000 (47.01%)

def predict_output(A, B, C, D, E):
    if B < 25 and C < 25:
        return 3
    elif E > 80:
        return 4
    elif B > 70 and C > 60 and D < 20:
        return 1
    elif B > 60 and C > 60:
        return 2
    else:
        return 1
"""
Predictor 474
Generated on: 2025-09-09 17:03:43
Accuracy: 53.49%
"""


# PREDICTOR 474 - Accuracy: 53.49%
# Correct predictions: 5349/10000 (53.49%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    elif E > 90 and C < 25:
        return 4
    elif B > 60 and C > 75:
        return 2
    else:
        return 1
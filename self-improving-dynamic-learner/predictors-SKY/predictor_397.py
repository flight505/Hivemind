"""
Predictor 397
Generated on: 2025-09-09 16:12:08
Accuracy: 52.73%
"""


# PREDICTOR 397 - Accuracy: 52.73%
# Correct predictions: 5273/10000 (52.73%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    elif B > 60 and C > 70:
        return 2
    elif C < 30 and E > 90:
        return 4
    else:
        return 1
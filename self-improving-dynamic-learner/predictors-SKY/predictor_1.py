"""
Predictor 1
Generated on: 2025-09-09 12:01:34
Accuracy: 34.53%
"""


# PREDICTOR 1 - Accuracy: 34.53%
# Correct predictions: 3453/10000 (34.53%)

def predict_output(A, B, C, D, E):
    if B < 20:
        return 3
    elif E > 90:
        return 4
    elif C > 70:
        return 2
    else:
        return 1
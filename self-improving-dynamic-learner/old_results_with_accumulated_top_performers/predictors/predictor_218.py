"""
Predictor 218
Generated on: 2025-09-09 05:35:19
Accuracy: 29.34%
"""


# PREDICTOR 218 - Accuracy: 29.34%
# Correct predictions: 2934/10000 (29.34%)

def predict_output(A, B, C, D, E):
    if B < 25:
        if C < 25:
            return 3
        elif E > 80:
            return 4
        else:
            return 2
    else:
        if C > 60:
            return 1
        else:
            return 2
"""
Predictor 199
Generated on: 2025-09-09 08:04:54
Accuracy: 40.64%
"""


# PREDICTOR 199 - Accuracy: 40.64%
# Correct predictions: 4064/10000 (40.64%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    elif C > 75:
        return 2
    elif C < 10:
        return 3
    else:
        return 1
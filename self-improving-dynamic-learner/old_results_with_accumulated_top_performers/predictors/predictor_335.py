"""
Predictor 335
Generated on: 2025-09-09 08:40:14
Accuracy: 35.76%
"""


# PREDICTOR 335 - Accuracy: 35.76%
# Correct predictions: 3576/10000 (35.76%)

def predict_output(A, B, C, D, E):
    if A + B + C < 60:
        return 3
    elif A + D + E > 200:
        return 1
    elif B + C > A + E:
        return 2
    else:
        return 1
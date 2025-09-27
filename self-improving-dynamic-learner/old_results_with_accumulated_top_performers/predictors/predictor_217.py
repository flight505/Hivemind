"""
Predictor 217
Generated on: 2025-09-09 05:31:32
Accuracy: 50.27%
"""


# PREDICTOR 217 - Accuracy: 50.27%
# Correct predictions: 5027/10000 (50.27%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    elif B < 25 and C < 25:
        return 3
    elif C > 60 and A <= 30:
        return 2
    else:
        return 1
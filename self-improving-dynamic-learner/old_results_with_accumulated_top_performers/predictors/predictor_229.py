"""
Predictor 229
Generated on: 2025-09-09 05:45:50
Accuracy: 48.81%
"""


# PREDICTOR 229 - Accuracy: 48.81%
# Correct predictions: 4881/10000 (48.81%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    elif B < 20 and C < 25:
        return 3
    elif C > 60 and A < 50:
        return 2
    else:
        return 1
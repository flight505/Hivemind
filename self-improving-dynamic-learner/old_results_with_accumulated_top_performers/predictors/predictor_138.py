"""
Predictor 138
Generated on: 2025-09-09 04:23:58
Accuracy: 37.15%
"""


# PREDICTOR 138 - Accuracy: 37.15%
# Correct predictions: 3715/10000 (37.15%)

def predict_output(A, B, C, D, E):
    if C > 75:
        return 2
    elif E > 90:
        return 4
    elif B < 20:
        return 3
    else:
        return 1
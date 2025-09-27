"""
Predictor 848
Generated on: 2025-09-09 21:26:14
Accuracy: 53.49%
"""


# PREDICTOR 848 - Accuracy: 53.49%
# Correct predictions: 5349/10000 (53.49%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B > 60 and C > 75:
        return 2
    if C < 25 and E > 90:
        return 4
    return 1
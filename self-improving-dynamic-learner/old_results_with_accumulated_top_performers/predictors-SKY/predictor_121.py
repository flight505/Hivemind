"""
Predictor 121
Generated on: 2025-09-09 05:38:32
Accuracy: 52.28%
"""


# PREDICTOR 121 - Accuracy: 52.28%
# Correct predictions: 5228/10000 (52.28%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15 and B < 20:
        return 3
    if C > 70 and B > 60:
        return 2
    return 1
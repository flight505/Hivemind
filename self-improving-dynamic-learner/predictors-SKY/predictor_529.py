"""
Predictor 529
Generated on: 2025-09-09 17:41:57
Accuracy: 50.19%
"""


# PREDICTOR 529 - Accuracy: 50.19%
# Correct predictions: 5019/10000 (50.19%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if B < 20 and C < 15:
        return 3
    if C > 70 and B > 60:
        return 2
    return 1
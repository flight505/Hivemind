"""
Predictor 430
Generated on: 2025-09-09 16:32:15
Accuracy: 54.36%
"""


# PREDICTOR 430 - Accuracy: 54.36%
# Correct predictions: 5436/10000 (54.36%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if B < 20 and C < 15:
        return 3
    if C > 75 and B > 60 and E > 70:
        return 2
    return 1
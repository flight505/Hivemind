"""
Predictor 768
Generated on: 2025-09-09 20:33:14
Accuracy: 50.71%
"""


# PREDICTOR 768 - Accuracy: 50.71%
# Correct predictions: 5071/10000 (50.71%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    if C > 70 and B < 35:
        return 4
    if A < 50 and B > 60 and C > 70 and E > 60:
        return 2
    if E > 90:
        return 4
    else:
        return 1
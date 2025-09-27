"""
Predictor 767
Generated on: 2025-09-09 20:32:15
Accuracy: 50.71%
"""


# PREDICTOR 767 - Accuracy: 50.71%
# Correct predictions: 5071/10000 (50.71%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 15:
        return 3
    if A < 50 and C > 30 and E > 60:
        return 2
    if E > 90:
        return 4
    else:
        return 1
"""
Predictor 809
Generated on: 2025-09-10 00:50:43
Accuracy: 51.71%
"""


# PREDICTOR 809 - Accuracy: 51.71%
# Correct predictions: 5171/10000 (51.71%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (A < 5 and C > 80):
        return 4
    elif (A < 20 and B > 70 and C < 25) or (B < 10 and C < 20):
        return 3
    elif B > 65 and C < 45:
        return 2
    else:
        return 1
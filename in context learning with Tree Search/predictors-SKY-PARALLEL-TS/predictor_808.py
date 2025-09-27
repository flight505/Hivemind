"""
Predictor 808
Generated on: 2025-09-10 00:50:43
Accuracy: 51.14%
"""


# PREDICTOR 808 - Accuracy: 51.14%
# Correct predictions: 5114/10000 (51.14%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C > 80 and E < 20):
        return 4
    elif (B > 70 and C < 20) or (B < 10 and C < 20):
        return 3
    elif B > 65 and C < 45:
        return 2
    else:
        return 1
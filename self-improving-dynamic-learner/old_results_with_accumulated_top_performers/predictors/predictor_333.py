"""
Predictor 333
Generated on: 2025-09-09 08:38:55
Accuracy: 54.79%
"""


# PREDICTOR 333 - Accuracy: 54.79%
# Correct predictions: 5479/10000 (54.79%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    elif B < 20 and C < 15:
        return 3
    elif B > 60 and C > 60 and A < 40:
        return 2
    else:
        return 1
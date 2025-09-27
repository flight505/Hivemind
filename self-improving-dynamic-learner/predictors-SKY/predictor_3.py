"""
Predictor 3
Generated on: 2025-09-09 12:03:01
Accuracy: 42.92%
"""


# PREDICTOR 3 - Accuracy: 42.92%
# Correct predictions: 4292/10000 (42.92%)

def predict_output(A, B, C, D, E):
    if E > 80 or (E > 70 and C < 20):
        return 4
    elif B < 20 and E < 50:
        return 3
    elif C > 60 and E < 45:
        return 3
    elif C >= 70 and E >= 70 and A < 60:
        return 2
    else:
        return 1
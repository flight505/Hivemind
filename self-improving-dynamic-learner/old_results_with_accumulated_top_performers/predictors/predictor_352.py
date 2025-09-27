"""
Predictor 352
Generated on: 2025-09-09 09:21:36
Accuracy: 50.99%
"""


# PREDICTOR 352 - Accuracy: 50.99%
# Correct predictions: 5099/10000 (50.99%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    elif E > 90:
        return 4
    elif A > 80 and B > 60 and C > 60:
        return 1
    elif B > 60 and C > 60:
        return 2
    else:
        return 1
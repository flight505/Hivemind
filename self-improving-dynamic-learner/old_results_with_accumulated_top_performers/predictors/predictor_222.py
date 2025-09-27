"""
Predictor 222
Generated on: 2025-09-09 05:39:31
Accuracy: 55.49%
"""


# PREDICTOR 222 - Accuracy: 55.49%
# Correct predictions: 5549/10000 (55.49%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    elif B < 20 and C < 20:
        return 3
    elif A > 50 and B > 60 and C > 60:
        return 1
    elif B > 60 and C > 60:
        return 2
    else:
        return 1
"""
Predictor 381
Generated on: 2025-09-09 10:42:59
Accuracy: 50.67%
"""


# PREDICTOR 381 - Accuracy: 50.67%
# Correct predictions: 5067/10000 (50.67%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    elif B > 60 and C > 60:
        if A > 70:
            return 1
        else:
            return 2
    elif E > 80:
        return 4
    else:
        return 1
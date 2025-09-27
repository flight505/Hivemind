"""
Predictor 325
Generated on: 2025-09-09 08:25:06
Accuracy: 39.79%
"""


# PREDICTOR 325 - Accuracy: 39.79%
# Correct predictions: 3979/10000 (39.79%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    elif E > 90:
        return 4
    elif B > 70 and C > 60 and D < 20:
        return 1
    elif B > 60 and C > 60:
        return 2
    elif A > 70 or D > 70:
        return 1
    else:
        return 3
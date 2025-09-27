"""
Predictor 249
Generated on: 2025-09-09 06:16:25
Accuracy: 45.40%
"""


# PREDICTOR 249 - Accuracy: 45.40%
# Correct predictions: 4540/10000 (45.40%)

def predict_output(A, B, C, D, E):
    if B < 25 and C < 25:
        return 3
    elif E > 80 and C < 25:
        return 4
    elif B > 70 and C > 60:
        return 1
    elif B > 70:
        return 2
    elif B < 25:
        return 4
    elif A > 70 and B > 30 and C > 25:
        return 1
    else:
        return 1
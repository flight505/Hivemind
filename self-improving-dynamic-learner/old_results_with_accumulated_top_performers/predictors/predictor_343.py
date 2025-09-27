"""
Predictor 343
Generated on: 2025-09-09 08:53:50
Accuracy: 54.44%
"""


# PREDICTOR 343 - Accuracy: 54.44%
# Correct predictions: 5444/10000 (54.44%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    elif B < 20 and C < 15:
        return 3
    elif A <= 30 and B > 60 and C > 60:
        return 2
    elif D > 80:
        return 1
    else:
        return 1
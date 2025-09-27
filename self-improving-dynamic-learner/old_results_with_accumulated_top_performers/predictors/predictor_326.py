"""
Predictor 326
Generated on: 2025-09-09 08:28:12
Accuracy: 20.76%
"""


# PREDICTOR 326 - Accuracy: 20.76%
# Correct predictions: 2076/10000 (20.76%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    elif E > 90:
        return 4
    elif B > 60 and C > 60:
        return 2
    elif A > 50 and D > 70:
        return 1
    else:
        return 3
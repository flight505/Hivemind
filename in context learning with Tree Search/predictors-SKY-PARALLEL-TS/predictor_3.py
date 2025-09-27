"""
Predictor 3
Generated on: 2025-09-09 23:16:45
Accuracy: 41.91%
"""


# PREDICTOR 3 - Accuracy: 41.91%
# Correct predictions: 4191/10000 (41.91%)

def predict_output(A, B, C, D, E):
    if ((B - A > 70 or D - C > 70) and (A < 10 or C < 10)):
        return 4
    elif A > 90:
        return 2
    elif B < 25:
        return 3
    else:
        return 1
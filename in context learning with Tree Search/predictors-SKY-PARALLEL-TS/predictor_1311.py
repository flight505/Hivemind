"""
Predictor 1311
Generated on: 2025-09-10 02:02:09
Accuracy: 53.60%
"""


# PREDICTOR 1311 - Accuracy: 53.60%
# Correct predictions: 5360/10000 (53.60%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 10 and D > 90 and E > 80) or (E > 90 and D < 40 and C > 50) or (C > 50 and D < 25 and E > 50) or (A > 80 and B < 40 and C > 70 and E > 80):
        return 4
    elif A < 10 and B > 95 and C < 35:
        return 2
    elif B > 80 and C > 75 and D > 90:
        return 3
    else:
        return 1
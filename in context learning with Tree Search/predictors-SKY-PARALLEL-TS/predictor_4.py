"""
Predictor 4
Generated on: 2025-09-09 23:16:45
Accuracy: 53.83%
"""


# PREDICTOR 4 - Accuracy: 53.83%
# Correct predictions: 5383/10000 (53.83%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90):
        return 4
    elif A > 90 and E < 10:
        return 2
    elif B < 10 and D > 80:
        return 3
    else:
        return 1
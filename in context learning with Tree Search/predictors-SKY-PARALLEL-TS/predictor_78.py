"""
Predictor 78
Generated on: 2025-09-09 23:27:20
Accuracy: 53.94%
"""


# PREDICTOR 78 - Accuracy: 53.94%
# Correct predictions: 5394/10000 (53.94%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 40) or (A > 80 and B < 10) or (C > 90 and D < 25) or (B > 75 and C < 10):
        return 4
    elif B > 90:
        return 2
    elif (E < 15 and D > 50 and C > 50) or (A > 90 and C < 40 and E > 90):
        return 3
    else:
        return 1
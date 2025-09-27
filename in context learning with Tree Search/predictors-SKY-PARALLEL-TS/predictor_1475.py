"""
Predictor 1475
Generated on: 2025-09-10 02:31:46
Accuracy: 53.90%
"""


# PREDICTOR 1475 - Accuracy: 53.90%
# Correct predictions: 5390/10000 (53.90%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C > 5) or (D - C > 80) or (A >= 70 and C < 30 and D > 50) or (C > 90 and E < 10):
        return 4
    elif (A > 90 and B > 70) or (A < 10 and B > 60 and E > 50):
        return 2
    elif (C > 70 and B < 10) or (A < 10 and B < 10 and C > 70):
        return 3
    else:
        return 1
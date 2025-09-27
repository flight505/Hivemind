"""
Predictor 1169
Generated on: 2025-09-10 01:39:40
Accuracy: 50.87%
"""


# PREDICTOR 1169 - Accuracy: 50.87%
# Correct predictions: 5087/10000 (50.87%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (B > 90) or (C < 30 and D > 70) or (A < 40 and E < 20):
        return 4
    elif (A > 90 and E < 10) or (D < 5 and E > 70):
        return 2
    elif B < 10 and C > 70:
        return 3
    else:
        return 1
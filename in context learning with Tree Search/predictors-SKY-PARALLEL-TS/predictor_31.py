"""
Predictor 31
Generated on: 2025-09-09 23:19:12
Accuracy: 41.87%
"""


# PREDICTOR 31 - Accuracy: 41.87%
# Correct predictions: 4187/10000 (41.87%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (A > 60 and D < 30 and E > 70):
        return 4
    elif (A > 90 and E < 10) or (B > 70 and C > 60 and E < 30) or (A < 10 and B < 20 and E > 40):
        return 2
    elif B < 20 or (D > 60 and C < 40) or A > 90:
        return 3
    else:
        return 1
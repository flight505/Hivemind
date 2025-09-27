"""
Predictor 1143
Generated on: 2025-09-10 01:35:54
Accuracy: 47.41%
"""


# PREDICTOR 1143 - Accuracy: 47.41%
# Correct predictions: 4741/10000 (47.41%)

def predict_output(A, B, C, D, E):
    if (C > 90 or
        (A < 20 and B < 20 and C > 90) or
        (B > 90) or
        (C < 20 and D > 50) or
        (A < 50 and C > 90) or
        (E < 15 and C < 30 and D > 55)):
        return 4
    elif (B > 70 and E > 70) or (D < 15 and E > 50) or (B > 60 and D < 15 and E > 45):
        return 2
    elif B > 70 and C < 15:
        return 3
    else:
        return 1
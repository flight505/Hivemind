"""
Predictor 754
Generated on: 2025-09-10 00:44:16
Accuracy: 54.41%
"""


# PREDICTOR 754 - Accuracy: 54.41%
# Correct predictions: 5441/10000 (54.41%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90) or (D < 5 and E > 70 and A > 50) or (C < 5 and B > 70) or (B < 10 and E > 80):
        return 4
    elif B > 85 and C > 80 and A < 50:
        return 2
    elif B < 10 and D > 80:
        return 3
    else:
        return 1
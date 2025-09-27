"""
Predictor 964
Generated on: 2025-09-10 01:09:35
Accuracy: 53.05%
"""


# PREDICTOR 964 - Accuracy: 53.05%
# Correct predictions: 5305/10000 (53.05%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 90 and B > 50) or (B > 90 and D > 90) or (C > 60 and E < 10):
        return 4
    elif (A < 15 and E > 90 and B < 40) or (B > 95):
        return 2
    elif (A > 50 and C < 5 and D < 25 and E < 30) or (B < 10 and D > 80):
        return 3
    else:
        return 1
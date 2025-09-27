"""
Predictor 1128
Generated on: 2025-09-10 01:35:54
Accuracy: 53.05%
"""


# PREDICTOR 1128 - Accuracy: 53.05%
# Correct predictions: 5305/10000 (53.05%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (C < 25 and E > 70) or (A > 80 and C < 40 and E > 55) or (B > 75 and C < 15) or (C > 60 and E < 40) or (B < 10 and A > 80 and C < 20 and D > 70 and E < 20):
        return 4
    elif (C > 90 and B < 20) or (B > 70 and C > 90) or (B > 90) or (A < 10 and B > 60 and D < 5 and E > 70):
        return 2
    elif (A > 50 and C < 50 and D > 70) or (C <= 10 and E < 60) or (A > 60 and B < 20 and C < 15):
        return 3
    else:
        return 1
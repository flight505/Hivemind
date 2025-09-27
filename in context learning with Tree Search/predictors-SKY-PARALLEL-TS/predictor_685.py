"""
Predictor 685
Generated on: 2025-09-10 00:34:06
Accuracy: 55.42%
"""


# PREDICTOR 685 - Accuracy: 55.42%
# Correct predictions: 5542/10000 (55.42%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 10 and D > 90) or
        (50 < A < 60 and B > 60 and C < 40 and E > 60) or
        (A > 90 and B > 60 and C < 40 and E > 60) or
        (C > 90 and E < 15 and A < 30)):
        return 4
    if ((A < 10 and B < 20 and C < 10 and E > 70) or
        (B > 95 and E > 85) or
        (A < 50 and C > 55 and D < 20 and E > 60)):
        return 2
    if ((A > 65 and D > 65 and E > 70) or
        (A < 30 and B > 40 and C < 20 and E < 5)):
        return 3
    else:
        return 1
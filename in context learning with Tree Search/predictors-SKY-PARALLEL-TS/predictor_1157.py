"""
Predictor 1157
Generated on: 2025-09-10 01:37:38
Accuracy: 57.11%
"""


# PREDICTOR 1157 - Accuracy: 57.11%
# Correct predictions: 5711/10000 (57.11%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 65 and E < 20) or
        (C < 15 and D > 90 and E > 70) or
        (C < 5 and E > 60) or
        (A < 5 and B > 65 and C > 50 and E < 20) or
        (A > 60 and B > 80 and C > 60 and D < 25 and E > 90)):
        return 4
    elif (B > 80 and C > 70 and A < 50):
        return 2
    elif (A > 60 and E < 10 and C > 30):
        return 3
    else:
        return 1
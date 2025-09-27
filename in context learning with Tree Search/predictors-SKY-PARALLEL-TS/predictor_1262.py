"""
Predictor 1262
Generated on: 2025-09-10 01:54:58
Accuracy: 55.11%
"""


# PREDICTOR 1262 - Accuracy: 55.11%
# Correct predictions: 5511/10000 (55.11%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C > 30 and E < 20 and D < 50) or
        (C < 10 and D > 90) or
        (A > 70 and C < 10) or
        (A > 60 and E < 10 and B < 30) or
        (B < 10 and C > 60)):
        return 4
    elif (B > 90 and ((C > 60 and E < 10) or C > 90)):
        return 2
    elif (A > 45 and C < 50 and D > 55 and B > 35 and B < 50 and E < 40):
        return 3
    else:
        return 1
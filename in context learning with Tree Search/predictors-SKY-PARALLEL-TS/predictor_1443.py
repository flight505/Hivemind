"""
Predictor 1443
Generated on: 2025-09-10 02:27:48
Accuracy: 54.58%
"""


# PREDICTOR 1443 - Accuracy: 54.58%
# Correct predictions: 5458/10000 (54.58%)

def predict_output(A, B, C, D, E):
    if ((A < 15 and B > 65) or
        (C < 15 and D > 80) or
        (C > 90 and E < 25) or
        (E > 85 and D < 35) or
        (A < 25 and B < 25 and C > 45) or
        (C < 5 and E > 95)):
        return 4
    elif (A < 15 and B > 85 and C > 65):
        return 2
    elif (A > 85 and B < 15 and C < 45 and D > 40 and E > 30):
        return 3
    else:
        return 1
"""
Predictor 994
Generated on: 2025-09-10 01:13:58
Accuracy: 53.40%
"""


# PREDICTOR 994 - Accuracy: 53.40%
# Correct predictions: 5340/10000 (53.40%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C > 10) or (C < 20 and D > 60 and A > 50):
        return 4
    elif (A > 60 and E < 10 and C > 40) or (B > 60 and C < 40 and D < 20 and E > 50 and A < 50):
        return 2
    elif (A < 10 and B > 70 and C < 5 and D < 30) or (C > 90 and D < 5) or (B > 60 and C > 90) or (B > 80 and D > 80):
        return 3
    else:
        return 1
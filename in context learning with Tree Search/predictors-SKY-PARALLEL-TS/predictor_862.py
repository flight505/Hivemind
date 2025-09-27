"""
Predictor 862
Generated on: 2025-09-10 00:55:50
Accuracy: 52.26%
"""


# PREDICTOR 862 - Accuracy: 52.26%
# Correct predictions: 5226/10000 (52.26%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and E < 20) or (C < 15 and D > 90 and E > 80) or (A > 80 and B < 10) or (A > 60 and B < 10 and C > 50 and D < 20):
        return 4
    elif B > 80 and A < 40 and C > 40 and D > 60:
        return 2
    elif (A > 40 and B > 40 and C > 40 and E < 20) or (C < 15 and A > 50 and E < 30):
        return 3
    else:
        return 1
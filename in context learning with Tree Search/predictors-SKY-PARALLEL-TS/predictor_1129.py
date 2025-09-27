"""
Predictor 1129
Generated on: 2025-09-10 01:35:54
Accuracy: 53.86%
"""


# PREDICTOR 1129 - Accuracy: 53.86%
# Correct predictions: 5386/10000 (53.86%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (A > 80 and B < 40 and C < 40 and E > 50) or (A < 30 and C > 60) or (B > 80 and C < 5 and D > 70):
        return 4
    elif (A > 80 and B < 20 and C > 90) or (B > 70 and C > 90) or (A < 10 and B > 60 and D < 5 and E > 70) or (B > 90 and E > 80):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40) or (C < 10 and E < 60) or (A > 60 and B < 20 and C < 15):
        return 3
    else:
        return 1
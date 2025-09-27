"""
Predictor 1284
Generated on: 2025-09-10 01:58:17
Accuracy: 54.97%
"""


# PREDICTOR 1284 - Accuracy: 54.97%
# Correct predictions: 5497/10000 (54.97%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and E < 20) or (C < 10 and D > 90) or
        (A < 35 and B < 20 and C > 35 and D > 40 and E < 15) or
        (40 < A < 50 and B > 60 and C < 35 and D > 50 and E > 70) or
        (30 < A < 40 and B > 50 and C > 85 and D < 20) or
        (A < 35 and B > 90 and C < 20 and D > 95)):
        return 4
    elif ((A > 90 and E < 10) or
          (40 < A < 50 and B > 40 and C > 40 and D < 25 and E > 50) or
          (A > 80 and B > 80 and C < 35 and D > 65 and E > 70)):
        return 2
    elif (B < 10 and D > 80):
        return 3
    else:
        return 1
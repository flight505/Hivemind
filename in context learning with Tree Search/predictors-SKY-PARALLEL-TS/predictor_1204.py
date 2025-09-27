"""
Predictor 1204
Generated on: 2025-09-10 01:46:44
Accuracy: 61.55%
"""


# PREDICTOR 1204 - Accuracy: 61.55%
# Correct predictions: 6155/10000 (61.55%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 80 and A > 30) or
        (C < 25 and E > 65) or
        (A < 30 and B < 35 and C > 70 and E < 5) or
        (A > 65 and B > 60 and C < 35 and D < 10 and E > 95) or
        (50 < A < 60 and B < 55 and C < 20 and D > 95) or
        (A < 30 and B < 60 and C > 40 and D > 45 and E < 20)):
        return 4
    if ((B > 85 and C > 80 and A < 80 and 20 < D < 80 and (C < 85 or D > 25)) or
        (A < 40 and D < 25 and E > 50 and C > 40 and B > 60) or
        (A > 60 and B > 65 and C < 50 and D > 60 and E < 50) or
        (A < 50 and B > 80 and C < 35 and D > 80 and E > 80)):
        return 2
    if ((A > 45 and C > 15 and C < 50 and D > 55 and B > 35 and E > 50) or
        (C < 15 and D > 80 and A < 30)):
        return 3
    else:
        return 1
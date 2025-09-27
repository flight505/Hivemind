"""
Predictor 492
Generated on: 2025-09-10 00:08:08
Accuracy: 59.58%
"""


# PREDICTOR 492 - Accuracy: 59.58%
# Correct predictions: 5958/10000 (59.58%)

def predict_output(A, B, C, D, E):
    if ((B - A > 60 and E < 20 and C > 30) or
        (D - C > 80 and E > 80) or
        (C - B > 50 and E < 5) or
        (A - B > 70 and C < 15) or
        (B - D > 50 and C > 60 and E > 70 and A > 20) or
        (A < 10 and B > 70) or
        (C < 15 and D > 80) or
        (E > 75 and C < 30) or
        (B > 90 and C < 5) or
        (B > 90 and E > 85)):
        return 4
    if ((E - A > 80 and B < 60 and C < 20) or
        (B > 90 and E > 85 and C > 60) or
        (B > 85 and C > 80 and A < 60) or
        (B > 80 and C > 70 and D < 5 and E > 80) or
        (B > 80 and C > 50 and E > 50 and A < 50)):
        return 2
    if ((C - A > 20 and D < 25 and (E - B > 30)) or
        (D > 90 and B > 80 and C < 40 and E < 40) or
        (A > 50 and C < 50 and D > 70) or
        (C > 90 and B < 20) or
        (A < 20 and D > 60 and C < 10) or
        (D < 10 and B < 50 and E < 30 and C > 20)):
        return 3
    else:
        return 1
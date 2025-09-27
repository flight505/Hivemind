"""
Predictor 973
Generated on: 2025-09-10 01:11:30
Accuracy: 57.12%
"""


# PREDICTOR 973 - Accuracy: 57.12%
# Correct predictions: 5712/10000 (57.12%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 60 and E > 80) or
        (C < 25 and E > 65 and (A < 40 or B > 70)) or
        (A > 70 and B < 20 and C > 70) or
        (A < 30 and C > 75 and D < 30) or
        (A > 80 and B > 70 and C < 40 and D > 50 and E > 80) or
        (A > 75 and B < 40 and C < 35 and D < 25 and E > 95) or
        (A < 10 and B < 30 and C < 5 and D > 95 and E > 85)):
        return 4
    if ((B > 85 and C > 80 and D < 70) or
        (B > 70 and D < 20 and A < 50 and E > 40 and C > 30 and B > 75) or
        (D < 5 and C > 50 and E > 50 and B < 45) or
        (B > 90 and E > 85 and C < 70) or
        (A < 40 and D < 20 and E > 50 and C > 40 and B > 70 and A > 25)):
        return 2
    if ((A > 50 and C < 50 and D > 70 and B > 40) or
        (A < 50 and D < 25 and E < 20) or
        (D < 15 and C > 40 and B < 80) or
        (C <= 10 and E < 60) or
        (A > 75 and B < 25 and C < 45 and D > 60) or
        (A > 50 and B < 20 and C < 15) or
        (A > 80 and B < 30 and C < 45 and D > 40) or
        (A < 25 and B < 25 and C < 15 and D > 70 and E < 20) or
        (50 < A < 60 and B < 20 and C < 15 and D > 30 and E < 20) or
        (A > 80 and B < 30 and C < 45)):
        return 3
    else:
        return 1
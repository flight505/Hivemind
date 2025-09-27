"""
Predictor 104
Generated on: 2025-09-09 23:29:09
Accuracy: 56.73%
"""


# PREDICTOR 104 - Accuracy: 56.73%
# Correct predictions: 5673/10000 (56.73%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 55 and E > 80) or
        (C < 25 and E > 65) or
        (C > 70 and E < 20 and B < 10 and A > 70) or
        (A > 80 and B < 10 and D > 70 and E < 10) or
        (40 < A < 60 and B < 40 and C < 30 and E < 5) or
        (C < 5 and A > 90 and B > 85) or
        (E > 85 and B < 50) or
        (C > 80 and D < 20 and B < 20)):
        return 4
    if ((B > 85 and C > 80 and A < 80) or
        (B > 70 and D < 20 and A < 50 and E > 40) or
        (A > 90 and E < 10)):
        return 2
    if ((A > 50 and C < 50 and D > 70 and B > 35) or
        (A < 50 and D < 25 and E < 20 and B < 60) or
        (D < 15 and 40 < C < 80 and B < 80 and A < 70) or
        (C <= 10 and E < 60 and B < 50) or
        (A > 75 and B < 25 and C < 45 and D > 60) or
        (A > 80 and D > 90) or
        (B < 20 and D > 60 and E < 30) or
        (A > 70 and B < 30 and C < 10 and D > 80)):
        return 3
    else:
        return 1
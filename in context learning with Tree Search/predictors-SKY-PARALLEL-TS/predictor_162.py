"""
Predictor 162
Generated on: 2025-09-09 23:33:44
Accuracy: 63.71%
"""


# PREDICTOR 162 - Accuracy: 63.71%
# Correct predictions: 6371/10000 (63.71%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C < 85 and E > 10) or
        (C < 15 and D > 55 and E > 80) or
        (C < 25 and E > 65) or
        (C > 70 and E < 20 and B < 10 and A > 70) or
        (A > 80 and B < 10 and D > 70 and E < 10) or
        (40 < A < 60 and B < 40 and C < 30 and E < 5) or
        (C < 5 and A > 90 and B > 85) or
        (A < 20 and C > 75 and D < 30 and E < 20) or
        (A > 60 and B > 80 and C < 10 and D > 70) or
        (A < 15 and C > 60 and E < 5) or
        (A < 30 and C > 75 and D <= 30) or
        (A > 90 and C > 70 and D < 30 and E > 70) or
        (A > 50 and B < 40 and C > 35 and E < 10)):
        return 4
    if ((B > 85 and C > 80 and A < 80 and D < 80) or
        (B > 70 and D < 20 and A < 50 and E > 40) or
        (D < 5 and C > 50 and B < 50 and E > 50) or
        (B < 15 and D < 6 and E > 50) or
        (A < 40 and D < 25 and E > 50 and C > 40) or
        (B > 70 and C > 55 and E < 25 and A < 45)):
        return 2
    if ((A > 45 and C < 40 and D > 70 and B > 50) or
        (A < 50 and D < 25 and E < 40 and B < 80 and C < 40) or
        (D < 15 and C > 40 and B < 80 and A < 70 and E < 50) or
        (C <= 10 and E < 60 and B < 50) or
        (A > 75 and B < 25 and C < 45 and D > 60) or
        (B > 80 and C > 85 and D > 80 and A < 50) or
        (A < 40 and B > 90 and D > 90) or
        (B > 80 and D > 90 and E < 30) or
        (A > 60 and B < 15 and C < 15 and D > 70)):
        return 3
    else:
        return 1
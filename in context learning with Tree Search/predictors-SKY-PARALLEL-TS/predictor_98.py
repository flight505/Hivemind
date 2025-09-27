"""
Predictor 98
Generated on: 2025-09-09 23:29:09
Accuracy: 57.53%
"""


# PREDICTOR 98 - Accuracy: 57.53%
# Correct predictions: 5753/10000 (57.53%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 85 and C > 60) or
        (A > 90 and B > 80 and C > 40) or
        (B > 70 and D < 20 and A < 50 and E > 40)):
        return 2
    if ((A < 10 and B >= 70 and C < 35) or
        (C < 15 and D > 55 and E > 80 and A > 50) or
        (A > 80 and D < 20 and E > 95) or
        (A > 90 and C < 25 and D > 80) or
        (B < 25 and C > 85) or
        (B > 75 and C < 30 and E > 90) or
        (A > 95 and B > 85 and C < 35) or
        (C > 70 and E < 20 and B < 10 and A > 70) or
        (A > 80 and B < 10 and D > 70 and E < 10) or
        (40 < A < 60 and B < 40 and C < 30 and E < 5) or
        (C < 5 and A > 90 and B > 85)):
        return 4
    if ((A > 50 and C < 50 and D > 70 and B > 40) or
        (A < 50 and D < 25 and E < 20 and B < 80) or
        (D < 15 and C > 40 and B < 80 and A < 70) or
        (C <= 10 and E < 60 and B < 50) or
        (A > 75 and B < 25 and C < 45 and D > 60)):
        return 3
    else:
        return 1
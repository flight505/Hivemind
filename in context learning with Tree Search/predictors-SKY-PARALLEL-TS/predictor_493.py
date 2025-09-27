"""
Predictor 493
Generated on: 2025-09-10 00:08:08
Accuracy: 60.72%
"""


# PREDICTOR 493 - Accuracy: 60.72%
# Correct predictions: 6072/10000 (60.72%)

def predict_output(A, B, C, D, E):
    if ((C < 15 and D > 60 and B > 50) or
        (A < 10 and B > 70) or
        (C < 30 and E > 65) or
        (B > 90 and E > 90) or
        (A > 60 and B < 20 and C > 60 and E < 10)):
        return 4
    if ((B > 85 and C > 80 and E > 30) or
        (B > 80 and C > 70 and D < 5 and E > 80) or
        (B > 80 and C > 50 and E > 50 and A < 50) or
        (A < 15 and B > 80 and C > 70 and D < 5 and E > 80)):
        return 2
    if ((A > 50 and C < 50 and D > 70) or
        (C > 90 and B < 20) or
        (A < 20 and D > 60 and C < 10) or
        (D < 10 and B < 50 and E < 30 and C > 20) or
        (A < 15 and C > 90 and D < 5) or
        (A < 20 and B < 25 and C < 10 and D > 60)):
        return 3
    else:
        return 1
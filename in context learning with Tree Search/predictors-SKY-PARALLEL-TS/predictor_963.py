"""
Predictor 963
Generated on: 2025-09-10 01:09:35
Accuracy: 49.79%
"""


# PREDICTOR 963 - Accuracy: 49.79%
# Correct predictions: 4979/10000 (49.79%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 55) or
        (C < 25 and E > 70 and (B > 40 or D > 40)) or
        (B < 10 and C > 70) or
        (D < 10 and E > 70 and A < 50) or
        (C < 10 and B < 25 and E > 50 and A < 80) or
        (A < 5 and B > 50 and C > 20 and E < 25) or
        (E > 70 and D < 20 and C > 30) or
        (B > 90 and E > 70) or
        (A > 60 and B < 40 and C > 40)):
        return 4
    if ((B > 70 and C > 70 and E < 20) or
        (B > 85 and C > 80) or
        (A + B > 140 and D < 20 and E > 40) or
        (B > 80 and E < 30) or
        (B > 90 and C < 40) or
        (A > 70 and B > 55 and E > 55)):
        return 2
    if ((A > 50 and C < 50 and D > 50 and B > 35) or
        (A < 50 and D < 25 and E < 20 and B < 80) or
        (D < 15 and C > 40 and B < 80 and A < 70) or
        (C <= 10 and E < 60 and B < 50) or
        (A > 75 and B < 25 and C < 45 and D > 60)):
        return 3
    else:
        return 1
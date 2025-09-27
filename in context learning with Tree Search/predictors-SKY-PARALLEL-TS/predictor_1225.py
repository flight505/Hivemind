"""
Predictor 1225
Generated on: 2025-09-10 01:48:40
Accuracy: 54.67%
"""


# PREDICTOR 1225 - Accuracy: 54.67%
# Correct predictions: 5467/10000 (54.67%)

def predict_output(A, B, C, D, E):
    if B > 90 and E < 20:
        return 3
    if ((A < 10 and B > 70 and E < 20) or
        (C < 15 and D > 90) or
        (C > 60 and D < 20) or
        (C < 30 and E > 80 and B > 60) or
        (B > 70 and D < 25 and E > 70) or
        (C > 80 and E < 10) or
        (30 < A < 40 and B < 60 and C < 40 and D < 40 and E < 20) or
        (A > 50 and B > 50 and C > 50 and D < 20 and E > 80)):
        return 4
    if ((B > 85 and C > 80 and A < 50) or
        (A < 10 and E > 80 and B < 60)):
        return 2
    if (A > 80 and B < 30 and D > 60 and E > 90) or (A < 10 and B > 90 and C < 30):
        return 3
    else:
        return 1
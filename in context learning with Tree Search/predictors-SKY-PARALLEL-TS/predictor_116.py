"""
Predictor 116
Generated on: 2025-09-09 23:30:47
Accuracy: 61.66%
"""


# PREDICTOR 116 - Accuracy: 61.66%
# Correct predictions: 6166/10000 (61.66%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70 and C < 85) or
        (C < 15 and D > 55 and E > 80) or
        (C < 25 and E > 65) or
        (C > 70 and E < 20 and B < 10 and A > 70) or
        (A > 80 and B < 10 and D > 70 and E < 10) or
        (40 < A < 60 and B < 40 and C < 30 and E < 5) or
        (C < 5 and A > 90 and B > 85) or
        (A < 20 and B < 25 and C > 75 and D < 30)):
        return 4
    if ((B > 85 and C > 80 and A < 80 and D < 80) or
        (B > 70 and D < 20 and A < 50 and E > 40) or
        (B > 40 and C > 50 and D < 10 and E > 50)):
        return 2
    if ((A > 50 and C < 50 and D > 70 and B > 40) or
        (A < 50 and D < 25 and E < 20 and B < 80) or
        (D < 15 and C > 40 and B < 80 and A < 70) or
        (C <= 10 and E < 60 and B < 50) or
        (A > 75 and B < 25 and C < 45 and D > 60) or
        (B > 90 and D > 95) or
        (B > 80 and C > 90 and D > 80) or
        (A > 40 and B > 35 and C < 25 and D < 20) or
        (A > 60 and B > 60 and C < 50 and D > 65)):
        return 3
    else:
        return 1
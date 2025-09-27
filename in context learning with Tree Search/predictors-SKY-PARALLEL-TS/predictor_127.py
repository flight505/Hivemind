"""
Predictor 127
Generated on: 2025-09-09 23:30:47
Accuracy: 59.82%
"""


# PREDICTOR 127 - Accuracy: 59.82%
# Correct predictions: 5982/10000 (59.82%)

def predict_output(A, B, C, D, E):
    if ((A < 15 and B > 70) or
        (C < 15 and D > 55 and E > 80) or
        (C < 25 and E > 65 and A > 50) or
        (C > 70 and E < 20 and B < 10 and A > 70) or
        (A > 80 and B < 10 and D > 70 and E < 10) or
        (B < 5 and C > 65) or
        (B < 25 and C < 10 and E > 55) or
        (D < 10 and E > 75 and A > 45)):
        return 4
    if ((B > 85 and C > 80 and A < 80) or
        (B > 70 and D < 20 and A < 50 and E > 40) or
        (B > 70 and C > 70 and E < 15)):
        return 2
    if ((A > 50 and C < 50 and D > 70 and B > 40) or
        (A < 50 and D < 25 and E < 20 and B < 80) or
        (D < 15 and C > 40 and B < 80 and A < 70 and E < 20) or
        (C <= 10 and E < 60 and B < 50 and A < 70) or
        (A > 75 and B < 25 and C < 45 and D > 60)):
        return 3
    else:
        return 1
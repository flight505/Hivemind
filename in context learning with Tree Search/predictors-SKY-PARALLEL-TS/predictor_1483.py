"""
Predictor 1483
Generated on: 2025-09-10 02:33:36
Accuracy: 50.41%
"""


# PREDICTOR 1483 - Accuracy: 50.41%
# Correct predictions: 5041/10000 (50.41%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 20 and D > 80) or
        (B < 20 and C > 60) or
        (B < 20 and D > 65) or
        (E > 90 and D < 50) or
        (B > 80 and C < 20 and D > 85 and E < 20) or
        (B > 85 and E > 85) or
        (A > 35 and B < 30 and C > 50 and D > 40 and E > 35) or
        (C < 10 and A < 10 and E > 65 and D > 50 and B > 50)):
        return 4
    elif (A > 60 and B > 50 and C > 30 and D > 40 and E < 15) or \
         (B > 95 and E < 15 and A > 60):
        return 2
    elif (A > 70 and B < 20 and C < 40 and D < 25 and E < 20) or \
         (A > 50 and C < 50 and D > 70 and B > 40):
        return 3
    else:
        return 1
"""
Predictor 823
Generated on: 2025-09-10 00:50:44
Accuracy: 49.74%
"""


# PREDICTOR 823 - Accuracy: 49.74%
# Correct predictions: 4974/10000 (49.74%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 80) or (A < 15 and C > 65) or (A > 90 and C < 5 and D > 80) or (B > 60 and D < 30 and E > 80):
        return 4
    elif (C > 70 and D < 10) or (B > 70 and D < 20 and A < 50 and E > 40) or (A > 90 and E < 10):
        return 2
    elif (D > 80 and (A > 70 or B > 70 or C > 70)) or (A > 50 and C < 50 and D > 70 and B > 40):
        return 3
    else:
        return 1
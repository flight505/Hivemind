"""
Predictor 821
Generated on: 2025-09-10 00:50:44
Accuracy: 53.56%
"""


# PREDICTOR 821 - Accuracy: 53.56%
# Correct predictions: 5356/10000 (53.56%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 20 and D > 80 and B > 50) or
        (A < 20 and C > 60 and D < 30) or
        (A > 80 and D < 25 and E > 80) or
        (A < 20 and C > 90) or
        (A > 90 and C < 5 and D > 80)):
        return 4
    elif (C > 70 and D < 10):
        return 2
    elif (D > 80 and (A > 70 or B > 70)):
        return 3
    else:
        return 1
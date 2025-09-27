"""
Predictor 1050
Generated on: 2025-09-10 01:23:11
Accuracy: 56.85%
"""


# PREDICTOR 1050 - Accuracy: 56.85%
# Correct predictions: 5685/10000 (56.85%)

def predict_output(A, B, C, D, E):
    if ((A < 10 and B > 70) or
        (C < 15 and D > 90) or
        (B > 70 and C < 10 and E > 90) or
        (E > 80 and D < 35 and C < 70) or
        (A < 15 and B < 30 and C > 55 and D < 25 and E < 20) or
        (A > 85 and B < 15 and D > 60 and E < 20) or
        (A < 10 and B > 55 and C < 5 and E > 80)):
        return 4
    elif ((B > 85 and C > 80) or
          (A < 50 and B < 15 and C > 70 and D < 5 and E > 90)):
        return 2
    elif ((A > 90 and B < 30 and D > 95) or
          (B > 60 and C < 30 and E < 5 and D < 35)):
        return 3
    else:
        return 1
"""
Predictor 431
Generated on: 2025-09-10 00:02:23
Accuracy: 57.28%
"""


# PREDICTOR 431 - Accuracy: 57.28%
# Correct predictions: 5728/10000 (57.28%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90 and E > 80) or (E > 80 and B > 60 and C < 35) or (E - C > 60):
        return 4
    elif (A > 90 and E < 10) or (B > 85 and C > 80 and A < 70) or (D < 5 and E > 70) or (A < 20 and B > 40 and C < 10 and E > 50) or (A < 10 and B > 90) or (B - A > 80 and C > 60):
        return 2
    elif (A < 20 and B > 70 and D < 25 and E < 30) or (A >= 50 and C < 60 and D > 70 and B > 40 and B + C < 115) or (A > 90 and B < 10 and C < 15 and D > 90) or (A < 15 and B < 20 and C < 25 and D < 30 and E < 25) or (A + B < 80 and C > 40 and D > 50 and E < 40):
        return 3
    else:
        return 1
"""
Predictor 428
Generated on: 2025-09-10 00:02:23
Accuracy: 57.97%
"""


# PREDICTOR 428 - Accuracy: 57.97%
# Correct predictions: 5797/10000 (57.97%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90 and E > 80) or (E > 80 and B > 30 and D > 50 and C < 40):
        return 4
    if (B > 85 and C > 80 and A < 50) or (D < 5 and A < 50 and E > 70) or (A < 20 and C < 20 and E > 50) or (A < 10 and B > 90 and C > 60) or (E > 75 and C < 50 and A > 50 and B > 50):
        return 2
    if (A < 20 and B > 70 and D < 25 and E < 30) or (A >= 50 and C < 60 and D > 70 and B > 40 and B + C < 115) or (A > 90 and B < 10 and C < 15 and D > 90) or (A < 15 and B < 20 and C < 25 and D < 30 and E < 25):
        return 3
    else:
        return 1
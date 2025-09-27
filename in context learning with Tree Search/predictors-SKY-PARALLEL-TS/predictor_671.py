"""
Predictor 671
Generated on: 2025-09-10 00:31:36
Accuracy: 43.92%
"""


# PREDICTOR 671 - Accuracy: 43.92%
# Correct predictions: 4392/10000 (43.92%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 20 and D > 60) or (D > 60 and E < 20) or (C > 50 and B < 40) or (A > 70 and B < 30 and C > 55):
        return 4
    elif (A > 80 and B < 15 and C < 30 and D < 25) or (B > 80 and D > 85 and E < 30) or (A > 70 and B < 20 and C < 10):
        return 3
    elif (A < 25 and B > 70 and D < 20) or (A > 80 and B > 80 and E < 25) or (B > 85 and C > 35 and E < 25):
        return 2
    else:
        return 1
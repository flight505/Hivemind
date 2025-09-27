"""
Predictor 519
Generated on: 2025-09-10 00:14:11
Accuracy: 46.54%
"""


# PREDICTOR 519 - Accuracy: 46.54%
# Correct predictions: 4654/10000 (46.54%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90 and E > 80) or (C > 60 and A < 20 and B < 60) or (B > 70 and C > 60) or (C > 80 and D < 25 and E < 20) or (B < 20 and C < 20 and A > 40):
        return 4
    elif (A > 70 and D > 80 and E > 70) or (B > 80 and C > 80 and D > 80) or (C < 15 and D > 90 and E < 20):
        return 3
    elif (B < 20 and D < 20 and E > 50) or (D < 10 and E > 60):
        return 2
    else:
        return 1
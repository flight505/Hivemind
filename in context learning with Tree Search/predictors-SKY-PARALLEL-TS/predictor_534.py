"""
Predictor 534
Generated on: 2025-09-10 00:14:11
Accuracy: 52.98%
"""


# PREDICTOR 534 - Accuracy: 52.98%
# Correct predictions: 5298/10000 (52.98%)

def predict_output(A, B, C, D, E):
    if (B > 90 and D < 30 and E > 60) or (D < 10 and C > 30 and E > 50) or (A > 90 and B > 80 and E < 50):
        return 2
    if (A < 10 and B > 70 and E < 20) or (C < 10 and D > 90) or (B > 95) or (D < 10 and E > 60) or (C > 60 and D < 25 and E > 80) or (B < 20 and D > 40 and E < 25):
        return 4
    if (B + E > 150 and A + D < 50) or (B < 10 and D > 80):
        return 3
    else:
        return 1
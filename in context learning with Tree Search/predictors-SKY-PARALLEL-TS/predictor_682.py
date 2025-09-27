"""
Predictor 682
Generated on: 2025-09-10 00:34:06
Accuracy: 50.66%
"""


# PREDICTOR 682 - Accuracy: 50.66%
# Correct predictions: 5066/10000 (50.66%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 90 and E > 80) or (C > 90 and D < 40 and E < 30) or (C < 20 and B > 70 and E > 50):
        return 4
    if (B > 80 and C > 50) or (A > 90 and B > 50) or (A < 10 and B > 60 and E > 55):
        return 2
    if (A > 50 and B < 20 and C < 20) or (D < 15 and C > 40) or (A > 40 and B > 35 and C > 25 and D < 30 and E < 5) or (A > 70 and B < 20 and C < 30):
        return 3
    else:
        return 1
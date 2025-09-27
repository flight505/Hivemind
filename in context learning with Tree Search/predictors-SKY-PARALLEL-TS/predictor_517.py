"""
Predictor 517
Generated on: 2025-09-10 00:14:11
Accuracy: 51.97%
"""


# PREDICTOR 517 - Accuracy: 51.97%
# Correct predictions: 5197/10000 (51.97%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 10 and D > 90) or (C > 60 and D < 30) or (B < 20 and C < 20 and 30 < D < 60 and E > 40):
        return 4
    elif (A > 70 and D > 80 and E > 70) or (B > 80 and C > 80 and D > 80) or (C < 15 and D > 90 and E < 20):
        return 3
    elif D < 15 and E > 50:
        return 2
    else:
        return 1
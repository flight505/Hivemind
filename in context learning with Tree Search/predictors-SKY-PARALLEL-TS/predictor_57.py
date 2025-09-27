"""
Predictor 57
Generated on: 2025-09-09 23:24:50
Accuracy: 59.66%
"""


# PREDICTOR 57 - Accuracy: 59.66%
# Correct predictions: 5966/10000 (59.66%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (C < 25 and E > 70) or (B > 90 and E > 75):
        return 4
    if (A > 90 and E < 10 and D < 70) or (B > 85 and C > 80) or (C > 55 and D < 10 and E > 85):
        return 2
    if (A > 40 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C < 10 and E < 60) or (B > 50 and D > 50 and C < 20):
        return 3
    else:
        return 1
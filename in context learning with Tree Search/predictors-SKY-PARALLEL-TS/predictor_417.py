"""
Predictor 417
Generated on: 2025-09-10 00:02:23
Accuracy: 58.45%
"""


# PREDICTOR 417 - Accuracy: 58.45%
# Correct predictions: 5845/10000 (58.45%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C < 40) or (C < 15 and D > 55) or (C < 25 and E > 70):
        return 4
    if (B > 85 and C > 80 and E < 50) or (B > 70 and D < 20 and A < 50 and E > 40 and C < 40) or (B < 20 and D < 10 and E > 60):
        return 2
    if (A > 50 and C < 50 and D > 70 and B > 40) or (C > 80 and D > 70) or (C < 15 and D > 50) or (40 < A < 60 and C < 30 and D < 15 and B < 50) or (A < 50 and D < 25 and E < 20 and B < 80) or (C <= 10 and E < 60 and B < 60) or (D < 15 and C > 40 and B < 80 and E < 30 and A < 60):
        return 3
    else:
        return 1
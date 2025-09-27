"""
Predictor 416
Generated on: 2025-09-10 00:02:23
Accuracy: 56.93%
"""


# PREDICTOR 416 - Accuracy: 56.93%
# Correct predictions: 5693/10000 (56.93%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C < 40) or (C < 15 and D > 60) or (C < 25 and E > 70):
        return 4
    if (B > 85 and C > 80 and A < 50) or (B > 70 and D < 20 and A < 50 and E > 40 and C < 40) or (B < 20 and D < 10 and E > 60):
        return 2
    if (C > 80 and D > 70) or (C < 15 and D > 50) or (D < 15 and C > 20 and B < 60 and E < 50):
        return 3
    else:
        return 1
"""
Predictor 64
Generated on: 2025-09-09 23:24:50
Accuracy: 59.56%
"""


# PREDICTOR 64 - Accuracy: 59.56%
# Correct predictions: 5956/10000 (59.56%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (C < 25 and E > 70) or (C > 70 and D < 25 and E < 25 and A < 50) or (A > 80 and B < 10 and E < 10):
        return 4
    if (B > 85 and C > 80) or (B > 70 and D < 20 and A < 50):
        return 2
    if (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C < 11 and E < 60):
        return 3
    else:
        return 1
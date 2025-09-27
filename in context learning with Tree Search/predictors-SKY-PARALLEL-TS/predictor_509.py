"""
Predictor 509
Generated on: 2025-09-10 00:11:10
Accuracy: 53.45%
"""


# PREDICTOR 509 - Accuracy: 53.45%
# Correct predictions: 5345/10000 (53.45%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and C < 40) or (C < 15 and D > 90):
        return 4
    if (B > 85 and C > 80) or (B > 70 and D < 20 and A < 50 and E > 40) or (A < 10 and B > 90 and C > 60 and E < 10) or (B > 80 and E > 90 and A > 70) or (C > 90 and B > 60 and D < 40):
        return 2
    if (A > 80 and B < 30 and D > 60 and E > 90) or (A > 70 and E < 10 and D > 50) or (B < 10 and D > 50 and C < 20) or (A > 90 and D > 80) or (D < 25 and C > 40 and A < 40) or (B < 10 and C > 75 and D < 5) or (A > 70 and B > 40 and C < 45 and D > 50 and E < 10):
        return 3
    else:
        return 1
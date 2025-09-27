"""
Predictor 75
Generated on: 2025-09-09 23:24:50
Accuracy: 58.34%
"""


# PREDICTOR 75 - Accuracy: 58.34%
# Correct predictions: 5834/10000 (58.34%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70 and D < 50) or (C < 15 and D > 55) or (C < 25 and E > 70) or (D < 5 and E > 70 and A > 40):
        return 4
    if (A > 90 and E < 10) or (B > 85 and C > 80) or (A < 10 and B > 90) or (D < 5 and E > 70 and B < 20) or (A - C > 10 and E > 75) or (A < 5 and C < 12 and E > 50):
        return 2
    if (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C < 10 and E < 60) or (A > 50 and C < 15 and E < 20):
        return 3
    else:
        return 1
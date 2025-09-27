"""
Predictor 66
Generated on: 2025-09-09 23:24:50
Accuracy: 59.58%
"""


# PREDICTOR 66 - Accuracy: 59.58%
# Correct predictions: 5958/10000 (59.58%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (C < 25 and E > 70) or (C > 70 and D < 25 and E < 25 and A < 50) or (A > 80 and E < 10 and B < 20):
        return 4
    if (A > 90 and E < 10 and B > 80) or (B > 85 and C > 80) or (B > 70 and D < 20 and A < 50):
        return 2
    if (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20 and B < 80) or (D < 15 and C > 40 and B < 80) or (C < 10 and E < 60) or (A < 30 and C < 15 and D > 25):
        return 3
    else:
        return 1
"""
Predictor 32
Generated on: 2025-09-09 23:19:12
Accuracy: 54.82%
"""


# PREDICTOR 32 - Accuracy: 54.82%
# Correct predictions: 5482/10000 (54.82%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 15 and D > 55) or (A < 10 and E < 10) or (B < 20 and C > 50):
        return 4
    elif (A > 90 and E < 10) or (C > 90 and D < 10):
        return 2
    elif (A > 50 and C < 50 and D > 70 and B > 40) or (A < 50 and D < 25 and E < 20):
        return 3
    else:
        return 1
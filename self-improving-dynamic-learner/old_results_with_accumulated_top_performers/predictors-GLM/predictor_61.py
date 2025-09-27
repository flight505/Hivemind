"""
Predictor 61
Generated on: 2025-09-09 05:55:40
Accuracy: 56.32%
"""


# PREDICTOR 61 - Accuracy: 56.32%
# Correct predictions: 5632/10000 (56.32%)

def predict_output(A, B, C, D, E):
    if (B <= 15 and C <= 12 and E < 40) or (B <= 30 and D >= 80 and C < 50 and E >= 20):
        return 3
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or (B >= 80 and C <= 35 and D >= 60 and A >= 50):
        return 4
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or (B >= 90 and C >= 80):
        return 2
    else:
        return 1
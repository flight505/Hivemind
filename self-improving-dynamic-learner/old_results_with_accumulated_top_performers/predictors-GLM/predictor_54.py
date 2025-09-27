"""
Predictor 54
Generated on: 2025-09-09 05:52:21
Accuracy: 54.77%
"""


# PREDICTOR 54 - Accuracy: 54.77%
# Correct predictions: 5477/10000 (54.77%)

def predict_output(A, B, C, D, E):
    if (B <= 15 and C <= 12 and E < 40):
        return 3
    elif (B >= 28 and B <= 36 and D >= 15 and D <= 36) or (E >= 90):
        return 4
    elif (B >= 65 and A <= 50 and C >= 70 and A > 20) or (B >= 90 and C >= 80):
        return 2
    else:
        return 1
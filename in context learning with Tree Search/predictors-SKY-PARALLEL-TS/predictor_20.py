"""
Predictor 20
Generated on: 2025-09-09 23:19:12
Accuracy: 49.30%
"""


# PREDICTOR 20 - Accuracy: 49.30%
# Correct predictions: 4930/10000 (49.30%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 70) or (C < 20 and D > 80) or (B < 20 and C > 60) or (B < 20 and D > 65) or (E > 90 and D < 50):
        return 4
    elif A > 90 and E < 10:
        return 2
    elif B > 90 and E < 15:
        return 3
    elif A > 70 and B < 20 and C < 10:
        return 3
    elif D > 90 and E > 70:
        return 3
    else:
        return 1
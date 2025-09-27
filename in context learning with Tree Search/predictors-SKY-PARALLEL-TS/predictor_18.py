"""
Predictor 18
Generated on: 2025-09-09 23:19:12
Accuracy: 44.99%
"""


# PREDICTOR 18 - Accuracy: 44.99%
# Correct predictions: 4499/10000 (44.99%)

def predict_output(A, B, C, D, E):
    if (B > 70 and A < 80) or (C < 15 and D > 75) or (D < 20 and E > 75) or (B < 15 and A > 80):
        return 4
    elif A > 80 and E < 50 and D > 50:
        return 2
    elif D > 80 and C < 40:
        return 3
    else:
        return 1
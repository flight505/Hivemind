"""
Predictor 17
Generated on: 2025-09-09 23:19:12
Accuracy: 48.11%
"""


# PREDICTOR 17 - Accuracy: 48.11%
# Correct predictions: 4811/10000 (48.11%)

def predict_output(A, B, C, D, E):
    if (B > 70 and A < 70) or (C < 20 and D > 70) or (E > 90 and D < 20) or (A > 80 and B < 10):
        return 4
    elif A > 80 and E < 40 and D > 50:
        return 2
    elif D > 80 and C < 40:
        return 3
    else:
        return 1
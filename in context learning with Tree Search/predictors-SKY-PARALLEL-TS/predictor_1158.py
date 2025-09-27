"""
Predictor 1158
Generated on: 2025-09-10 01:37:38
Accuracy: 56.11%
"""


# PREDICTOR 1158 - Accuracy: 56.11%
# Correct predictions: 5611/10000 (56.11%)

def predict_output(A, B, C, D, E):
    if (A < 10 and B > 65 and E < 20) or (C < 15 and D > 90 and A > 50) or (C < 5 and E > 60) or (D < 25 and E > 90):
        return 4
    elif B > 80 and C > 70 and E < 60:
        return 2
    elif A > 65 and C > 30 and E < 10:
        return 3
    else:
        return 1
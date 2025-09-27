"""
Predictor 5
Generated on: 2025-09-09 23:16:45
Accuracy: 50.82%
"""


# PREDICTOR 5 - Accuracy: 50.82%
# Correct predictions: 5082/10000 (50.82%)

def predict_output(A, B, C, D, E):
    if (A + C < 100) and (B + D > 120):
        return 4
    elif A > 80 and B < 20:
        return 2
    elif E > 80 and C < 20:
        return 3
    else:
        return 1
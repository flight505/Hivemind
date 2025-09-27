"""
Predictor 1239
Generated on: 2025-09-10 01:48:40
Accuracy: 49.22%
"""


# PREDICTOR 1239 - Accuracy: 49.22%
# Correct predictions: 4922/10000 (49.22%)

def predict_output(A, B, C, D, E):
    sum_abc = A + B + C
    diff_de = D - E
    ratio_be = B / E if E != 0 else 0
    if (A < 10 and B > 70) or (C < 15 and D > 90 and E > 80):
        return 4
    elif sum_abc > 200 and diff_de > 20:
        return 2
    elif ratio_be > 2 and C < D:
        return 3
    else:
        return 1
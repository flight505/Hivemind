"""
Predictor 211
Generated on: 2025-09-09 08:23:02
Accuracy: 50.16%
"""


# PREDICTOR 211 - Accuracy: 50.16%
# Correct predictions: 5016/10000 (50.16%)

def predict_output(A, B, C, D, E):
    if C < 15 and B < 20:
        return 3
    if E > 90 and D < 40:
        return 4
    if C >= 58:
        if A > 50:
            return 1
        else:
            return 2
    return 1
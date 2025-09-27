"""
Predictor 1
Generated on: 2025-09-09 12:02:28
Accuracy: 49.65%
"""


# PREDICTOR 1 - Accuracy: 49.65%
# Correct predictions: 4965/10000 (49.65%)

def predict_output(A, B, C, D, E):
    if C <= 12:
        return 3
    if E >= 95:
        return 4
    if A <= 35 and C >= 70:
        return 2
    return 1
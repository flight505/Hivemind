"""
Predictor 231
Generated on: 2025-09-09 09:46:02
Accuracy: 50.21%
"""


# PREDICTOR 231 - Accuracy: 50.21%
# Correct predictions: 5021/10000 (50.21%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if C < 20:
        if B > 20:
            return 1
        else:
            return 3
    if C >= 70:
        if A > 50:
            return 1
        else:
            return 2
    return 1
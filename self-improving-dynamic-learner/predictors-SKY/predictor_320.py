"""
Predictor 320
Generated on: 2025-09-09 15:26:28
Accuracy: 50.20%
"""


# PREDICTOR 320 - Accuracy: 50.20%
# Correct predictions: 5020/10000 (50.20%)

def predict_output(A, B, C, D, E):
    if B > 60 and C > 70:
        return 2
    if E > 90:
        return 4
    if B < 20 and C < 20:
        return 3
    if B > 80:
        return 1
    if D > 70:
        return 1
    return 1
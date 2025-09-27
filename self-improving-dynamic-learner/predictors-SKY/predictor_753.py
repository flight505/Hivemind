"""
Predictor 753
Generated on: 2025-09-09 20:23:26
Accuracy: 52.68%
"""


# PREDICTOR 753 - Accuracy: 52.68%
# Correct predictions: 5268/10000 (52.68%)

def predict_output(A, B, C, D, E):
    if B < 30 and C < 20 and D > 80 and E < 20:
        return 1
    if B < 30 and C < 20:
        return 3
    if C > 75 and E >= 70:
        return 2
    if E > 90 and C < 25:
        return 4
    if B > 80 or D > 70:
        return 1
    return 1
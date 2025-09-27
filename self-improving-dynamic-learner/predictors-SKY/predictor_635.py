"""
Predictor 635
Generated on: 2025-09-09 18:59:50
Accuracy: 43.31%
"""


# PREDICTOR 635 - Accuracy: 43.31%
# Correct predictions: 4331/10000 (43.31%)

def predict_output(A, B, C, D, E):
    if B < 20 and C < 20:
        return 3
    if B < 30 and C > 60:
        return 3
    if B > 60 and C > 70:
        return 2
    if E > 90:
        return 4
    return 1
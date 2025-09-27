"""
Predictor 628
Generated on: 2025-09-09 18:53:34
Accuracy: 54.26%
"""


# PREDICTOR 628 - Accuracy: 54.26%
# Correct predictions: 5426/10000 (54.26%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    if C > 75 and B > 60 and E >= 70:
        return 2
    if B + C < 30:
        return 3
    return 1
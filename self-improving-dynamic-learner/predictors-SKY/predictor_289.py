"""
Predictor 289
Generated on: 2025-09-09 15:05:36
Accuracy: 44.49%
"""


# PREDICTOR 289 - Accuracy: 44.49%
# Correct predictions: 4449/10000 (44.49%)

def predict_output(A, B, C, D, E):
    if B < 25 and C < 20:
        if E > 50:
            return 4
        return 3
    if B < 20 and C > 15:
        return 4
    if 30 < B < 60 and C < 30 and E < 30:
        return 3
    if C < 20 and D > 80 and B > 20 and E > 30:
        return 4
    if C < 25 and E > 60:
        return 4
    if B > 40 and C > 40 and E < 30:
        return 4
    if B > 60 and E < 30:
        return 2
    if B > 60 and C > 70:
        return 2
    return 1
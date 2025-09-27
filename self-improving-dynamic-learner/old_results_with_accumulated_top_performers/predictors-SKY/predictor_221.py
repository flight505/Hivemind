"""
Predictor 221
Generated on: 2025-09-09 08:58:04
Accuracy: 58.45%
"""


# PREDICTOR 221 - Accuracy: 58.45%
# Correct predictions: 5845/10000 (58.45%)

def predict_output(A, B, C, D, E):
    if C < 25:
        if B < 20 and E < 40:
            return 3
        elif E > 90:
            return 4
        else:
            return 1
    else:
        if B > 60 and E >= 70 and A < 50:
            return 2
        else:
            return 1
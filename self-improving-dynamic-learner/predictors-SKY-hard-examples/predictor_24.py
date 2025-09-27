"""
Predictor 24
Generated on: 2025-09-09 17:21:41
Accuracy: 59.89%
"""


# PREDICTOR 24 - Accuracy: 59.89%
# Correct predictions: 5989/10000 (59.89%)

def predict_output(A, B, C, D, E):
    if A < 20 and B > 50 and E < 30:
        return 4
    if C < 35 and E > 70:
        return 4
    if B < 35 and C < 20:
        if D > 80 and E < 20:
            return 1
        else:
            return 3
    if (B + E > 125) and C > 40 and 10 < A < 60:
        return 2
    return 1
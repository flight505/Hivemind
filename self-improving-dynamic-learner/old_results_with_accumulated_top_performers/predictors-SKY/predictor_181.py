"""
Predictor 181
Generated on: 2025-09-09 07:23:23
Accuracy: 56.45%
"""


# PREDICTOR 181 - Accuracy: 56.45%
# Correct predictions: 5645/10000 (56.45%)

def predict_output(A, B, C, D, E):
    if E > 90 and D < 40:
        return 4
    if C < 15:
        return 3
    if C > 70:
        if B > 60:
            if A >= 50:
                return 1
            else:
                return 2
        else:
            return 1
    if C < 40:
        return 1
    return 1
"""
Predictor 357
Generated on: 2025-09-09 09:37:14
Accuracy: 44.42%
"""


# PREDICTOR 357 - Accuracy: 44.42%
# Correct predictions: 4442/10000 (44.42%)

def predict_output(A, B, C, D, E):
    if C < 25:
        if B < 25:
            return 3
        else:
            if E >= 90:
                return 4
            else:
                return 1
    else:
        if C > 60:
            if A >= 70:
                return 1
            else:
                return 2
        else:
            return 1
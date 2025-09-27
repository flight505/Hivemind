"""
Predictor 318
Generated on: 2025-09-09 08:16:36
Accuracy: 46.51%
"""


# PREDICTOR 318 - Accuracy: 46.51%
# Correct predictions: 4651/10000 (46.51%)

def predict_output(A, B, C, D, E):
    if C < 25:
        if B < 25:
            return 3
        else:
            if E > 80:
                return 4
            else:
                return 1
    else:
        if C > 60:
            if A > 65:
                return 1
            else:
                return 2
        else:
            return 1
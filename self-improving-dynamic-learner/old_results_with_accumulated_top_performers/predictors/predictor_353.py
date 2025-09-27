"""
Predictor 353
Generated on: 2025-09-09 09:25:39
Accuracy: 47.75%
"""


# PREDICTOR 353 - Accuracy: 47.75%
# Correct predictions: 4775/10000 (47.75%)

def predict_output(A, B, C, D, E):
    if C < 25:
        if B < 25:
            return 3
        else:
            if E > 90:
                return 4
            else:
                return 1
    else:
        if A <= 30:
            return 2
        else:
            return 1
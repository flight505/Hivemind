"""
Predictor 338
Generated on: 2025-09-09 08:46:38
Accuracy: 42.11%
"""


# PREDICTOR 338 - Accuracy: 42.11%
# Correct predictions: 4211/10000 (42.11%)

def predict_output(A, B, C, D, E):
    if B > 70:
        if A > 50:
            return 1
        else:
            if D > 70:
                return 4
            else:
                return 2
    else:
        if E > 80:
            return 4
        else:
            if C > 60:
                return 1
            else:
                return 3
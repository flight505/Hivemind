"""
Predictor 269
Generated on: 2025-09-09 21:27:39
Accuracy: 44.11%
"""


# PREDICTOR 269 - Accuracy: 44.11%
# Correct predictions: 4411/10000 (44.11%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C >= 50:
            return 2
        else:
            if D < 30:
                return 1
            else:
                return 4
    else:
        if C >= 50:
            if D < 30:
                return 4
            else:
                return 1
        else:
            if E < 20:
                return 1
            else:
                return 3
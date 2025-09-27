"""
Predictor 290
Generated on: 2025-09-09 21:35:39
Accuracy: 46.43%
"""


# PREDICTOR 290 - Accuracy: 46.43%
# Correct predictions: 4643/10000 (46.43%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C > 50:
            return 2
        else:
            if E > 50 or D > 50:
                return 4
            else:
                return 1
    else:
        if C > 50:
            if E > 50 or D > 50:
                return 1
            else:
                return 4
        else:
            if E < 20:
                return 1
            else:
                return 3
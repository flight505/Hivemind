"""
Predictor 3
Generated on: 2025-09-09 18:56:44
Accuracy: 44.32%
"""


# PREDICTOR 3 - Accuracy: 44.32%
# Correct predictions: 4432/10000 (44.32%)

def predict_output(A, B, C, D, E):
    if E < 20:
        if B >= 80:
            if D > 50:
                return 4
            else:
                return 1
        else:
            if C > 50:
                return 4
            else:
                return 1
    else:
        if B >= 80:
            if C < 50:
                return 4
            else:
                return 2
        else:
            if C > 50:
                return 1
            else:
                return 3
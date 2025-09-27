"""
Predictor 2
Generated on: 2025-09-09 18:56:44
Accuracy: 38.97%
"""


# PREDICTOR 2 - Accuracy: 38.97%
# Correct predictions: 3897/10000 (38.97%)

def predict_output(A, B, C, D, E):
    if C > 50:
        if B > 90:
            return 2
        elif B < 40:
            return 4
        else:
            return 1
    else:
        if B >= 80:
            if D > 40:
                return 4
            else:
                return 1
        else:
            if E < 20:
                return 1
            else:
                return 3
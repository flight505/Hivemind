"""
Predictor 1
Generated on: 2025-09-09 18:56:44
Accuracy: 45.27%
"""


# PREDICTOR 1 - Accuracy: 45.27%
# Correct predictions: 4527/10000 (45.27%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C < 50:
            if D < 40:
                return 1
            else:
                return 4
        else:
            return 2
    else:
        if C > 50:
            if E < 20:
                return 4
            else:
                return 1
        else:
            if E < 20:
                return 1
            else:
                return 3
"""
Predictor 4
Generated on: 2025-09-09 18:56:45
Accuracy: 36.42%
"""


# PREDICTOR 4 - Accuracy: 36.42%
# Correct predictions: 3642/10000 (36.42%)

def predict_output(A, B, C, D, E):
    if C < 50:
        if B >= 80:
            if D < 40:
                return 1
            else:
                return 4
        else:
            if E < 20:
                return 1
            else:
                return 3
    else:
        if B >= 80:
            return 2
        elif B < 40:
            return 4
        else:
            return 1
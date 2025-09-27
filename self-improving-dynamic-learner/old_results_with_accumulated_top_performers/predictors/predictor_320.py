"""
Predictor 320
Generated on: 2025-09-09 08:19:46
Accuracy: 39.51%
"""


# PREDICTOR 320 - Accuracy: 39.51%
# Correct predictions: 3951/10000 (39.51%)

def predict_output(A, B, C, D, E):
    if C < 25:
        if B < 25:
            if E > 80:
                return 4
            else:
                return 3
        else:
            if A > 70 or sum(A, B, C, D, E) > 300:
                return 1
            else:
                return 4
    else:
        if C > 60:
            if A > 70:
                return 1
            else:
                return 2
        else:
            return 1
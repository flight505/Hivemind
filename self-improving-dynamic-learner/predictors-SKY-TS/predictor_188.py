"""
Predictor 188
Generated on: 2025-09-09 20:48:52
Accuracy: 44.22%
"""


# PREDICTOR 188 - Accuracy: 44.22%
# Correct predictions: 4422/10000 (44.22%)

def predict_output(A, B, C, D, E):
    if B >= 80:
        if C > 50:
            if E > 70:
                return 4
            else:
                return 2
        else:
            if D > 40 or E > 50:
                return 4
            else:
                return 1
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
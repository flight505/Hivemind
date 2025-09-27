"""
Predictor 91
Generated on: 2025-09-09 05:01:45
Accuracy: 54.40%
"""


# PREDICTOR 91 - Accuracy: 54.40%
# Correct predictions: 5440/10000 (54.40%)

def predict_output(A, B, C, D, E):
    if C < 25:
        if B < 20:
            return 3
        elif B > 80:
            return 1
        else:
            if E > 90:
                return 4
            else:
                return 1
    else:
        if B < 50:
            return 1
        else:
            if A >= 50:
                return 1
            else:
                return 2
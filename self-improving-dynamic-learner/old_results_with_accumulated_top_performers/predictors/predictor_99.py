"""
Predictor 99
Generated on: 2025-09-09 03:55:55
Accuracy: 38.95%
"""


# PREDICTOR 99 - Accuracy: 38.95%
# Correct predictions: 3895/10000 (38.95%)

def predict_output(A, B, C, D, E):
    # Simple decision tree based on patterns from high C, low B, high E, high D
    if C > 60:
        if B > 70:
            return 1
        else:
            return 2
    elif E > 80:
        return 4
    elif B < 25 and C < 25:
        return 3
    else:
        return 1
"""
Predictor 1
Generated on: 2025-09-09 03:32:32
Accuracy: 35.24%
"""


# PREDICTOR 1 - Accuracy: 35.24%
# Correct predictions: 3524/10000 (35.24%)

def predict_output(A, B, C, D, E):
    """
    Predicts the categorical output (1-4) based on simple arithmetic thresholds.
    """
    if B <= 15:
        return 3
    if E > 90:
        return 4
    if C > 70:
        return 2
    return 1
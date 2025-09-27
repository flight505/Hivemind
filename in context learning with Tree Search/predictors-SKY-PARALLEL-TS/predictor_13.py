"""
Predictor 13
Generated on: 2025-09-09 23:16:45
Accuracy: 33.10%
"""


# PREDICTOR 13 - Accuracy: 33.10%
# Correct predictions: 3310/10000 (33.10%)

def predict_output(A, B, C, D, E):
    if B > 75 or D > 93:
        return 4
    elif (A + C) > 140:
        return 2
    elif (E - D) > 70:
        return 3
    else:
        return 1
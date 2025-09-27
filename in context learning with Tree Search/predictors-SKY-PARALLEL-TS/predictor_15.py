"""
Predictor 15
Generated on: 2025-09-09 23:16:45
Accuracy: 34.98%
"""


# PREDICTOR 15 - Accuracy: 34.98%
# Correct predictions: 3498/10000 (34.98%)

def predict_output(A, B, C, D, E):
    if B > 75 or (D > 90 and E > 80):
        return 4
    elif A + C > 140:
        return 2
    elif E - D > 70:
        return 3
    else:
        return 1
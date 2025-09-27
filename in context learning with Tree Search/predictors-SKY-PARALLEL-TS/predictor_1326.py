"""
Predictor 1326
Generated on: 2025-09-10 02:07:02
Accuracy: 57.31%
"""


# PREDICTOR 1326 - Accuracy: 57.31%
# Correct predictions: 5731/10000 (57.31%)

def predict_output(A, B, C, D, E):
    if B > 70 and C < 20 and E < 20:
        return 3
    if B > 85 and A < 70:
        return 2
    if (B - A > 60 and C < 50) or (E - C > 65) or (D - C > 80):
        return 4
    else:
        return 1
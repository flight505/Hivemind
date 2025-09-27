"""
Predictor 417
Generated on: 2025-09-09 16:23:24
Accuracy: 51.10%
"""


# PREDICTOR 417 - Accuracy: 51.10%
# Correct predictions: 5110/10000 (51.10%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    elif B < 20 and C < 15:
        return 3
    elif B > 60 and C > 75:
        return 2
    else:
        return 1
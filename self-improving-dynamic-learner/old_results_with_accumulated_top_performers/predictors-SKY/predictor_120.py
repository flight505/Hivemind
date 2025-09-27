"""
Predictor 120
Generated on: 2025-09-09 05:38:11
Accuracy: 48.06%
"""


# PREDICTOR 120 - Accuracy: 48.06%
# Correct predictions: 4806/10000 (48.06%)

def predict_output(A, B, C, D, E):
    if E > 90:
        return 4
    elif C > 70 and A < 50:
        return 2
    elif B > 80 or (D > 75 and A < 80):
        return 1
    elif C < 20 and A > 40:
        return 3
    else:
        return 1
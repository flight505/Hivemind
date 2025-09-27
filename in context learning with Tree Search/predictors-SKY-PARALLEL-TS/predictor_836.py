"""
Predictor 836
Generated on: 2025-09-10 00:53:24
Accuracy: 51.34%
"""


# PREDICTOR 836 - Accuracy: 51.34%
# Correct predictions: 5134/10000 (51.34%)

def predict_output(A, B, C, D, E):
    if (B - A > 60 and E < 20) or (D - C > 80):
        return 4
    elif A + B > 120 and E < 20:
        return 2
    elif B > 70 and D > 70:
        return 3
    else:
        return 1